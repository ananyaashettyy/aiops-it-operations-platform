
# 🤖 AI-Powered IT Operations & AIOps Platform

An intelligent IT Operations and AIOps platform that monitors infrastructure, detects anomalies, generates alerts, manages incidents, and visualizes system health through a centralized React dashboard.

The platform combines **Python, FastAPI, React.js, MySQL, Machine Learning, Monitoring & Observability** and is designed to evolve toward **Generative AI, Cloud Monitoring, ITSM integration, and automated remediation**.

## ✨ Key Capabilities

- Real-time CPU, memory, disk, and network monitoring
- Threshold-based alert detection
- Incident creation and management
- MySQL-based telemetry persistence
- Machine-learning anomaly detection
- Historical infrastructure analytics
- React-based monitoring dashboard
- REST APIs using FastAPI

---

# 🏗️ Architecture

```text
                    ┌──────────────────────┐
                    │   Windows / Linux    │
                    │        Server        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Python Monitoring    │
                    │       psutil         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      FastAPI         │
                    │     REST APIs        │
                    └──────┬───────┬───────┘
                           │       │
                 ┌─────────┘       └─────────┐
                 ▼                           ▼
        ┌─────────────────┐        ┌─────────────────┐
        │      MySQL      │        │   Alert Engine  │
        │ Metrics/Incidents│       │   Thresholds    │
        └────────┬────────┘        └────────┬────────┘
                 │                          │
                 │                          ▼
                 │                 ┌─────────────────┐
                 │                 │    Incidents    │
                 │                 └─────────────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ ML Anomaly      │
        │ Detection       │
        │ Isolation Forest│
        └────────┬────────┘
                 │
                 ▼
        ┌──────────────────────┐
        │   React Dashboard    │
        │ Monitoring & Analytics│
        └──────────────────────┘


---

🔄 Workflow

System Metrics
      ↓
Monitoring
      ↓
FastAPI
      ↓
MySQL
      ↓
Alert Detection
      ↓
Incident Management
      ↓
ML Anomaly Detection
      ↓
React Dashboard


---

🛠️ Tech Stack

Backend: Python, FastAPI, Uvicorn, psutil
Frontend: React.js, Vite, JavaScript, Recharts
Database: MySQL
Machine Learning: Scikit-learn, Isolation Forest, NumPy
AIOps: Monitoring, Observability, Alerting, Incident Management, Anomaly Detection


---

▶️ Run Locally

Backend

cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

Frontend

cd frontend
npm install
npm run dev

API Documentation

http://127.0.0.1:8000/docs

Frontend

http://localhost:5173

