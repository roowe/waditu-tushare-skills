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

## [2026-05-09] rewrite+create | 第二批页面更新
- 重写 concept 页 6 个: 公募基金、大模型语料(原大模型语料专题数据)、期权交易(原期权数据)、外汇与海外资产(原外汇数据)、行业经济与另类数据(原行业经济-TMT行业)、财富管理、黄金现货市场(原现货数据)
- 删除旧页 5 个: 大模型语料专题数据、期权数据、外汇数据、现货数据、行业经济-TMT行业
- 新建 query 页 5 个: 获取实时行情、获取历史分钟数据、查龙虎榜游资席位、对比AH股价差、获取概念板块成分

## [2026-05-09] create | 领域知识概念页批量创建 (8 agents 并行)
- 交易制度: 涨跌停机制、T+1与做T、集合竞价、停复牌、限售与解禁 (5 pages)
- 市场情绪: 游资与打板、情绪周期、次新股 (3 pages)
- 资金分析: 资金流向、沪深港通、融资融券、筹码分布 (4 pages)
- 估值基本面: 估值指标、盈利能力、杜邦分析、每股指标 (4 pages)
- 财务报表: 利润表、资产负债表、现金流量表 (3 pages)
- 财务比率: 偿债能力、营运能力、成长能力 (3 pages)
- 技术指标: 趋势类指标、震荡动量类指标 (2 pages)
- 行情基础: K线与复权、市场微观结构、行业分类 (3 pages)
- 债券: 可转债、国债收益率曲线、债券市场 (3 pages)
- 期货: 期货合约、期货持仓、商品指数 (3 pages)
- 宏观: 通胀指标、经济景气、货币与社融、利率体系、财经日历 (5 pages)
- 跨市场: AH股比价、ETF与指数投资 (2 pages)
- 公司治理: 股权质押、股东行为、公司治理、股票回购 (4 pages)
- 财报: 财报披露规则、财报补充概念 (2 pages)
- 卖方研究: 卖方研究与机构行为 (1 page)
- Entity: 东方财富、同花顺、通达信、开盘啦、港交所、Tushare社区 (6 pages)
- Comparison: 板块数据源对比、A股vs港股vs美股、行情接口选择、免费vs付费、资金流向对比 (5 pages)
- 总计新建 47 个领域知识概念页 + 6 entity + 5 comparison = 58 pages
- 当前 wiki 共 91 pages (75 concepts + 6 entities + 5 comparisons + 5 queries)

## [2026-05-09] update | P18 补全 21 个 API 目录页详细参数
- 为 21 个原有 API 目录页追加接口详细参数章节
- 每个接口新增: 调用说明(积分/频率/条数)、数据说明(更新时间/起始时间)、输入参数表、输出参数表
- 7 个并行 agent 分组处理: 股票行情+基础+财务(42 APIs)、资金+两融+参考+特色(39 APIs)、ETF+指数(27 APIs)、债券+期货(28 APIs)、港股+美股(20 APIs)、宏观(18 APIs)、打板(22 APIs)
- 共增强约 196 个 API 接口
- P19 导航更新: 补回 index.md 中遗漏的外汇与海外资产条目
- P20 Lint: 修复 6 个断链、14 个孤儿页面(添加入站 wikilink)
- 最终 lint: 91 pages, 0 broken, 0 orphans, 0 missing index, 0 frontmatter issues
