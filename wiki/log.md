# Wiki Log

> Tushare Pro 金融数据 API 知识库操作日志。只追加，不修改。
> Format: `## [YYYY-MM-DD] action | subject`

## [2026-05-09] create | Wiki 初始化
- Domain: Tushare Pro 金融数据 API
- 结构: SCHEMA.md + index.md + log.md + concepts/ (28 pages)
- Raw 层: symlink → ../references/ (229 个 API 文档)
- 概念页面按分类拆分: 股票数据 8 页、宏观经济 7 页、其余一级分类各 1 页

## [2026-05-09] ingest | 批量导入 raw 层
- 运行 fetch_refs.py 从 tushare.pro 下载 229 个接口文档
- 228 成功、1 失败(262.md 超时)后手动补回
- 来源: tushare-data/references/数据接口.md 表格中的所有链接
