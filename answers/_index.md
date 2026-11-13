---
title: 话题答案索引
type: overview
tags: [topic-cache, index]
---

# 话题答案索引

> 本目录独立于 `raw/` 与 `wiki/`，不纳入 AGENTS.md 的 ingest 流程。
> 由 `xhs-topic-answer/scripts/cache.py save` 自动维护，请勿手工重排。

| 话题 | 落盘时间 | 到期 | 状态 | 文件 |
|---|---|---|---|---|
| [[抖音男装性价比好店top10推荐]] | 2026-11-12 | 2027-05-12 | 有效 | `抖音男装性价比好店top10推荐.md` |
| [[最火的十部动漫]] | 2026-11-11 | 2027-05-11 | 有效 | `最火的十部动漫.md` |

## 规则

- 问「帮我查看 X」→ 先 `cache.py lookup "X"`。
- `FRESH` → 直接给本地结果 + 落盘时间，不联网。
- `STALE`（超过 6 个月）→ 重新抓小红书，旧版进 `_archive/`，不覆盖。
- `MANUAL`（自己手写的文件）→ 直接给结果，不自动刷新覆盖。
