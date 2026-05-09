---
title: 对比AH股价差
created: 2026-05-09
updated: 2026-05-09
type: query
tags: [stock, hk]
sources: []
---

# 对比AH股价差

> **问题**：怎么对比AH股价差？

## 回答

使用 `stk_ah_comparison` 获取 AH 股比价数据，配合 `ccass_hold`（CCASS 持仓数据）进行综合分析。

### stk_ah_comparison — AH 股比价

获取同时在 A 股和 H 股上市的公司的比价数据。

```python
import tushare as ts
pro = ts.pro_api('your_token')

# 获取某日 AH 股比价数据
df = pro.stk_ah_comparison(trade_date='20240115')

# 查询某只股票的 AH 比价历史
df = pro.stk_ah_comparison(ts_code='601318.SH', start_date='20240101', end_date='20240131')
```

### ccass_hold — CCASS 持仓数据

获取港股中央结算系统（CCASS）的持股数据，追踪港股通资金对 H 股的持仓变化。

```python
# 某股票 CCASS 持仓
df = pro.ccass_hold(ts_code='601318.HK', start_date='20240101', end_date='20240131')
```

### 关键字段说明

**stk_ah_comparison 输出**：
- **a_close / h_close**：A 股 / H 股收盘价
- **a_h_ratio**：AH 股价比（A 股价格 / H 股价格，需考虑汇率）
- **h_a_ratio**：H/A 比价
- 当 a_h_ratio > 1 时 A 股溢价，< 1 时 A 股折价

### 分析要点

1. **AH 溢价指数**：多数情况下 A 股相对 H 股有溢价（比值 > 1）
2. **套利机会**：当溢价极端偏离历史均值时，可能存在均值回归机会
3. **资金流向**：结合 CCASS 持仓变动判断南下资金动向

### 组合查询示例

```python
# 获取 AH 比价数据
ah = pro.stk_ah_comparison(trade_date='20240115')

# 筛选 A 股大幅溢价的个股
overpriced = ah[ah['a_h_ratio'] > 2.0]

# 进一步查看 CCASS 持仓变化
for _, row in overpriced.iterrows():
    hold = pro.ccass_hold(ts_code=row['ts_code_hk'], trade_date='20240115')
    print(row['ts_code'], row['a_h_ratio'], hold)
```

## 相关主题
- [[股票特色数据]]
- [[股票资金流向]]
