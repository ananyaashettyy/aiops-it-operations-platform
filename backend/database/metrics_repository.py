from database.database import get_connection


def save_metrics(metrics: dict) -> None:
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            INSERT INTO system_metrics (hostname, cpu_usage, memory_usage, disk_usage, bytes_sent, bytes_received)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            metrics["system"]["hostname"], metrics["cpu"]["usage_percent"],
            metrics["memory"]["usage_percent"], metrics["disk"]["usage_percent"],
            metrics["network"]["bytes_sent"], metrics["network"]["bytes_received"],
        ))
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def get_metric_history(limit: int = 100) -> list[dict]:
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT hostname, cpu_usage, memory_usage, disk_usage, bytes_sent, bytes_received, recorded_at
            FROM system_metrics ORDER BY recorded_at DESC LIMIT %s
        """, (limit,))
        return cursor.fetchall()
    finally:
        cursor.close()
        connection.close()
