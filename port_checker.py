import subprocess
import json
import psutil
from languages import get_text

def get_process_name(pid):
    try:
        return psutil.Process(pid).name()
    except:
        return get_text("unknown_process")  # Dil desteği eklendi

def check_port(port):
    try:
        cmd = [
            "powershell",
            "-Command",
            f"(Get-NetTCPConnection -LocalPort {port} -ErrorAction SilentlyContinue) | ConvertTo-Json"
        ]

        result = subprocess.check_output(cmd).decode("utf-8")

        if not result.strip():
            return None

        data = json.loads(result)
        pid = data["OwningProcess"]
        return {
            "pid": pid,
            "name": get_process_name(pid)
        }
    except Exception as e:
        return None

def scan_ports():
    ports = [80, 443]
    results = {}

    for p in ports:
        r = check_port(p)
        results[p] = r

    return results
