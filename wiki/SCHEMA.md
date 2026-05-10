# Wiki Schema

## Domain
Tushare Pro 金融数据 API 文档知识库。覆盖 A股、港股、美股、ETF、公募基金、债券、期货、期权、宏观经济、行业经济等全品类金融数据接口。

## Conventions
- 文件名：中文原名，与 `raw/` 中对应分类目录名一致（如 `股票行情.md`、`可转债.md`）
- 每个 wiki 页面包含 YAML frontmatter
- 使用 `[[wikilinks]]` 链接相关页面（每页至少 2 个出链）
- 更新页面时更新 `updated` 日期
- 新页面必须添加到 `index.md` 对应分类下
- 每次操作追加到 `log.md`
- 来源标记：引用 raw 层源文件时使用 `^[raw/分类/文件名.md]`

## Frontmatter
```yaml
---
title: 页面标题
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query
tags: [from taxonomy below]
sources: [raw/分类/文件名.md]
---
```

## Tag Taxonomy

### 数据品类
- stock — A股数据
- etf — ETF数据
- fund — 公募基金
- bond — 债券（含可转债）
- futures — 期货
- options — 期权
- hk — 港股
- us — 美股
- forex — 外汇
- index — 指数
- spot — 现货（黄金等）

### 数据类型
- quote — 行情数据（日/周/月/分钟）
- fundamental — 财务基本面
- reference — 基础参考（列表、日历等）
- moneyflow — 资金流向
- macro — 宏观经济
- sentiment — 市场情绪/热点
- alternative — 另类数据（筹码、技术因子等）
- llm-corpus — 大模型语料

### 元标签
- realtime — 实时数据
- historical — 历史数据
- pro — 专业版/付费
- discontinued — 已停更

### 领域知识
- regulation — 监管制度与合规规则
- risk-mgmt — 风险管理
- quant — 量化投资方法论
- data-eng — 数据工程与偏差防范

## Page Thresholds
- **创建页面**：当一类接口涉及 3+ 个 API 或是核心数据品类
- **追加更新**：当新接口属于已有分类
- **不创建**：单独一个接口且不属于任何分类
- **拆分**：页面超过 200 行时拆分为子主题

## Update Policy
- tushare 接口文档更新后，重新运行 `fetch_refs.py` 同步 raw 层
- raw 层为不可变源文件，修正内容写入 wiki 页面
- 新增接口同步更新对应的 concept 页面和 index.md
