import psutil
import shutil
import time
from alert import send_email_alert
from logger import log_data
from config import DISK_THRESHOLD

def check_disk_usage():
    total, used, free = shutil.disk_usage("/")
    usage_percent = (used / total) * 100
    return usage_percent

def check_system_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    return cpu, memory

def monitor():
    disk_usage = check_disk_usage()
    cpu, memory = check_system_metrics()

    log_data(disk_usage, cpu, memory)

    if disk_usage > DISK_THRESHOLD:
        send_email_alert(disk_usage)

if __name__ == "__main__":
    monitor()
