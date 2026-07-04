---
name: antigravity-notebooklm
description: 在 AntiGravity 连接 NotebookLM MCP。说“连接 NotebookLM”“设置 NotebookLM”时加载。
---

# 连接 NotebookLM（AntiGravity 版）

## 步骤

### 1. 安装
```powershell
uv tool install notebooklm-mcp-cli
# 若无 uv，改用:
pip install notebooklm-mcp-cli
nlm --version
```

### 2. 登录
```powershell
nlm login
```
（在浏览器中进行 Google 账号 OAuth 授权）

### 3. 验证
```powershell
# 若 Windows 有编码错误先执行：$env:PYTHONIOENCODING = "utf-8"
nlm doctor
nlm list
```

### 4. 注册 MCP
在 Anti-Gravity 的 MCP 配置文件中加入：
```json
"notebooklm": {
  "type": "local",
  "command": ["nlm", "mcp"],
  "enabled": true
}
```

⚠️ 安全提醒：不要复制 cookie/token，不把笔记本列表 commit 到 repo。
