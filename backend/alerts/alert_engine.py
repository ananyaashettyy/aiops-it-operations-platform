"""Threshold-based incident detection for local system metrics."""


def _alert(resource_type: str, severity: str, value: float) -> dict:
    label = resource_type.title()
    level = "Critical" if severity == "CRITICAL" else "High"
    return {
        "type": resource_type,
        "severity": severity,
        "title": f"{level} {label} Usage",
        "message": f"{label} usage has reached {value}%",
        "value": value,
    }


def generate_alerts(metrics: dict) -> list[dict]:
    """Return at most one open alert per monitored resource."""
    alerts = []
    resources = {
        "CPU": metrics["cpu"]["usage_percent"],
        "MEMORY": metrics["memory"]["usage_percent"],
        "DISK": metrics["disk"]["usage_percent"],
    }
    for resource_type, value in resources.items():
        if value >= 90:
            alerts.append(_alert(resource_type, "CRITICAL", value))
        elif value >= 80:
            alerts.append(_alert(resource_type, "WARNING", value))
    return alerts
