# content-compliance-dist

基金宣传推介内容合规审查的分发包，用于对接盈米内容合规审查系统（[regtech.yingmi.com](https://regtech.yingmi.com)），对文档或文本进行合规审核并展示风险与修改建议。

## 功能概览

- **文件审核**：支持 PDF、DOCX，单文件 ≤10MB，文字 ≤10000 字
- **文本审核**：直接传入文本内容，自动按 txt 形式提交
- **策略选择**：使用系统预置或自定义审核策略（场景）
- **结果展示**：各维度合规/违规汇总、违规详情、修改建议

本仓库包含：

- `scripts/compliance_api.py`：合规审查 API 的 CLI 封装（API Key 认证）
- `SKILL.md`：供 Cursor Agent 使用的内容合规审查 Skill 定义
- `requirements.txt`：Python 依赖

## 前置条件

- Python 3.7+
- 盈米内容合规审查系统账号，并已获取 **API Key**（登录 [regtech.yingmi.com](https://regtech.yingmi.com) → 个人中心）

## 安装

```bash
cd content-compliance-dist
pip install -r requirements.txt
```

依赖：`requests>=2.28.0,<3`。

## 配置

通过环境变量传入 API Key：

```bash
export COMPLIANCE_API_KEY="你的API Key"
```

（可选）自定义 API 基地址，默认 `https://regtech.yingmi.com/api`：

```bash
export COMPLIANCE_BASE_URL="https://regtech.yingmi.com/api"
```

## 使用方式

### 方式一：作为 Cursor Skill 使用

将本目录配置为 Cursor 的 Agent Skill，通过自然语言触发「合规审查、内容审查、审核文件」等，由 Agent 按 SKILL.md 流程调用 `scripts/compliance_api.py` 完成上传、轮询与结果展示。详见 [SKILL.md](./SKILL.md)。

### 方式二：直接使用 CLI

**1. 校验 API Key**

```bash
python3 scripts/compliance_api.py --check
```

**2. 查看可用策略**

```bash
python3 scripts/compliance_api.py --list-scenarios
```

**3. 提交审核**

```bash
# 按文件
python3 scripts/compliance_api.py --scenario <策略ID> --file /path/to/file.pdf

# 按文本
python3 scripts/compliance_api.py --scenario <策略ID> --text "待审核的文本内容"
```

脚本会轮询任务状态并在完成后输出各维度汇总与违规详情。

## CLI 参数说明

| 参数 | 说明 |
|------|------|
| `--check` | 验证当前环境中的 API Key 是否有效 |
| `--list-scenarios` | 列出所有可用策略（名称与 id） |
| `--scenario` | 策略 ID（必填，提交审核时） |
| `--file` | 待审核文件路径（pdf/docx） |
| `--text` | 待审核文本内容（与 `--file` 二选一） |

## 安全与合规

- 认证仅使用 API Key（环境变量 `COMPLIANCE_API_KEY`），不涉及用户密码或其它登录凭证。
- 请求仅发往盈米合规系统（regtech.yingmi.com），脚本不写入本地凭证、不访问敏感路径。
- 安全漏洞报送方式、响应承诺与披露策略见 [SECURITY.md](./SECURITY.md)。

## 许可证

[MIT License](./LICENSE.txt)
