

# 🚀 AI-Powered IT Operations & AIOps Platform

An intelligent IT Operations and AIOps platform for **real-time infrastructure monitoring, alert detection, incident management, machine-learning-based anomaly detection, and historical performance analytics**.

The project combines **Python, FastAPI, React.js, MySQL, Scikit-learn, Monitoring & Observability** to demonstrate how traditional IT monitoring can evolve into an intelligent AIOps platform.

---

## 🌐 Project Status

**Current Status:** 🚧 Active Development

The current version implements the core AIOps monitoring foundation:

- ✅ Real-time system monitoring
- ✅ CPU, memory, disk and network monitoring
- ✅ FastAPI REST APIs
- ✅ React monitoring dashboard
- ✅ Threshold-based alerting
- ✅ Incident management
- ✅ MySQL persistence
- ✅ Historical metrics collection
- ✅ ML-based anomaly detection
- ✅ Infrastructure performance visualization
- 🚧 Generative AI incident analysis
- 🚧 Root-cause analysis
- 🚧 ServiceNow/Jira integration
- 🚧 Automated remediation
- 🚧 Cloud infrastructure monitoring
- 🚧 Kubernetes monitoring

---

# 🎯 Project Objective

Modern IT environments generate large amounts of infrastructure and application telemetry.

Traditional monitoring systems generally depend on fixed thresholds:

