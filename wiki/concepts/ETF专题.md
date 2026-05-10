---
title: ETF专题
created: 2026-05-09
updated: 2026-05-10
type: concept
tags: [etf, quote]
sources: [references/ETF专题/]
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

## 接口详细参数

### `etf_share_size` 详细说明

**调用说明**: 需要8000积分可调取；单次最大5000条，可根据代码或日期循环提取
**数据说明**: 建议每日19点后提取；涉及海外ETF数据更新会晚一些

**输入参数**

| 名称 | 类型 | 必选 | 描述 |
|------|------|------|------|
| ts_code | str | N | 基金代码（可从ETF基础信息接口提取） |
| trade_date | str | N | 交易日期（YYYYMMDD格式，下同） |
| start_date | str | N | 开始日期 |
| end_date | str | N | 结束日期 |
| exchange | str | N | 交易所（SSE上交所 SZSE深交所） |

**输出参数**

| 名称 | 类型 | 描述 |
|------|------|------|
| trade_date | str | 交易日期 |
| ts_code | str | ETF代码 |
| etf_name | str | 基金名称 |
| total_share | float | 总份额（万份） |
| total_size | float | 总规模（万元） |
| nav | float | 基金份额净值(元) |
| close | float | 收盘价（元） |
| exchange | str | 交易所（SSE上交所 SZSE深交所 BSE北交所） |

---

### `stk_mins` 详细说明

**调用说明**: 需正式权限；单次最大8000行数据，可通过股票代码和时间循环获取；提供超过10年ETF历史分钟数据
**数据说明**: 支持1min/5min/15min/30min/60min行情

**输入参数**

| 名称 | 类型 | 必选 | 描述 |
|------|------|------|------|
| ts_code | str | Y | ETF代码，e.g. 159001.SZ |
| freq | str | Y | 分钟频度（1min/5min/15min/30min/60min） |
| start_date | datetime | N | 开始日期 格式：2025-06-01 09:00:00 |
| end_date | datetime | N | 结束时间 格式：2025-06-20 19:00:00 |

**输出参数**

| 名称 | 类型 | 描述 |
|------|------|------|
| ts_code | str | ETF代码 |
| trade_time | str | 交易时间 |
| open | float | 开盘价 |
| close | float | 收盘价 |
| high | float | 最高价 |
| low | float | 最低价 |
| vol | int | 成交量（股） |
| amount | float | 成交金额（元） |

---

### `etf_index` 详细说明

**调用说明**: 用户积累8000积分可调取；单次请求最大返回5000行数据
**数据说明**: 当前未超过2000条记录

**输入参数**

| 名称 | 类型 | 必选 | 描述 |
|------|------|------|------|
| ts_code | str | N | 指数代码 |
| pub_date | str | N | 发布日期（格式：YYYYMMDD） |
| base_date | str | N | 指数基期（格式：YYYYMMDD） |

**输出参数**

| 名称 | 类型 | 描述 |
|------|------|------|
| ts_code | str | 指数代码 |
| indx_name | str | 指数全称 |
| indx_csname | str | 指数简称 |
| pub_party_name | str | 指数发布机构 |
| pub_date | str | 指数发布日期 |
| base_date | str | 指数基日 |
| bp | float | 指数基点(点) |
| adj_circle | str | 指数成份证券调整周期 |

---

### `etf_basic` 详细说明

**调用说明**: 用户积8000积分可调取；单次请求最大返回5000条数据（当前ETF总数未超过2000）
**数据说明**: 数据来源与沪深交易所公开披露信息；包括QDII

**输入参数**

| 名称 | 类型 | 必选 | 描述 |
|------|------|------|------|
| ts_code | str | N | ETF代码（带.SZ/.SH后缀的6位数字，如：159526.SZ） |
| index_code | str | N | 跟踪指数代码 |
| list_date | str | N | 上市日期（格式：YYYYMMDD） |
| list_status | str | N | 上市状态（L上市 D退市 P待上市） |
| exchange | str | N | 交易所（SH上交所 SZ深交所） |
| mgr | str | N | 管理人（简称，e.g.华夏基金） |

**输出参数**

