---
title: AI Stage Gate 决策机制（来源摘要）
type: source
tags: [AI共创, Stage Gate, 决策, POC, MVP, Pilot]
sources: [AI共创/03《AI Stage Gate 决策机制 V1.0》.md]
created: 2026-08-17
updated: 2026-08-17
---

# AI Stage Gate 决策机制 — 来源摘要

> 本页是 `raw/AI共创/03《AI Stage Gate 决策机制 V1.0》.md` 的摘要页。原件不可修改，一切主张以原件为准。

## 这份来源讲什么

「AI共创工作体系」**模板 03**，整个体系的**决策中枢**：为 AI 共创项目提供从发现机会到规模化的阶段性决策机制。避免在没有验证业务价值或 AI 可行性的情况下持续投入资源。

## 关键内容一览

- **五道 Gate 判定标准**：

| Gate | 核心问题 | 关键证据 | 决策 |
|---|---|---|---|
| Gate 0 | 值不值得做？ | Scenario + Score | GO / HOLD / KILL |
| Gate 1 | AI 能不能做？ | POC Result | GO / ITERATE / KILL |
| Gate 2 | 能不能用？ | MVP | GO / ITERATE / KILL |
| Gate 3 | 有没有价值？ | Pilot Data | SCALE / ITERATE / STOP |
| Gate 4 | 能否复制？ | Scale Data | ASSET / SCALE MORE / RETIRE |

- **Gate 0**：进入前须完成场景发现、业务访谈、流程梳理、痛点识别、价值假设、优先级评分；必答 5 问；输出 AI Scenario Decision Card。
- **Gate 1**：POC 验证 4 块——AI 能力、**输出质量（必须先定义"什么叫可用"：RAG 看检索准确率/Recall/来源正确率，生成看内容准确率/完整性/可读性，Agent 看 Task Completion Rate）**、性能、成本。
- **Gate 2**：MVP = 完成一个最小但完整的业务闭环（用户输入→AI 处理→AI 输出→人工修改→业务交付），验收看产品/AI/用户三类指标。
- **Gate 3（全体系最重要的一道 Gate）**：Pilot 验证四类指标——Adoption / Efficiency / Quality / Business Impact，**四项同时判断**才能进入 Scale。
- **Gate 4**：核心问题从"项目做完了吗"变为"AI 能力能不能成为公司组织能力"，验证技术/数据/组织/治理四块。
- **三条决策原则**：没有证据不进入下一阶段；失败也是正常结果；投入逐阶段增加、越往后证据要求越高。
- **决策会议 7 问**：Hypothesis → Evidence → Result → Validated → Invalidated → Investment → Decision。
- **One-page 单页治理**：每项目只维护一页（BUSINESS / EVIDENCE / RISK / DECISION 四块）。

## 涉及的核心概念

- [[AI共创模板体系]] — 模板 03 在体系中的位置
- [[AI共创核心工作流（整合）]]

## 相关来源

- [[AI场景发现与业务访谈表]]、[[AI场景优先级评分表]] — Gate 0 的前置输入
- [[AI POC验证方案]]、[[AI MVP方案]]、[[AI Pilot试点方案]]、[[AI Adoption方案]]、[[AI能力资产沉淀表]] — 各 Gate 对应的执行模板
