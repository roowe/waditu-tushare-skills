---
title: ETF专题
created: 2026-05-09
updated: 2026-05-09
type: concept
tags: [ETF, 基金, 行情, 分钟线, 复权]
sources: [raw/ETF专题/]
---

# ETF专题

> 覆盖ETF基金的基础信息、行情数据（日线/分钟线）、份额规模、复权因子、基准指数等全链路数据接口

## 接口一览

| 接口名 | 说明 | 关键参数 |
|--------|------|----------|
| `etf_share_size` | 获取沪深ETF每日份额和规模数据，能体现规模份额的变化，掌握ETF资金动向，同时提供每日净值和收盘价；数据指标是分批入库，建议在每日19点后提取；另外，涉及海外的ETF数据更新会晚一些属于正常情况。 | ts_code, trade_date, start_date, end_date |
| `stk_mins` | 获取ETF分钟数据，支持1min/5min/15min/30min/60min行情，提供Python SDK和 http Restful API两种方式 | ts_code, freq, start_date, end_date |
| `etf_index` | 获取ETF基准指数列表信息 | ts_code, pub_date, base_date |
| `etf_basic` | 获取国内ETF基础信息，包括了QDII。数据来源与沪深交易所公开披露信息。 | ts_code, index_code, list_date, list_status |
| `fund_adj` | 获取基金复权因子，用于计算基金复权行情 | ts_code, trade_date, start_date, end_date |
| `rt_min` | 获取ETF实时分钟数据，包括1~60min | freq, ts_code |
| `rt_etf_k` | 获取ETF实时日k线行情，支持按ETF代码或代码通配符一次性提取全部ETF实时日k线行情 | ts_code, topic |
| `fund_daily` | 获取ETF行情每日收盘后成交数据，历史超过10年 | ts_code, trade_date, start_date, end_date |

## 典型用法

```python
import tushare as ts
pro = ts.pro_api('your_token')

# 调用 etf_share_size 接口
df = pro.etf_share_size(ts_code="159919.SZ", trade_date="20240101", start_date="20240101")
print(df.head())
```

## 相关主题
- [[公募基金]]
- [[指数专题]]
- [[股票行情]]
