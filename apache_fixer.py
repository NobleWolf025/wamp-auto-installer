import subprocess
from languages import get_text

def check_service(service_name):
    try:
        result = subprocess.check_output(
            ["sc", "query", service_name],
            stderr=subprocess.STDOUT,
            shell=True
        ).decode("utf-8")

        if "RUNNING" in result:
            return "RUNNING"
        elif "STOPPED" in result:
            return "STOPPED"
        else:
            return "UNKNOWN"
    except:
        return "NOT_FOUND"

def start_service(service_name):
    try:
        subprocess.run(["sc", "start", service_name], shell=True)
        return True
    except:
        return False
