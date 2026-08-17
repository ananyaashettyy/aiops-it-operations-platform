from database.database import get_connection


def create_incident(alert: dict) -> str | None:
    """Save one open incident per resource type to avoid repeated duplicates."""
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT incident_id FROM incidents WHERE status = 'OPEN' AND alert_type = %s LIMIT 1", (alert["type"],))
        if cursor.fetchone():
            return None
        cursor.execute("SELECT COUNT(*) FROM incidents")
        incident_id = f"INC-{cursor.fetchone()[0] + 1:06d}"
        cursor.execute("""
            INSERT INTO incidents (incident_id, alert_type, severity, title, message, value, status)
            VALUES (%s, %s, %s, %s, %s, %s, 'OPEN')
        """, (incident_id, alert["type"], alert["severity"], alert["title"], alert["message"], alert["value"]))
        connection.commit()
        return incident_id
    finally:
        cursor.close()
        connection.close()


def get_incidents() -> list[dict]:
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT id, incident_id, alert_type, severity, title, message, value, status, created_at, resolved_at
            FROM incidents ORDER BY created_at DESC
        """)
        return cursor.fetchall()
    finally:
        cursor.close()
        connection.close()
