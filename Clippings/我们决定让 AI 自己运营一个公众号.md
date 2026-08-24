---
title: "我们决定让 AI 自己运营一个公众号"
source: "https://mp.weixin.qq.com/s/wz8X73-JmKlgcZfoyJxT6Q"
author:
  - "[[AI探索者]]"
published:
created: 2026-08-24
description: "不聊 AI，搞点真的。我们把一个真实的 AI 实践交给 AI，让它自己走完「采访→选题→写作→配图→审核建议→传播→复盘」的完整链路。这是第一篇记录，也是第一个实验案例。"
tags:
  - "clippings"
---
AI探索者 AI搞事儿 *2026年8月24日 12:01*

不聊 AI，搞点真的。

这篇文章本身就是一次实验。我们把“AI 搞事儿”交给 AI 自己运营，人只负责四件事： **事实、敏感信息、人物授权、最终发布** 。

## 为什么做这件事

公司里用 AI 的人不少，但大多数实践做完就完了——没人记录、没人分享、没人复盘。我们想做一个企业内部的 AI 实践社区，把这些真实发生的事记下来。

问题来了： **谁来记？** 业务同学没时间也不擅长，专人运营现阶段投入不起。

不如让 AI 自己试试。

## 整体规划

“AI 搞事儿”定位为企业 AI 共创成果实践社区。核心是一个飞轮：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3AzxEqHPwRs2nbf6shbwxUtYR6fQa9GfAYwtGsTyCKrhqZvn6mRE5AcFIWEqFRkciaWAORxavkicZyn0WfJlUOrCydMlrLqiaw6uiahSIOYevSg/640?from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

内容围绕五大栏目：

- • **搞事现场** ：真实案例
- • **搞事的人** ：AI 玩家故事
- • **搞砸了** ：失败复盘
- • **AI 怎么干** ：方法与过程
- • **本周搞事儿** ：周报与成绩单

## 我们给 AI 配置了什么

一套完整的公众号内容生产工具链，共 5 个 Skill：

| Skill | 干什么 |
| --- | --- |
| format-markdown | 整理结构化 Markdown |
| cover-image | 生成公众号封面 |
| article-illustrator | 生成正文插图 |
| post-to-wechat | 排版并 API 发布 |
| image-gen | 图片生成后端（gpt-image-2） |

![图片](https://mmbiz.qpic.cn/mmbiz_png/3AzxEqHPwRtssKyaLyaTcylKCJclg9zJPUibIT5iacicunEvM21xzOtCPib8EeoW3LxzBEcATsfZyXNQVpGR1gwwOEgdic0ic5LQ925iayeSCfMib1k/640?from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

> AI 负责把事做出来，人负责把事情做对。

## AI 现在能做什么

实测两轮，AI 能稳定完成：文章格式化、封面生成、正文插图、微信排版、API 发布。过程 AI 独立完成，人工不干预内容。

## AI 目前不会做什么

- • 不会采访——只能基于已有素材工作
- • 不会判断事实真伪
- • 不识别敏感信息
- • 不会最终发布
- • 封面文字渲染不稳定

## 第一轮遇到的问题

如实记录：Windows 兼容性 bug、发布脚本 npx 通道问题、API key 给错过、并发图片生成崩溃、封面风格跑偏一次。

都不是大事，但很真实。 **这个差距，正是实验最有价值的部分。**

## 哪些环节仍然需要人

| 环节 | 谁负责 |
| --- | --- |
| 提供真实素材、回答追问 | 共创官 |
| 事实核查、敏感信息排查 | 内容审核人 |
| 最终发布 | 内容审核人 |
| 复盘决策 | 小组负责人 |

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3AzxEqHPwRuqEia4fWqrHwyf2uQcLiavvm4GE3kGGbNs8QVLzjSib4gOJrzQ3LjDxibCdBlEEBPA8cj0nZjdiaBmSUO0j9eibI2G0UnZQkHBflib1Y/640?from=appmsg&watermark=1#imgIndex=2)

## 接下来 7 天怎么测试

| 天数 | 任务 |
| --- | --- |
| Day 1-3 | 素材整理、采访、选题、写作、配图 |
| Day 4 | 人工审核 |
| Day 5 | 人工发布、内部传播 |
| Day 6 | 收集数据 |
| Day 7 | AI 复盘，提出改进建议 |

7 天后只看四个问题：AI 独立完成了多少？哪些环节做不了？人工投入多少时间？下一版 Skill 改什么？

## 最后

不追求粉丝量，不追求阅读量，不搞复杂积分体系。

只想知道一件事： **AI 能不能参与运营一个真实的企业 AI 实践社区。**

跑通了，逐步加自动化；跑不通，失败记录本身就是一篇好文章。

反正，不聊 AI，搞点真的。

---

*本文由 AI 协作完成，人负责事实与审核。*