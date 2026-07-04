---
name: antigravity-github
description: 在 AntiGravity 连接 GitHub CLI。说“连接 GitHub”“设置 GitHub”时加载。
---

# 连接 GitHub（AntiGravity 版）

## 步骤

### 1. 检查状态
```powershell
gh auth status
```

### 2. 登录
```powershell
gh auth login --web --git-protocol https
```

### 3. 设置 Git 全局用户
```powershell
git config --global user.name "你的名字"
git config --global user.email "your-email@example.com"
```

⚠️ 安全提醒：不把 GitHub 访问 Token 写入 Markdown 或任何代码库中。
