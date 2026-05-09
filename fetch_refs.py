"""
从 tushare-data/references/数据接口.md 解析表格，批量下载接口文档到 references/ 目录
"""
import os
import re
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "tushare-data" / "references" / "数据接口.md"
OUT = ROOT / "references"

def parse_table(md_text: str) -> list[dict]:
    """解析 markdown 表格，提取接口信息"""
    entries = []
    for line in md_text.splitlines():
        # 匹配表格行: | [name](url) | title | categories | desc |
        m = re.match(
            r'\|\s*\[(\w+)\]\((https?://[^)]+)\)\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|',
            line,
        )
        if not m:
            continue
        name, url, title, categories, desc = m.groups()
        entries.append({
            "name": name.strip(),
            "url": url.strip(),
            "title": title.strip(),
            "categories": [c.strip() for c in categories.strip().split(",")],
            "desc": desc.strip(),
        })
    return entries

def fetch_markdown(url: str) -> str | None:
    """用 xh GET 下载 markdown 内容"""
    try:
        r = subprocess.run(
            ["xh", "GET", url],
            capture_output=True, text=True, timeout=30,
        )
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout
    except Exception as e:
        print(f"  [ERR] {url}: {e}")
    return None

def main():
    md_text = SRC.read_text(encoding="utf-8")
    entries = parse_table(md_text)
    print(f"共 {len(entries)} 个接口文档待下载")

    OUT.mkdir(exist_ok=True)
    ok, fail, skip = 0, 0, 0

    for i, e in enumerate(entries, 1):
        # 用分类做目录，标题做文件名
        cat_path = OUT / "/".join(e["categories"])
        # 文件名: 标题.md
        safe_title = re.sub(r'[<>:"/\\|?*]', '', e["title"])
        safe_title = safe_title.replace("（", "(").replace("）", ")")
        filepath = cat_path / f"{safe_title}.md"

        if filepath.exists():
            skip += 1
            continue

        cat_path.mkdir(parents=True, exist_ok=True)

        print(f"[{i}/{len(entries)}] {e['name']} → {filepath.relative_to(OUT)}")
        content = fetch_markdown(e["url"])
        if content:
            filepath.write_text(content, encoding="utf-8")
            ok += 1
            # 礼貌延时，避免请求过快
            time.sleep(0.3)
        else:
            fail += 1
            print(f"  [FAIL] {e['url']}")

    print(f"\n完成: {ok} 成功, {fail} 失败, {skip} 跳过(已存在)")

if __name__ == "__main__":
    main()
