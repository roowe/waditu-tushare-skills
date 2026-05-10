---
title: ETF与指数投资
created: 2026-05-09
updated: 2026-05-10
type: concept
tags:
  - etf
  - index
  - fund
sources:
  - raw/ETF专题/ETF行情.md
  - raw/指数专题/指数行情.md
  - etf_basic
  - etf_share_size
  - etf_index
  - index_weight
  - index_dailybasic
---

# ETF与指数投资

> ETF（Exchange Traded Fund，交易型开放式指数基金）是一种在交易所上市交易的基金，通常跟踪某一特定指数，兼具股票和基金的特性。指数投资则以特定指数为标的，通过购买指数成分股或跟踪指数的ETF来实现分散投资。

## 核心概念

| 概念 | 说明 | 关键字段/接口 |
|------|------|---------------|
| ETF基本信息 | ETF产品的基础属性，包括代码、名称、跟踪指数等 | `etf_basic`：`ts_code`、`index_code`、`etf_type`、`mgt_fee` |
| 跟踪指数 | ETF所跟踪的基准指数代码 | `index_code`（如 000300.SH 对应沪深300指数） |
| QDII-ETF | 投资境外市场的ETF，如跟踪纳斯达克、标普500等 | `etf_type`="QDII"，涉及海外数据更新较晚 |
| ETF份额规模变动 | 每日ETF份额和规模变化，反映资金流入流出 | `etf_share_size`：`total_share`、`total_size`、`nav`、`close` |
| 基准指数 | ETF跟踪的指数基础信息，包括发布机构、基日、基点 | `etf_index`：`pub_party_name`、`base_date`、`bp`(基点) |
| 指数成分权重 | 指数成分股及其权重分配，月度数据 | `index_weight`：`con_code`(成分代码)、`weight`(权重) |
| 指数估值指标 | 大盘指数的PE/PB/换手率等估值指标 | `index_dailybasic`：`pe`、`pe_ttm`、`pb`、`turnover_rate` |
| 管理费 | 基金管理人收取的费用 | `mgt_fee`，不同ETF管理费差异较大 |

## 详细说明

### ETF基础信息（etf_basic）

`etf_basic` 接口提供国内ETF的基础信息，包含QDII类型ETF。数据来源于沪深交易所公开披露信息，单次最大返回5000条（当前ETF总数未超过2000），需要8000积分。

关键筛选维度：
- 按跟踪指数筛选：`index_code='000300.SH'` 可找到所有跟踪沪深300的ETF
- 按管理人筛选：`mgr='华夏基金'` 可找到华夏基金管理的所有ETF
- 按交易所筛选：`exchange='SH'`/`'SZ'` 区分上交所/深交所
- 按上市状态筛选：`list_status`（L上市/D退市/P待上市）

### ETF份额与规模（etf_share_size）

`etf_share_size` 接口提供ETF每日份额和规模数据，是追踪ETF资金动向的重要工具：
- **份额增长**：通常表示资金净流入，投资者看好后市
- **份额减少**：通常表示资金净流出，投资者看空或获利了结
- 同时提供净值（`nav`）和收盘价（`close`），可计算折溢价率

数据分批入库，建议每日19点后提取；涉及海外的QDII-ETF数据更新会更晚。

### 基准指数（etf_index）

`etf_index` 接口提供ETF所跟踪的基准指数列表信息，包括：
- 指数发布机构（`pub_party_name`）：如中证指数公司、上交所等
- 基日（`base_date`）和基点（`bp`）：指数的起始计算基准
- 调整周期（`adj_circle`）：成分证券的调整频率

当前约1400多个基准指数，需要8000积分。

### 指数成分与权重（index_weight）

`index_weight` 提供各类指数的成分股和权重数据，为月度更新。建议查询时输入当月第一天和最后一天作为日期范围。需要2000积分。

权重数据可用于：
- 分析指数的行业和个股集中度
- 构建指数增强策略
- 理解个股对指数涨跌的贡献度

### 指数估值指标（index_dailybasic）

`index_dailybasic` 提供主要大盘指数的每日估值指标，数据从2004年1月开始：
- **市盈率**：`pe`（静态）、`pe_ttm`（滚动12个月）
- **市净率**：`pb`
- **换手率**：`turnover_rate`（总股本）、`turnover_rate_f`（自由流通股本）
- **市值与股本**：`total_mv`、`float_mv`、`total_share`、`float_share`、`free_share`

目前覆盖上证综指、深证成指、上证50、中证500、中小板指、创业板指等核心指数。需要400积分。

## 相关主题

- [[公募基金]]
- [[K线与复权]]
- [[行业分类]]