| 名称 | 类型 | 描述 |
|------|------|------|
| ts_code | str | 基金交易代码 |
| csname | str | ETF中文简称 |
| extname | str | ETF扩位简称(对应交易所简称) |
| cname | str | 基金中文全称 |
| index_code | str | ETF基准指数代码 |
| index_name | str | ETF基准指数中文全称 |
| setup_date | str | 设立日期（格式：YYYYMMDD） |
| list_date | str | 上市日期（格式：YYYYMMDD） |
| list_status | str | 存续状态（L上市 D退市 P待上市） |
| exchange | str | 交易所（上交所SH 深交所SZ） |
| mgr_name | str | 基金管理人简称 |
| custod_name | str | 基金托管人名称 |
| mgt_fee | float | 基金管理人收取的费用 |
| etf_type | str | 基金投资通道类型（境内、QDII） |

---

### `fund_adj` 详细说明

**调用说明**: 用户积600积分可调取，超过5000积分以上频次相对较高；单次最大提取2000行记录，可循环提取，数据总量不限制
**数据说明**: 用于计算基金复权行情

**输入参数**

| 名称 | 类型 | 必选 | 描述 |
|------|------|------|------|
| ts_code | str | N | TS基金代码（支持多只基金输入） |
| trade_date | str | N | 交易日期（格式：yyyymmdd，下同） |
| start_date | str | N | 开始日期 |
| end_date | str | N | 结束日期 |
| offset | str | N | 开始行数 |
| limit | str | N | 最大行数 |

**输出参数**

| 名称 | 类型 | 描述 |
|------|------|------|
| ts_code | str | ts基金代码 |
| trade_date | str | 交易日期 |
| adj_factor | float | 复权因子 |

---

### `rt_min` 详细说明

**调用说明**: 需正式权限；单次最大1000行数据，支持逗号分隔的多个代码同时提取
**数据说明**: 包括1~60min实时分钟数据

**输入参数**

| 名称 | 类型 | 必选 | 描述 |
|------|------|------|------|
| freq | str | Y | 1MIN,5MIN,15MIN,30MIN,60MIN（大写） |
| ts_code | str | Y | 支持单个和多个：589960.SH 或者 589960.SH,159100.SZ |

**输出参数**

| 名称 | 类型 | 描述 |
|------|------|------|
| ts_code | str | 股票代码 |
| time | None | 交易时间 |
| open | float | 开盘价 |
| close | float | 收盘价 |
| high | float | 最高价 |
| low | float | 最低价 |
| vol | float | 成交量(股) |
| amount | float | 成交额（元） |

---

### `rt_etf_k` 详细说明

**调用说明**: 单独开权限的数据，单独申请权限
**数据说明**: 获取ETF实时日k线行情，支持通配符方式一次性提取全部ETF

**输入参数**

| 名称 | 类型 | 必选 | 描述 |
|------|------|------|------|
| ts_code | str | Y | 支持通配符方式，e.g. 5\*.SH、15\*.SZ、159101.SZ |
| topic | str | Y | 分类参数，取上海ETF时需输入'HQ_FND_TICK' |

**输出参数**

| 名称 | 类型 | 描述 |
|------|------|------|
| ts_code | str | ETF代码 |
| name | None | ETF名称 |
| pre_close | float | 昨收价 |
| high | float | 最高价 |
| open | float | 开盘价 |
| low | float | 最低价 |
| close | float | 收盘价（最新价） |
| vol | int | 成交量（股） |
| amount | int | 成交金额（元） |
| num | int | 开盘以来成交笔数 |
| ask_volume1 | int | 委托卖盘（股） |
| bid_volume1 | int | 委托买盘（股） |
| trade_time | str | 交易时间 |

---

### `fund_daily` 详细说明

**调用说明**: 需要至少5000积分才可以调取，8000积分频次更高；单次最大5000行记录，可以根据ETF代码和日期循环获取历史，总量不限制
**数据说明**: 历史超过10年

**输入参数**

| 名称 | 类型 | 必选 | 描述 |
|------|------|------|------|
| ts_code | str | N | 基金代码 |
| trade_date | str | N | 交易日期(YYYYMMDD格式，下同) |
| start_date | str | N | 开始日期 |
| end_date | str | N | 结束日期 |

**输出参数**

| 名称 | 类型 | 描述 |
|------|------|------|
| ts_code | str | TS代码 |
| trade_date | str | 交易日期 |
| open | float | 开盘价(元) |
| high | float | 最高价(元) |
| low | float | 最低价(元) |
| close | float | 收盘价(元) |
| pre_close | float | 昨收盘价(元) |
| change | float | 涨跌额(元) |
| pct_chg | float | 涨跌幅(%) |
| vol | float | 成交量(手) |
| amount | float | 成交额(千元) |

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
