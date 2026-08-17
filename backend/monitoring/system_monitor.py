"""Local system telemetry collector for the Day 3 dashboard."""
from datetime import datetime
import os
import platform

import psutil


def get_system_metrics() -> dict:
    memory = psutil.virtual_memory()
    # SystemDrive is C: on normal Windows installations; '/' keeps this portable.
    disk_path = f"{os.environ.get('SystemDrive', 'C:')}\\" if os.name == "nt" else "/"
    disk = psutil.disk_usage(disk_path)
    network = psutil.net_io_counters()

    return {
        "timestamp": datetime.now().isoformat(),
        "system": {
            "os": platform.system(),
            "os_version": platform.version(),
            "hostname": platform.node(),
            "processor": platform.processor(),
        },
        "cpu": {"usage_percent": psutil.cpu_percent(interval=0.2), "cores": psutil.cpu_count(logical=True)},
        "memory": {
            "usage_percent": memory.percent,
            "total_gb": round(memory.total / (1024 ** 3), 2),
            "used_gb": round(memory.used / (1024 ** 3), 2),
            "available_gb": round(memory.available / (1024 ** 3), 2),
        },
        "disk": {
            "usage_percent": disk.percent,
            "total_gb": round(disk.total / (1024 ** 3), 2),
            "used_gb": round(disk.used / (1024 ** 3), 2),
            "free_gb": round(disk.free / (1024 ** 3), 2),
        },
        "network": {"bytes_sent": network.bytes_sent, "bytes_received": network.bytes_recv},
    }
