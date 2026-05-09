---
title: 行业经济-TMT行业
created: 2026-05-09
updated: 2026-05-09
type: concept
tags: [行业, TMT, 科技, 通信, 半导体]
sources: [raw/行业经济/TMT行业/]
---

# 行业经济-TMT行业

> 覆盖TMT（科技、媒体、通信）行业的细分数据接口

## 接口一览

| 接口名 | 说明 | 关键参数 |
|--------|------|----------|
| `film_record` | 获取全国电影剧本备案的公示数据 | ann_date, start_date, end_date |
| `teleplay_record` | 获取2009年以来全国拍摄制作电视剧备案公示数据 | report_date, start_date, end_date, org |
| `tmt_twincome` | 获取台湾TMT电子产业领域各类产品月度营收数据。 | date, item, start_date, end_date |
| `tmt_twincomedetail` | 获取台湾TMT行业上市公司各类产品月度营收情况。 | date, item, symbol, start_date |
| `bo_cinema` | 获取每日各影院的票房数据 | date |
| `bo_weekly` | 获取周度票房数据 | date |
| `bo_daily` | 获取电影日度票房 | date |
| `bo_monthly` | 获取电影月度票房数据 | date |

## 典型用法

```python
import tushare as ts
pro = ts.pro_api('your_token')

# 调用 film_record 接口
df = pro.film_record(ann_date="20240101", start_date="20240101", end_date="20240131")
print(df.head())
```

## 相关主题
- [[股票基础]]
- [[宏观经济-国民经济]]
- [[股票行情]]
