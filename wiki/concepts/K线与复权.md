---
title: K线与复权
created: 2026-05-09
updated: 2026-05-09
type: concept
tags: [stock, quote, historical]
sources:
  - raw/股票数据/行情数据/通用行情接口.md
  - raw/股票数据/特色数据/股票技术面因子(专业版).md
---
# K线与复权
> 股票价格的基本记录方式（OHLCV）及消除分红送股影响的价格调整机制。

## 核心概念

| 概念 | 英文 | 说明 | 相关接口/字段 |
|---|---|---|---|
| OHLCV | Open/High/Low/Close/Volume | K线五要素：开盘价/最高价/最低价/收盘价/成交量 | `open`、`high`、`low`、`close`、`vol` |
| K线周期 | Bar Period | 支持1/5/15/30/60分钟、日(D)/周(W)/月(M) | `pro_bar(freq='D')`，分钟需600+积分 |
| 前复权 | Forward Adjusted (qfq) | 以最新价为基准向前调整历史价格，保证最新价不变，历史价可连续比较 | `adj='qfq'` 或字段后缀 `_qfq` |
| 后复权 | Backward Adjusted (hfq) | 以最早价为基准向后调整，保证最早价不变，反映真实收益 | `adj='hfq'` 或字段后缀 `_hfq` |
| 不复权 | No Adjust (bfq) | 原始交易价格，不做任何复权处理 | `adj=None` 或字段后缀 `_bfq` |
| 复权因子 | Adjustment Factor | 将原始价格转为复权价格的乘数因子，分红再投模式 | `adj_factor` |
| 通用行情接口 | pro_bar | 集成行情接口，整合股票/指数/基金/期货/期权/可转债等多资产行情 | `ts.pro_bar()` |

## 详细说明

### 复权机制

分红送股会导致K线出现跳空缺口，复权用于消除此影响，使价格序列连续可比：
- **前复权 (qfq)**：最新价不变，历史价格按复权因子向下调整。适合观察长期走势和技术分析。
- **后复权 (hfq)**：最早价不变，后续价格按复权因子向上调整。适合计算真实收益率。
- **不复权 (bfq)**：保留原始交易价格。适合查看真实历史成交情况。

复权因子 `adj_factor` 的关系：`复权价 = 原始价 * adj_factor`

> 注意：`pro_bar` 目前只支持日线复权，复权机制根据 `end_date` 参数动态计算。

### pro_bar 接口详解

`pro_bar` 是 Tushare 的集成开发接口，支持多种资产类型：

| asset 参数 | 说明 |
|---|---|
| `E` | 股票（默认） |
| `I` | 沪深指数 |
| `C` | 数字货币 |
| `FT` | 期货 |
| `FD` | 基金 |
| `O` | 期权 |
| `CB` | 可转债 |

**接口调用示例**：
```python
# 前复权日线
df = ts.pro_bar(ts_code='000001.SZ', adj='qfq', start_date='20180101', end_date='20181011')

# 上证指数行情
df = ts.pro_bar(ts_code='000001.SH', asset='I', start_date='20180101', end_date='20181011')

# 带均线（动态计算）
df = ts.pro_bar(ts_code='000001.SZ', start_date='20180101', end_date='20181011', ma=[5, 20, 50])

# 带换手率(tor)、量比(vr)
df = ts.pro_bar(ts_code='000001.SZ', start_date='20180101', end_date='20181011', factors=['tor', 'vr'])
```

### stk_factor_pro 中的复权字段

`stk_factor_pro` 接口对 OHLCV 和所有技术指标均提供三种复权版本，字段命名规则为 `指标名_复权类型`，如 `close_qfq`（前复权收盘价）、`macd_dif_hfq`（后复权MACD-DIF）。

> 注意：`pre_close` 字段为前复权昨收价，由 daily 接口的 pre_close 以当时复权因子计算，可能跟前一日的 `close_qfq` 不完全对应。

## 相关主题
- [[趋势类指标]]
- [[震荡动量类指标]]
- [[市场微观结构]]
- [[ETF与指数投资]]
