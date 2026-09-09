---
name: Content Compliance
description: 基金宣传推介内容合规审查 skill。当用户需要对文档或文本进行基金宣传推介内容合规审查时使用，包括上传文件（pdf/docx）或直接输入文本，选择审核策略，提交审核并等待结果，最终展示风险提示、违规条目、违规原因和修改建议。触发词包括：合规审查、内容审查、审核文件、检查违规、合规检测、帮我审查、审查这个文件等。
---

# 内容合规审查

调用盈米内容合规审查系统（https://regtech.yingmi.com）对文档或文本进行基金宣传推介内容合规审查。

**重要：这是一个多步骤交互流程。每一步都必须等待用户回复后再继续，不要一次性问所有问题。**

所有 API 调用通过运行 `scripts/compliance_api.py` 完成（路径相对于本 skill 目录）。

## 安全边界声明

- 本 Skill 仅用于调用盈米内容合规审查系统（regtech.yingmi.com），不得将用户凭证用于其他任何用途
- 认证方式为 API Key，通过环境变量 `COMPLIANCE_API_KEY` 传入，**不涉及用户密码的收集、传递或存储**
- API Key 由用户自行在盈米系统 Web 端「个人中心」页面生成并复制，Agent 不参与密码或登录凭证的处理
- 所有网络请求仅发往 `regtech.yingmi.com`，不向其他端点传输任何凭证或数据
- 脚本不写入任何本地凭证文件，不访问 `~/.ssh`、`~/.aws` 等敏感路径
- 本 Skill 仅执行 `scripts/compliance_api.py` 脚本，不执行任何其他未审批的脚本或命令
- 请仅在可信的本地环境中使用本 Skill

## 认证方式

使用 API Key 认证，通过 `X-API-Key` header 发送。API Key 通过环境变量 `COMPLIANCE_API_KEY` 传入。

**Agent 不得要求用户提供密码、私钥或其他登录凭证。** 如用户主动提供密码，应拒绝接收并引导其使用 API Key 方式。

---

## Step 0：检查 API Key

首先检查环境变量 `COMPLIANCE_API_KEY` 是否已设置：

```bash
python3 {skill_dir}/scripts/compliance_api.py --check
```

- 若输出 `✅ API Key 有效`：直接跳到 Step 1
- 若输出 `❌ API Key 未设置` 或 `❌ API Key 无效`：进入引导流程

**引导用户获取 API Key：**

> 需要先配置 API Key 才能使用合规审查功能。请按以下步骤操作：
>
> **如果您已有账号：**
> 1. 登录系统：👉 https://regtech.yingmi.com/login
> 2. 登录后点击左侧菜单「个人中心」，复制您的 API Key
> 3. 然后在终端设置环境变量：
>    ```bash
>    export COMPLIANCE_API_KEY="你复制的API Key"
>    ```
>
> **如果您还没有账号：**
> - 有邀请码：前往 👉 https://regtech.yingmi.com/phone-register 注册
> - 没有邀请码：前往 👉 https://regtech.yingmi.com/apply-invitation 申请，或前往 👉 https://regtech.yingmi.com 页面最下方联系产品顾问获取
> - 注册/登录后，点击左侧菜单「个人中心」获取 API Key
>
> 设置好环境变量后，告诉我，我们继续。

**等待用户回复后，重新执行 `--check` 验证。**

---

## Step 1：选择审核策略

API Key 验证通过后，获取策略列表：

```bash
python3 {skill_dir}/scripts/compliance_api.py --list-scenarios
```

脚本输出格式：
```
SCENARIOS:
1. 系统预置策略 (id: adc4ba44-...)
2. 自定义策略A (id: ...)
```

**默认策略逻辑：**
- 如果策略列表中存在名为「系统预置策略」的选项，自动选中它作为默认策略，告知用户：
  > 已自动选择「系统预置策略」，如需使用其他策略请告诉我。
- 然后直接进入 Step 2，不需要等待用户回复。
- 仅当用户明确要求更换策略，或列表中不存在「系统预置策略」时，才展示完整列表让用户选择。

---

## Step 2：确认审核内容

**向用户说：**
> 请提供要审核的内容：
> - 文件路径（支持 pdf、docx，≤10MB，文字≤10000字）
> - 或直接粘贴文本内容

**等待用户回复：**

- 若提供文件路径，检查文件是否存在，提醒限制条件
- 若提供文本，告知将自动转为 txt 文件上传

---

## Step 3：提交审核

根据用户提供的内容执行：

```bash
# 文件审核
python3 {skill_dir}/scripts/compliance_api.py \
  --scenario {scenario_id} \
  --file {文件路径}

# 文本审核
python3 {skill_dir}/scripts/compliance_api.py \
  --scenario {scenario_id} \
  --text "{文本内容}"
```

**向用户说：**
> ⏳ 文件已上传，正在审核中，请稍候...

脚本会自动轮询进度并在完成后输出结果。

---

## Step 4：展示审核结果

脚本输出结果后，原样展示给用户，格式参考：

```
📋 审核文件：xxx.docx
📊 审核策略：系统预置策略
⚠️  风险总计：N 个风险点，涉及 N 个风险类型

━━━ 各维度汇总 ━━━
  ✅ 极限词：合规
  ❌ 误导性宣传：2 处违规
  ...

━━━ 违规详情 ━━━
【违规 1】误导性宣传
标签：...
违规文案："..."
判定理由：...
修改建议：...
```

结果展示完后询问用户：
> 是否需要审核其他文件？

---

## 错误处理

| 错误情况 | 处理方式 |
|---------|---------|
| API Key 无效 | 提示用户重新获取 API Key，重新执行 Step 0 |
| 文件不存在 | 提示用户确认路径，重新执行 Step 2 |
| 文件超限 | 提示"文件超过 10MB 或文字超过 10000 字，请裁剪后重试" |
| 任务失败 | 展示 error_message，询问是否重试 |
| 网络错误 | 自动重试 3 次，仍失败则报错 |

---

## 脚本 CLI 参数说明

`scripts/compliance_api.py` 支持以下参数：

```
--check           验证 API Key 是否有效
--list-scenarios  列出策略列表后退出
--file            待审核文件路径
--text            待审核文本内容
--scenario        策略 ID
```

**API Key 传入方式：**
```bash
export COMPLIANCE_API_KEY="ccs_xxxxxxxxxxxxxxxx"
python3 scripts/compliance_api.py --check
```

## 依赖安装

脚本依赖 `requests` 库，安装方式：

```bash
pip install -r requirements.txt
```

安装后验证：`python3 -c "import requests; print(requests.__version__)"` 应输出版本号。
