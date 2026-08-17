"""In-memory Isolation Forest anomaly detector for local system behavior."""
import numpy as np
from sklearn.ensemble import IsolationForest


class AnomalyDetector:
    def __init__(self) -> None:
        self.model = IsolationForest(contamination=0.1, random_state=42)
        self.history: list[list[float]] = []

    @staticmethod
    def _point(metrics: dict) -> list[float]:
        return [
            metrics["cpu"]["usage_percent"],
            metrics["memory"]["usage_percent"],
            metrics["disk"]["usage_percent"],
        ]

    def add_metrics(self, metrics: dict) -> None:
        self.history.append(self._point(metrics))
        if len(self.history) > 100:
            self.history.pop(0)

    def load_history(self, historical_metrics: list[dict]) -> None:
        self.history = [[float(item["cpu_usage"]), float(item["memory_usage"]), float(item["disk_usage"])] for item in reversed(historical_metrics)][-100:]

    def detect(self, metrics: dict) -> dict:
        if len(self.history) < 10:
            return {"is_anomaly": False, "confidence": 0, "message": f"Collecting historical data ({len(self.history)}/10)..."}
        historical_data = np.array(self.history)
        current_data = np.array([self._point(metrics)])
        self.model.fit(historical_data)
        prediction = self.model.predict(current_data)[0]
        score = float(self.model.decision_function(current_data)[0])
        if prediction == -1:
            return {"is_anomaly": True, "confidence": round(abs(score) * 100, 2), "message": "Unusual system behavior detected"}
        return {"is_anomaly": False, "confidence": round(max(0, score) * 100, 2), "message": "System behavior is normal"}
