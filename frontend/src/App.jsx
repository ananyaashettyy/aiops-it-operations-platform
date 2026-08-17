import { useEffect, useState } from "react";
import { CartesianGrid, Legend, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import "./App.css";

function App() {
  const [backendStatus, setBackendStatus] = useState("Connecting...");
  const [metrics, setMetrics] = useState(null);
  const [alerts, setAlerts] = useState([]);
  const [incidents, setIncidents] = useState([]);
  const [anomaly, setAnomaly] = useState(null);
  const [history, setHistory] = useState([]);

  useEffect(() => {
    const fetchMetrics = () => fetch("http://127.0.0.1:8000/metrics")
      .then((response) => {
        if (!response.ok) throw new Error("Failed to fetch metrics");
        return response.json();
      })
      .then((data) => {
        setBackendStatus("Connected");
        setMetrics(data);
      })
      .catch(() => setBackendStatus("Backend Offline"));
    fetchMetrics();
    const interval = setInterval(fetchMetrics, 5000);
    return () => clearInterval(interval);
  }, []);

  const fetchHistory = () => fetch("http://127.0.0.1:8000/metrics/history")
    .then((response) => {
      if (!response.ok) throw new Error("Metric history database is not available");
      return response.json();
    })
    .then((data) => setHistory([...data.metrics].reverse().map((item) => ({
      time: new Date(item.recorded_at).toLocaleTimeString(), cpu: Number(item.cpu_usage),
      memory: Number(item.memory_usage), disk: Number(item.disk_usage),
    }))))
    .catch((error) => console.info(error.message));

  useEffect(() => {
    fetchHistory();
    const interval = setInterval(fetchHistory, 5000);
    return () => clearInterval(interval);
  }, []);

  const fetchAnomaly = () => fetch("http://127.0.0.1:8000/anomalies")
    .then((response) => {
      if (!response.ok) throw new Error("Failed to fetch anomaly data");
      return response.json();
    })
    .then(setAnomaly)
    .catch((error) => console.error(error));

  useEffect(() => {
    fetchAnomaly();
    const interval = setInterval(fetchAnomaly, 5000);
    return () => clearInterval(interval);
  }, []);

  const fetchIncidents = () => fetch("http://127.0.0.1:8000/incidents")
    .then((response) => {
      if (!response.ok) throw new Error("Incident database is not available");
      return response.json();
    })
    .then((data) => setIncidents(data.incidents))
    .catch((error) => console.info(error.message));

  useEffect(() => {
    fetchIncidents();
    const interval = setInterval(fetchIncidents, 5000);
    return () => clearInterval(interval);
  }, []);

  const fetchAlerts = () => fetch("http://127.0.0.1:8000/alerts")
    .then((response) => {
      if (!response.ok) throw new Error("Failed to fetch alerts");
      return response.json();
    })
    .then((data) => setAlerts(data.alerts))
    .catch((error) => console.error(error));

  useEffect(() => {
    fetchAlerts();
    const interval = setInterval(fetchAlerts, 5000);
    return () => clearInterval(interval);
  }, []);

  const formatBytes = (bytes) => {
    if (bytes == null) return "--";
    return `${(bytes / (1024 ** 3)).toFixed(2)} GB`;
  };

  return (
    <div className="app">
      <header className="header">
        <div><h1>AI-Ops Command Center</h1><p>AI-Powered IT Operations &amp; Monitoring Platform</p></div>
        <div className="status"><span className="status-dot"></span>{backendStatus}</div>
      </header>
      <main>
        <section className="cards">
          <div className="card"><h3>Backend</h3><p className="value">{backendStatus}</p></div>
          <div className="card"><h3>System Health</h3><p className="value">{metrics ? "healthy" : "Checking..."}</p></div>
          <div className="card"><h3>Active Incidents</h3><p className="value">{incidents.filter((item) => item.status === "OPEN").length || alerts.length}</p></div>
          <div className="card"><h3>Monitored Servers</h3><p className="value">{metrics ? 1 : 0}</p></div>
        </section>
        <section className="dashboard"><h2>Monitoring Overview</h2>
          <div className="monitor-grid">
            <div className="monitor-card"><h3>CPU Usage</h3><div className="metric">{metrics ? `${metrics.cpu.usage_percent}%` : "--%"}</div><p>{metrics ? `${metrics.cpu.cores} logical cores` : "Waiting for monitoring agent"}</p></div>
            <div className="monitor-card"><h3>Memory Usage</h3><div className="metric">{metrics ? `${metrics.memory.usage_percent}%` : "--%"}</div><p>{metrics ? `${metrics.memory.used_gb} GB of ${metrics.memory.total_gb} GB used` : "Waiting for monitoring agent"}</p></div>
            <div className="monitor-card"><h3>Disk Usage</h3><div className="metric">{metrics ? `${metrics.disk.usage_percent}%` : "--%"}</div><p>{metrics ? `${metrics.disk.free_gb} GB free` : "Waiting for monitoring agent"}</p></div>
            <div className="monitor-card"><h3>Network</h3><div className="metric network-value">{metrics ? formatBytes(metrics.network.bytes_received) : "--"}</div><p>{metrics ? `${formatBytes(metrics.network.bytes_sent)} sent` : "Waiting for monitoring agent"}</p></div>
          </div>
        </section>
        <section className="dashboard"><h2>Infrastructure Performance Trends</h2>
          <div className="chart-card">{history.length === 0 ? <p className="chart-empty">Historical charts appear after MySQL monitoring storage is configured.</p> :
            <ResponsiveContainer width="100%" height={350}><LineChart data={history}><CartesianGrid strokeDasharray="3 3" /><XAxis dataKey="time" /><YAxis domain={[0, 100]} /><Tooltip /><Legend />
              <Line type="monotone" dataKey="cpu" name="CPU %" stroke="#2563eb" strokeWidth={2} dot={false} />
              <Line type="monotone" dataKey="memory" name="Memory %" stroke="#e11d48" strokeWidth={2} dot={false} />
              <Line type="monotone" dataKey="disk" name="Disk %" stroke="#16a34a" strokeWidth={2} dot={false} />
            </LineChart></ResponsiveContainer>}
          </div>
        </section>
        <section className="dashboard">
          <h2>AI Anomaly Detection</h2>
          {!anomaly ? <div className="no-alerts"><h3>Loading AI analysis...</h3><p>Collecting system behavior data.</p></div> :
            <div className={`anomaly-card ${anomaly.anomaly.is_anomaly ? "anomaly-detected" : ""}`}>
              <div className="anomaly-header"><div><h3>{anomaly.anomaly.is_anomaly ? "⚠ Anomaly Detected" : "✓ Normal System Behavior"}</h3><p>{anomaly.anomaly.message}</p></div><div className="confidence">{anomaly.anomaly.confidence}%<span>confidence</span></div></div>
              <div className="anomaly-metrics"><div><strong>CPU</strong><span>{anomaly.metrics.cpu}%</span></div><div><strong>Memory</strong><span>{anomaly.metrics.memory}%</span></div><div><strong>Disk</strong><span>{anomaly.metrics.disk}%</span></div></div>
            </div>}
        </section>
        <section className="dashboard">
          <h2>Incident Management</h2>
          {incidents.length === 0 ? (
            <div className="no-alerts"><h3>✓ No Incidents Recorded</h3><p>No incidents have been detected by the monitoring system, or MySQL has not been configured yet.</p></div>
          ) : (
            <div className="incident-list">
              {incidents.map((incident) => <div className={`incident ${incident.severity.toLowerCase()}`} key={incident.incident_id}>
                <div className="incident-header"><div><h3>{incident.incident_id} — {incident.title}</h3><span className="severity">{incident.severity}</span></div><div className="incident-value">{incident.value}%</div></div>
                <p>{incident.message}</p><div className="incident-footer"><span>Type: {incident.alert_type}</span><span>Status: {incident.status}</span><span>{new Date(incident.created_at).toLocaleString()}</span></div>
              </div>)}
            </div>
          )}
        </section>
      </main>
    </div>
  );
}

export default App;
