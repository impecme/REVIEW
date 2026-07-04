---
name: antigravity-workflow
description: AntiGravity 开工/收工/新项目初始化流程。说“开工”“收工”“初始化项目”时加载。
---

# 开工 / 收工 / 新项目初始化

## 开工
1. 读取项目根目录的 `ANTIGRAVITY.md`。
2. 读取项目进度重点。
3. 执行 `git status` 与最近的 commit 状态。
4. 向用户汇报当前状态，并给出下一步行动建议。
5. *不自动进行 pull/commit/push。*

## 收工
1. 检查敏感数据（API key、token、私人密码等）。
2. 在项目笔记中记录完成事项、下一步工作计划及待解决的问题。
3. 仅在规则或路径有变更时才更新 `ANTIGRAVITY.md`。
4. 检查 `git status` 及 diff。
5. **精准提交**：仅 stage 与本次工作相关的文档（不使用无差别的 `git add .`）。
6. 确认后 commit 及 push。
