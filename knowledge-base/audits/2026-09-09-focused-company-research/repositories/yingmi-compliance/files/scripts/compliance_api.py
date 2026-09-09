#!/usr/bin/env python3
"""
盈米内容合规审查 API 封装 - API Key 认证版
"""
import os, sys, time, tempfile, requests

BASE_URL = os.environ.get("COMPLIANCE_BASE_URL", "https://regtech.yingmi.com/api")

def get_api_key():
    return os.environ.get("COMPLIANCE_API_KEY")

def get_auth_headers():
    api_key = get_api_key()
    if not api_key:
        print("API Key 未设置，请先设置环境变量 COMPLIANCE_API_KEY")
        sys.exit(1)
    return {"X-API-Key": api_key}

def check_api_key():
    api_key = get_api_key()
    if not api_key:
        print("API Key 未设置")
        return False
    try:
        resp = requests.get(f"{BASE_URL}/scenarios", headers={"X-API-Key": api_key}, timeout=10)
        if resp.status_code == 200:
            print("API Key 有效")
            return True
        elif resp.status_code == 401:
            print("API Key 无效")
            return False
        else:
            print(f"验证失败，状态码：{resp.status_code}")
            return False
    except Exception as e:
        print(f"网络错误：{e}")
        return False

def get_scenarios():
    resp = requests.get(f"{BASE_URL}/scenarios", headers=get_auth_headers(), timeout=15)
    resp.raise_for_status()
    data = resp.json()
    return data if isinstance(data, list) else data.get("items", data.get("scenarios", []))

def upload_file(file_path, scenario_id):
    file_path = os.path.expanduser(file_path)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件不存在：{file_path}")
    if os.path.getsize(file_path) / 1024 / 1024 > 10:
        raise ValueError("文件超过 10MB 限制")
    with open(file_path, "rb") as f:
        resp = requests.post(f"{BASE_URL}/documents/upload", headers=get_auth_headers(),
                             files={"file": (os.path.basename(file_path), f)},
                             data={"scenario_id": scenario_id}, timeout=60)
    resp.raise_for_status()
    data = resp.json()
    return data["document_id"], data["task_id"]

def upload_text(text, scenario_id):
    if len(text) > 10000:
        raise ValueError(f"文本长度 {len(text)} 字超过 10000 字限制")
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", encoding="utf-8", delete=False) as tmp:
        tmp.write(text)
        tmp_path = tmp.name
    try:
        return upload_file(tmp_path, scenario_id)
    finally:
        os.unlink(tmp_path)

def poll_task(task_id, timeout=300, interval=3):
    headers = get_auth_headers()
    deadline = time.time() + timeout
    last_progress = -1
    while time.time() < deadline:
        resp = requests.get(f"{BASE_URL}/documents/tasks/{task_id}", headers=headers, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        status, progress = data.get("status", ""), data.get("progress", 0)
        if progress != last_progress:
            print(f"  审核进度：{progress}%  [{status}]")
            last_progress = progress
        if status == "completed":
            return data
        if status == "failed":
            raise RuntimeError(f"审核任务失败：{data.get('error_message', '未知错误')}")
        time.sleep(interval)
    raise TimeoutError(f"审核超时（{timeout}s），task_id={task_id}")

def get_results(task_id):
    resp = requests.get(f"{BASE_URL}/documents/tasks/{task_id}/results", headers=get_auth_headers(), timeout=15)
    resp.raise_for_status()
    return resp.json()

def format_results(data):
    lines = []
    lines.append(f"审核文件：{data.get('document_filename', '-')}")
    lines.append(f"审核策略：{data.get('scenario_name', '-')}")
    lines.append(f"风险总计：{data.get('total_issues', 0)} 个问题，涉及 {data.get('total_results', 0)} 个审核维度")
    lines.append("\n--- 各维度汇总 ---")
    issues_by_wf = data.get("issues_by_workflow", {})
    for result in data.get("results", []):
        wf = result.get("workflow_name", "")
        if result.get("is_compliant"):
            lines.append(f"  [合规] {wf}")
        else:
            cnt = issues_by_wf.get(wf, len(result.get("issues", [])))
            lines.append(f"  [违规] {wf}：{cnt} 处")
    violation_num = 0
    lines.append("\n--- 违规详情 ---")
    for result in data.get("results", []):
        if result.get("is_compliant"):
            continue
        wf = result.get("workflow_name", "")
        for issue in result.get("issues", []):
            violation_num += 1
            lines.append(f"\n[违规 {violation_num}] {wf}")
            lines.append(f"标签：{', '.join(issue.get('tags', []))}")
            lines.append(f"违规文本：\"{issue.get('text', '')}\"")
            reason = issue.get("reason", "")
            lines.append(f"原因：{reason[:200]}{'...' if len(reason) > 200 else ''}")
            if issue.get("suggestion"):
                lines.append(f"建议：{issue['suggestion']}")
    if violation_num == 0:
        lines.append("  未发现违规内容")
    return "\n".join(lines)

def main():
    import argparse
    parser = argparse.ArgumentParser(description="内容合规审查 CLI")
    parser.add_argument("--check", action="store_true", help="验证 API Key 是否有效")
    parser.add_argument("--list-scenarios", action="store_true", help="列出策略列表")
    parser.add_argument("--file", help="待审核文件路径")
    parser.add_argument("--text", help="待审核文本内容")
    parser.add_argument("--scenario", help="策略 ID")
    args = parser.parse_args()
    if args.check:
        sys.exit(0 if check_api_key() else 1)
    scenarios = get_scenarios()
    if args.list_scenarios:
        print("\nSCENARIOS:")
        for i, s in enumerate(scenarios, 1):
            print(f"  {i}. {s.get('name', '')} (id: {s['id']})")
        sys.exit(0)
    scenario_id = args.scenario
    if not scenario_id:
        print("错误：必须通过 --scenario 指定策略 ID")
        print("可用策略：")
        for i, s in enumerate(scenarios, 1):
            print(f"  {i}. {s.get('name', '')}  (id: {s['id']})")
        sys.exit(1)
    print(f"使用策略：{scenario_id}")
    if args.file:
        _, task_id = upload_file(args.file, scenario_id)
    elif args.text:
        _, task_id = upload_text(args.text, scenario_id)
    else:
        print("请提供 --file 或 --text")
        sys.exit(1)
    print(f"上传成功，task_id={task_id}")
    print("\n等待审核完成...")
    poll_task(task_id)
    results = get_results(task_id)
    print("\n" + "=" * 60)
    print(format_results(results))

if __name__ == "__main__":
    main()