```text
CPU > 90%
      ↓
   ALERT

This project aims to evolve that approach into an AIOps workflow:

Monitor
   ↓
Detect
   ↓
Analyze
   ↓
Correlate
   ↓
Predict
   ↓
Recommend
   ↓
Remediate

The long-term goal is to create an intelligent IT Operations platform capable of identifying abnormal infrastructure behavior, understanding incidents, suggesting root causes, recommending remediation actions, and integrating with enterprise ITSM platforms.


---

🏗️ Architecture

┌──────────────────────────┐
                         │     Windows / Linux      │
                         │          Host            │
                         └────────────┬─────────────┘
                                      │
                                      ▼
                         ┌──────────────────────────┐
                         │   Python Monitoring      │
                         │         psutil           │
                         └────────────┬─────────────┘
                                      │
                                      ▼
                         ┌──────────────────────────┐
                         │         FastAPI          │
                         │       REST Backend       │
                         └───────┬─────────┬────────┘
                                 │         │
                  ┌──────────────┘         └──────────────┐
                  ▼                                       ▼
        ┌──────────────────┐                    ┌──────────────────┐
        │      MySQL       │                    │   Alert Engine   │
        │                  │                    │                  │
        │ System Metrics   │                    │ Threshold Rules  │
        │ Incidents        │                    │ Severity         │
        └────────┬─────────┘                    └────────┬─────────┘
                 │                                       │
                 │                                       ▼
                 │                              ┌──────────────────┐
                 │                              │ Incident Manager │
                 │                              └──────────────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ ML Anomaly       │
        │ Detection        │
        │                  │
        │ Isolation Forest │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────────────┐
        │      React Dashboard     │
        │                          │
        │ Monitoring               │
        │ Alerts                   │
        │ Incidents                │
        │ Anomalies                │
        │ Performance Trends       │
        └──────────────────────────┘


---

✨ Key Features

1. Real-Time System Monitoring

The platform collects real-time infrastructure metrics using Python and psutil.

Currently monitored:

CPU utilization

Memory utilization

Disk utilization

Network traffic

Hostname

Operating system

Processor information

Monitoring timestamp


Example:

CPU Usage       24%
Memory Usage    63%
Disk Usage      72%
Network         Online
OS              Windows
Hostname        MY-PC


---

2. FastAPI REST Backend

The backend is developed using FastAPI and provides REST APIs for monitoring and operations.

Current API endpoints

GET /health
GET /metrics
GET /metrics/history
GET /alerts
GET /incidents
GET /anomalies

Health API

GET /health

Used to verify backend availability.

Example response:

{
  "status": "healthy"
}


---

Current Metrics

GET /metrics

Returns the latest infrastructure metrics.


---

Historical Metrics

GET /metrics/history

Returns historical infrastructure telemetry stored in MySQL.


---

Alerts

GET /alerts

Evaluates current infrastructure metrics against predefined thresholds.


---

Incidents

GET /incidents

Returns incidents stored in the MySQL database.


---

Anomaly Detection

GET /anomalies

Analyzes infrastructure behavior using the machine-learning anomaly detection engine.


---

3. React.js AIOps Dashboard

The frontend provides a centralized monitoring dashboard built using React.js.

The dashboard displays:

Backend status

System health

Hostname

Operating system

CPU usage

Memory usage

Disk usage

Network status

AI anomaly status

Incident history

Infrastructure performance trends


The dashboard automatically refreshes monitoring information periodically.


---

4. Threshold-Based Alert Engine

The platform contains a rule-based alert engine for detecting infrastructure problems.

Example:

CPU >= 80%
       ↓
   WARNING

CPU >= 90%
       ↓
  CRITICAL

Similarly:

Memory >= 80% → WARNING
Memory >= 90% → CRITICAL

Disk >= 80% → WARNING
Disk >= 90% → CRITICAL

Example alert:

Type: CPU
Severity: CRITICAL
Title: High CPU Usage
Message: CPU usage has reached 94%
Value: 94%

This provides the first layer of automated infrastructure monitoring.


---

5. Incident Management

When an alert is detected, the platform can create a persistent incident.

Each incident receives a unique identifier:

INC-000001

An incident contains:

Incident ID
Alert Type
Severity
Title
Message
Metric Value
Status
Created At
Resolved At

Example:

INC-000001

Title: High CPU Usage
Type: CPU
Severity: WARNING
Value: 86%
Status: OPEN

The system also prevents repeated creation of the same open incident for a continuously active alert.


---

6. MySQL Database

MySQL is used as the persistence layer.

Database:

aiops_db

Tables:

system_metrics
incidents


---

system_metrics

Stores historical infrastructure telemetry.

id
hostname
cpu_usage
memory_usage
disk_usage
bytes_sent
bytes_received
recorded_at

Example:

Hostname:       MY-PC
CPU:            24.5%
Memory:         63.2%
Disk:           71.8%
Recorded At:    2026-08-18 08:20:00


---

incidents

Stores detected infrastructure incidents.

id
incident_id
alert_type
severity
title
message
value
status
created_at
resolved_at


---

7. Machine Learning Anomaly Detection

The project goes beyond traditional threshold-based monitoring by implementing machine-learning-based behavioral anomaly detection.

The current implementation uses:

Scikit-learn
        +
Isolation Forest

The model analyzes:

CPU
Memory
Disk

Instead of only checking:

CPU > 90%

the ML engine evaluates whether the current infrastructure behavior is unusual compared with historical behavior.

Example:

Normal:

20% → 22% → 23% → 25% → 27%

Sudden behavior:

27% → 45% → 67% → 81%
                    ↓
               ANOMALY

The API can return:

{
  "anomaly": {
    "is_anomaly": true,
    "confidence": 82.4,
    "message": "Unusual system behavior detected"
  }
}


---

8. Historical Infrastructure Analytics

The platform stores system telemetry in MySQL and uses the historical data to visualize infrastructure behavior.

Metrics visualized include:

CPU

Memory

Disk


Example:

100% ┤
     │
 75% ┤              ╭──────╮
     │         ╭────╯      ╰───
 50% ┤    ╭────╯
     │────╯
 25% ┤
     │
  0% └────────────────────────────
        Time →

This provides visibility into infrastructure performance trends.


---

🔄 End-to-End Workflow

The current platform follows this workflow:

System
  │
  ▼
Collect Metrics
  │
  ▼
Python Monitoring
  │
  ▼
FastAPI
  │
  ├───────────────► MySQL
  │                   │
  │                   └── Historical Metrics
  │
  ▼
Alert Engine
  │
  ├── Normal ─────────────► Continue Monitoring
  │
  └── Threshold Exceeded
              │
              ▼
        Create Incident
              │
              ▼
             MySQL
              │
              ▼
       ML Anomaly Detection
              │
              ▼
       React AIOps Dashboard


---

🧠 AIOps Detection Model

The platform currently uses two complementary detection approaches.

Rule-Based Detection

Metric
  ↓
Threshold
  ↓
Alert

Useful for known conditions such as:

CPU > 90%
Disk > 90%
Memory > 90%


---

ML-Based Detection

Historical Metrics
       ↓
Machine Learning
       ↓
Behavioral Analysis
       ↓
Anomaly

This allows the platform to identify unusual patterns that may not necessarily cross a fixed threshold.


---

📁 Project Structure

aiops-platform/
│
├── backend/
│   │
│   ├── main.py
│   ├── requirements.txt
│   ├── .env.example
│   │
│   ├── ai/
│   │   ├── __init__.py
│   │   └── anomaly_detector.py
│   │
│   ├── alerts/
│   │   ├── __init__.py
│   │   └── alert_engine.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── metrics_repository.py
│   │
│   ├── incidents/
│   │   ├── __init__.py
│   │   └── incident_service.py
│   │
│   └── monitoring/
│       ├── __init__.py
│       └── system_monitor.py
│
├── frontend/
│   │
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   │
│   └── src/
│       ├── App.jsx
│       ├── App.css
│       ├── index.css
│       └── main.jsx
│
├── .gitignore
└── README.md


---

🛠️ Technology Stack

Programming

Python

JavaScript

SQL


Backend

FastAPI

Uvicorn

REST APIs

psutil


Frontend

React.js

Vite

Recharts

HTML5

CSS3


Database

MySQL


Machine Learning

Scikit-learn

Isolation Forest

NumPy


Monitoring & Observability

Infrastructure Monitoring

Metrics Collection

Alerting

Incident Management

Anomaly Detection

Historical Telemetry

Performance Analytics


Development Tools

Git

GitHub

VS Code

MySQL Workbench

Postman



---

💻 Local Installation

Prerequisites

Install:

Python 3.x

Node.js

npm

MySQL Server

MySQL Workbench

Git



---

⚙️ Backend Setup

Clone the repository:

git clone https://github.com/ananyaashettyy/aiops-it-operations-platform.git

Navigate into the project:

cd aiops-it-operations-platform

Navigate to backend:

cd backend

Create a virtual environment:

python -m venv venv

Activate it on Windows:

.\venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt


---

🗄️ Database Configuration

Create the database:

CREATE DATABASE aiops_db;

Select it:

USE aiops_db;

Create the metrics table:

CREATE TABLE system_metrics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hostname VARCHAR(255) NOT NULL,
    cpu_usage DECIMAL(5,2) NOT NULL,
    memory_usage DECIMAL(5,2) NOT NULL,
    disk_usage DECIMAL(5,2) NOT NULL,
    bytes_sent BIGINT DEFAULT 0,
    bytes_received BIGINT DEFAULT 0,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Create the incidents table:

CREATE TABLE incidents (
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
);


---

🔐 Environment Variables

Create a local .env file:

DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=aiops_db

Do not commit .env to GitHub.

The repository contains:

backend/.env.example

as a safe configuration template.


---

▶️ Start the Backend

From the backend directory:

uvicorn main:app --reload

Backend:

http://127.0.0.1:8000

FastAPI documentation:

http://127.0.0.1:8000/docs


---

▶️ Start the Frontend

Open another terminal:

cd frontend

Install dependencies:

npm install

Start the development server:

npm run dev

The frontend will normally be available at:

http://localhost:5173


---

🔍 API Testing

FastAPI provides interactive API documentation:

http://127.0.0.1:8000/docs

The following APIs can be tested:

GET /health
GET /metrics
GET /metrics/history
GET /alerts
GET /incidents
GET /anomalies


---

📊 Current Capabilities

Capability	Status

React Dashboard	✅
FastAPI Backend	✅
REST APIs	✅
CPU Monitoring	✅
Memory Monitoring	✅
Disk Monitoring	✅
Network Monitoring	✅
Threshold-Based Alerts	✅
Alert Severity	✅
Incident Creation	✅
Incident Persistence	✅
MySQL Integration	✅
Historical Metrics	✅
ML Anomaly Detection	✅
Isolation Forest	✅
Performance Charts	✅
Generative AI	🚧
LLM Incident Analysis	🚧
Root-Cause Analysis	🚧
AI Operations Chatbot	🚧
ServiceNow Integration	🚧
Jira Integration	🚧
Automated Remediation	🚧
Docker	🚧
Kubernetes	🚧
Terraform	🚧
AWS Monitoring	🚧
Azure Monitoring	🚧
Google Cloud Monitoring	🚧



---

☁️ Planned Cloud Architecture

The future deployment architecture will separate the monitoring agent from the cloud platform.

┌──────────────────────┐
                 │   Windows / Linux    │
                 │      Endpoint        │
                 └──────────┬───────────┘
                            │
                            │ Telemetry
                            ▼
                 ┌──────────────────────┐
                 │   Monitoring Agent   │
                 │       Python         │
                 └──────────┬───────────┘
                            │
                            ▼
                   Internet / API
                            │
                            ▼
                 ┌──────────────────────┐
                 │    AIOps Backend     │
                 │      FastAPI         │
                 └──────────┬───────────┘
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
          ┌────────┐   ┌──────────┐  ┌──────────┐
          │ MySQL  │   │ ML/AI    │  │ ITSM     │
          │        │   │ Engine   │  │ Systems  │
          └────────┘   └──────────┘  └──────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    React Dashboard   │
                 └──────────────────────┘

This architecture will allow the platform to monitor remote infrastructure rather than only the machine running the backend.


---

🤖 Future Generative AI Architecture

The next major stage is to introduce LLM-powered incident analysis.

Planned workflow:

Infrastructure Alert
        ↓
Incident Created
        ↓
Collect Metrics + Logs
        ↓
AI / LLM Analysis
        ↓
Root Cause Analysis
        ↓
Incident Summary
        ↓
Recommended Remediation
        ↓
ITSM Ticket
        ↓
Engineer Approval
        ↓
Remediation
        ↓
Verification
        ↓
Incident Resolution

Potential technologies:

Azure AI Foundry

Google Vertex AI

LLMs

LangChain

Prompt Engineering

Retrieval-Augmented Generation

Agentic AI



---

🧩 Planned ITSM Integration

The platform is designed to integrate with enterprise IT service management systems.

Planned integrations:

AIOps Platform
      │
      ├──► ServiceNow
      │
      └──► Jira

Example workflow:

CPU Anomaly
    ↓
AI Analysis
    ↓
Incident Created
    ↓
ServiceNow / Jira Ticket
    ↓
Assigned to IT Team


---

☁️ Planned Cloud Monitoring

Future versions will monitor cloud infrastructure including:

AWS

EC2

Lambda

S3

CloudWatch


Microsoft Azure

Virtual Machines

Azure Monitor

Azure Resource Manager

Storage

Compute resources


Google Cloud

Compute Engine

Cloud Monitoring

Cloud Logging



---

🐳 Planned DevOps & Cloud-Native Architecture

The platform will eventually be containerized and deployed using:

Docker
   ↓
Kubernetes
   ↓
Cloud Infrastructure

Infrastructure provisioning will be automated using:

Terraform

Planned CI/CD:

GitHub
   ↓
CI/CD Pipeline
   ↓
Docker Build
   ↓
Container Registry
   ↓
Kubernetes
   ↓
Production


---

🔐 Security Considerations

The project follows basic security practices during development.

Sensitive configuration should be stored using environment variables.

Examples:

Database passwords
API keys
LLM credentials
Cloud credentials
ServiceNow credentials
Jira credentials

These should never be committed to GitHub.

The .gitignore file excludes:

.env
venv/
node_modules/
dist/
logs


---

📚 Learning Outcomes

This project provides practical experience with:

Software Development

Python

JavaScript

React.js

FastAPI

REST API development

Full-stack architecture


IT Operations

Infrastructure monitoring

Metrics collection

Alerting

Incident management

Observability

Incident lifecycle


Data & AI

MySQL

Historical telemetry

Machine learning

Isolation Forest

Anomaly detection

Behavioral analysis


DevOps

Git

GitHub

Virtual environments

Dependency management

Planned Docker/Kubernetes/Terraform integration



---

🎓 Project Use Case

This platform can be used by IT Operations teams to monitor infrastructure and identify potential operational issues.

Example scenario:

A production server starts experiencing abnormal CPU behavior.

            ↓

Monitoring agent detects increasing CPU utilization.

            ↓

Metrics are stored in MySQL.

            ↓

Threshold engine evaluates the metric.

            ↓

ML anomaly detector identifies unusual behavior.

            ↓

An incident is created.

            ↓

Dashboard displays the incident.

            ↓

Future AI module analyzes logs and metrics.

            ↓

AI recommends a probable root cause and remediation.

            ↓

Future ITSM integration creates a ServiceNow/Jira ticket.


---

📈 Roadmap

Phase 1 — Monitoring Foundation

[x] Python system monitoring

[x] CPU monitoring

[x] Memory monitoring

[x] Disk monitoring

[x] Network monitoring

[x] FastAPI backend

[x] React dashboard


Phase 2 — Alerting & Incidents

[x] Threshold-based alerting

[x] Severity classification

[x] Incident creation

[x] Incident persistence

[x] Incident history


Phase 3 — AIOps Analytics

[x] Historical telemetry

[x] Performance charts

[x] Isolation Forest

[x] Behavioral anomaly detection


Phase 4 — Generative AI

[ ] LLM integration

[ ] AI incident summaries

[ ] Root-cause analysis

[ ] Resolution recommendations

[ ] IT Operations chatbot


Phase 5 — ITSM Automation

[ ] ServiceNow integration

[ ] Jira integration

[ ] Automatic ticket creation

[ ] Incident synchronization


Phase 6 — Cloud & DevOps

[ ] Docker

[ ] Kubernetes

[ ] Terraform

[ ] AWS monitoring

[ ] Azure monitoring

[ ] Google Cloud monitoring

[ ] CI/CD


Phase 7 — Autonomous Operations

[ ] Automated remediation

[ ] Remediation approval workflow

[ ] Post-remediation verification

[ ] Predictive failure detection

[ ] Autonomous incident resolution



---

🏆 Project Vision

The ultimate vision is to build an enterprise-style AIOps platform that can:

OBSERVE
   ↓
DETECT
   ↓
UNDERSTAND
   ↓
PREDICT
   ↓
RECOMMEND
   ↓
AUTOMATE
   ↓
VERIFY

The platform will progressively combine:

Monitoring
+
Observability
+
Machine Learning
+
Generative AI
+
ITSM
+
Cloud
+
DevOps
+
Automation
=
Intelligent IT Operations


---

👩‍💻 Author

Ananya R Shetty

B.E. — Information Science and Engineering

Interests:

AIOps

Cloud Computing

DevOps

Generative AI

Infrastructure Automation

Monitoring & Observability

Full-Stack Development



---

📌 Repository

GitHub:

https://github.com/ananyaashettyy/aiops-it-operations-platform


---

