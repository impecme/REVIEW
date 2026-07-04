# Anti-Gravity 专属懒人包 #09：服务连接与工作流程设定（自定义版）

> 版本：v1.4 (自定义版 - 已整合 01, 02, 04, 05)
> 更新日期：2026-06-02
> 语系偏好：简体中文

这份专属懒人包为您量身打造，仅包含您选择的服务：**NotebookLM、GitHub、AI生图指引、开工/收工/新项目初始化工作流**。

---

## 🚦 行前准备与环境检查

请在您的 Windows PowerShell 中执行以下命令，检查必要环境是否就绪（我们之前已帮您安装好 Node.js）：

```powershell
git --version
gh --version
node --version
python --version
```

---

## 📌 一、连接 NotebookLM (01)

### 1. 安装 CLI 工具
推荐使用 `uv` 安装（如果没有安装 `uv`，会自动降级使用 `pip`）：
```powershell
uv tool install notebooklm-mcp-cli
nlm --version
```
或者使用 `pip` 安装：
```powershell
pip install notebooklm-mcp-cli
nlm --version
```

### 2. 登录 Google 账号
执行以下命令以通过浏览器完成 OAuth 授权：
```powershell
nlm login
```

### 3. 验证连接状态
```powershell
nlm doctor
nlm list
```
> 💡 **Windows 编码提示**：如果出现 `Unicode` 或 `CP950` 编码错误，请在同一 PowerShell 窗口先执行：
> `$env:PYTHONIOENCODING = "utf-8"`

### 4. 注册至 Anti-Gravity MCP
在 Anti-Gravity 的 MCP 配置文件（通常为客户端设置或特定 JSON 配置文件）中加入以下内容：
```json
"notebooklm": {
  "type": "local",
  "command": ["nlm", "mcp"],
  "enabled": true
}
```

---

## 📌 二、连接 GitHub CLI (02)

### 1. 登录 GitHub 账号
在终端中执行：
```powershell
gh auth login --web --git-protocol https
```
按提示在浏览器中完成授权。

### 2. 验证登录状态
```powershell
gh auth status
```

### 3. 设置 Git 用户（若尚未设置）
```powershell
git config --global user.name "您的名字"
git config --global user.email "your-email@example.com"
```

---

## 📌 三、AI 生图指引 (04)

在 Anti-Gravity 中，您可以直接使用自然语言让 AI 绘制图片（走内置生图路线，无需配置 API Key）。

### 建议生图提示格式
```text
生成一张图片：
用途：[例如：网页背景 / logo / 插画]
尺寸比例：[例如：16:9 / 1:1]
主题：[例如：抗重力科技实验室]
画面内容：[例如：一个发光的反重力球体悬停在现代感实验室中央，背景有虚拟数据投影]
风格：[例如：赛博朋克 / 写实 / 极简 3D]
色彩：[例如：深蓝与霓虹绿]
限制：[例如：不要有任何文字]
输出位置：[例如：assets/anti-gravity-core.png]
```

---

## 📌 四、开工 / 收工 / 新项目初始化工作流 (05)

我们将在项目根目录使用 `ANTIGRAVITY.md` 作为 AI 工作规则入口。

### 🌅 1. 开工流程
当您对 AI 说 **“开工”** 时，AI 将自动执行：
1. 读取项目根目录的 `ANTIGRAVITY.md` 规则。
2. 读取当前的项目进度重点。
3. 执行 `git status` 检查并回顾最近的一次 commit。
4. 向您汇报当前项目状态，并给出下一步行动建议。
5. *注意：AI 不会自动进行 `pull`、`commit` 或 `push`，一切由您主控。*

### 🌌 2. 收工流程
当您对 AI 说 **“收工”** 时，AI 将自动执行：
1. 扫描项目，检查并排除敏感数据（如 API key、私人 token）。
2. 在项目笔记中记录今日完成事项、下一步计划与遇到的问题。
3. 检查 `git status` 与变更细节（diff）。
4. **精准提交**：仅 stage 本次工作相关的文档，不随意使用 `git add .`。
5. 撰写 Commit Message，在您确认后执行 commit 及 push。

### 🏗️ 3. 新项目初始化
当您说 **“新项目初始化”** 时，AI 会引导您确认项目名称、目录与 GitHub 设置，并为您建立或补齐以下基本结构：
- `ANTIGRAVITY.md`（AI 工作规则）
- `README.md`
- `.gitignore`
- Git 本地仓库

---

## 📝 项目规则模板：ANTIGRAVITY.md

请在您的项目根目录中建立此文件，作为与 AI 协作的基准：

```markdown
# <项目名称> - ANTIGRAVITY.md

## 项目入口
项目名称：
项目用途：
主要工作目录：
GitHub repo：
默认 branch：

## 工作规则
- 回应使用简体中文。
- 涉及文件操作时汇报完整产出位置。
- 使用 PowerShell 语法。
- 开工时读取本文件、检查 Git 状态。
- 收工时检查变更，确认后再提交，不纳入无关文件。
- 严禁擅自/随意删除任何项目文件。每次删除任何文件前，必须使用中文向用户提出申请并获得明确许可。
- 无论是展现思考过程、工作处理过程，还是向用户提出请求或进行询问，均必须一律使用中文。


## 安全限制
- 严禁 commit 任何 API key、密码、个人 token 或 Notebook 识别码。
- 项目代码一律储存在指定的 workspace 目录中。
```

---

## 📊 完成汇报格式

每次配置完成后，AI 将依此格式汇报：

```markdown
## Anti-Gravity 专属设置已载入
- NotebookLM 连接状态：[已启用 / 待登录 / 未启用]
- GitHub 连接状态：[已登录 / 待登录]
- 工作流状态：已就绪 (开工/收工指令已启用)
- 下一步建议：
```
