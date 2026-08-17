"""MySQL connection and schema bootstrap for incident persistence."""
import os

import mysql.connector
from mysql.connector import Error


class DatabaseUnavailable(Exception):
    pass


def _config(include_database: bool = True) -> dict:
    config = {
        "host": os.getenv("MYSQL_HOST", "127.0.0.1"),
        "port": int(os.getenv("MYSQL_PORT", "3306")),
        "user": os.getenv("MYSQL_USER", "root"),
        "password": os.getenv("MYSQL_PASSWORD", ""),
        "connection_timeout": 3,
    }
    if include_database:
        config["database"] = os.getenv("MYSQL_DATABASE", "aiops_db")
    return config


def get_connection():
    try:
        return mysql.connector.connect(**_config())
    except Error as error:
        raise DatabaseUnavailable(f"MySQL is unavailable: {error.msg}") from error


def initialize_database() -> None:
    """Creates the database and incidents table after MySQL credentials are configured."""
    try:
        connection = mysql.connector.connect(**_config(include_database=False))
        cursor = connection.cursor()
        database = os.getenv("MYSQL_DATABASE", "aiops_db")
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{database}`")
        cursor.execute(f"USE `{database}`")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS incidents (
                id INT AUTO_INCREMENT PRIMARY KEY,
                incident_id VARCHAR(50) UNIQUE NOT NULL,
                alert_type VARCHAR(50) NOT NULL,
                severity VARCHAR(20) NOT NULL,
                title VARCHAR(255) NOT NULL,
                message TEXT NOT NULL,
                value DECIMAL(10,2),
                status VARCHAR(20) DEFAULT 'OPEN',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                resolved_at TIMESTAMP NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS system_metrics (
                id INT AUTO_INCREMENT PRIMARY KEY,
                hostname VARCHAR(255) NOT NULL,
                cpu_usage DECIMAL(5,2) NOT NULL,
                memory_usage DECIMAL(5,2) NOT NULL,
                disk_usage DECIMAL(5,2) NOT NULL,
                bytes_sent BIGINT DEFAULT 0,
                bytes_received BIGINT DEFAULT 0,
                recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        connection.commit()
        cursor.close()
        connection.close()
    except Error as error:
        raise DatabaseUnavailable(f"MySQL setup failed: {error.msg}") from error
