from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from ai.anomaly_detector import AnomalyDetector
from alerts.alert_engine import generate_alerts
from database.database import DatabaseUnavailable
from database.database import initialize_database
from database.metrics_repository import get_metric_history, save_metrics
from incidents.incident_service import create_incident, get_incidents
from monitoring.system_monitor import get_system_metrics

anomaly_detector = AnomalyDetector()

app = FastAPI(
    title="AI-Powered IT Operations Platform",
    description="AIOps monitoring and incident management platform",
    version="1.0.0",
)


@app.on_event("startup")
def load_persistent_monitoring_history():
    """Initialize the optional MySQL schema and seed the ML model with its history."""
    try:
        initialize_database()
        anomaly_detector.load_history(get_metric_history(100))
    except DatabaseUnavailable:
        # Local development can use live monitoring before MySQL is configured.
        pass

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "AIOps Platform Backend is running",
        "status": "online",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/metrics")
def system_metrics():
    metrics = get_system_metrics()
    try:
        save_metrics(metrics)
    except DatabaseUnavailable:
        pass
    return metrics


@app.get("/metrics/history")
def metric_history():
    try:
        return {"metrics": get_metric_history(100)}
    except DatabaseUnavailable as error:
        raise HTTPException(status_code=503, detail=str(error)) from error


@app.get("/anomalies")
def detect_anomaly():
    metrics = get_system_metrics()
    # Detect before recording so the new observation does not influence its score.
    result = anomaly_detector.detect(metrics)
    anomaly_detector.add_metrics(metrics)
    return {
        "timestamp": metrics["timestamp"],
        "metrics": {
            "cpu": metrics["cpu"]["usage_percent"],
            "memory": metrics["memory"]["usage_percent"],
            "disk": metrics["disk"]["usage_percent"],
        },
        "anomaly": result,
    }


@app.get("/alerts")
def get_alerts():
    metrics = get_system_metrics()
    alerts = generate_alerts(metrics)
    incidents_created = []
    persistence_error = None
    for alert in alerts:
        try:
            incident_id = create_incident(alert)
            if incident_id:
                incidents_created.append(incident_id)
        except DatabaseUnavailable as error:
            persistence_error = str(error)
            break
    return {"count": len(alerts), "alerts": alerts, "incidents_created": incidents_created, "persistence_error": persistence_error}


@app.get("/incidents")
def incidents():
    try:
        return {"incidents": get_incidents()}
    except DatabaseUnavailable as error:
        raise HTTPException(status_code=503, detail=str(error)) from error
