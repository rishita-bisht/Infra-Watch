# Infra-Watch

A lightweight Linux infrastructure monitoring tool built with Bash.

Infra-Watch collects essential system metrics from a Linux machine, making it easy to monitor resource utilization and build a foundation for alerting, automation, and system observability.

## Features

- CPU utilization
- Memory utilization
- Disk utilization
- System load average
- Top 5 CPU-consuming processes
- Network statistics
- Persistent CSV-based metric storage
- Automated metric collection
- Log rotation and compression
- SQLite-based metric storage
- Slack webhook alerting with cooldown
- Automated report generation
- Text reports
- HTML reports
- Graph-based metric visualization
- systemd service and timer
- Prometheus-based metrics collection
- Node Exporter system metrics
- Grafana dashboard visualization

## Project Structure

```text
Infra-Watch/
├── alerts/
│   └── alert_checker.py
├── collectors/
│   └── collector.sh
├── config/
│   └── infrawatch
├── logs/
├── reports/
│   └── report_generator.py
├── storage/
│   ├── init_db.py
│   └── sync_to_db.py
├── systemd/
│   ├── infrawatch.service
│   └── infrawatch.timer
├── .gitignore
├── LICENSE
└── README.md
```

## Requirements

- Linux (tested on Kali Linux)
- Bash
- Python
- SQLite
- systemd
- Prometheus
- Node Exporter
- Grafana
- Standard Linux utilities:
  - top
  - free
  - df
  - ps
  - ss
- logrotate
- Slack Webhook

## Getting Started

Clone the repository:

    git clone https://github.com/rishita-bisht/Infra-Watch.git
    cd Infra-Watch

Make the script executable:

    chmod +x collectors/collector.sh

Run the collector:

    ./collectors/collector.sh

## Metrics Collected

| Metric | Source |
|---------|--------|
| CPU Usage | top |
| Memory Usage | free |
| Disk Usage | df |
| Load Average | /proc/loadavg |
| Top Processes | ps |
| Network Statistics | ss |

## Data Storage

Infra-Watch supports persistent storage of collected metrics.

Metrics are initially stored in CSV format and can also be stored in SQLite for structured querying and analysis.

Each metric collection is timestamped, allowing historical system performance data to be retained and analyzed.

## Scheduling

Infra-Watch uses systemd service and timer units to execute the metric collector automatically.

The systemd timer replaces the earlier cron-based scheduling approach and provides managed, persistent execution of the collector.

## Log Rotation

Log files are managed using Linux logrotate.

The configuration supports:

- Weekly log rotation
- Retention of previous logs
- Compression
- Handling of missing or empty logs
- copytruncate for active log files

## Alerting

Infra-Watch supports threshold-based alerting through a Slack webhook.

Alerts can be triggered when monitored system metrics exceed configured thresholds.

A cooldown mechanism prevents repeated alerts from being sent continuously while a condition remains active.

## Reports

Infra-Watch generates reports from collected system metrics.

Supported report formats include:

- Text reports
- HTML reports
- Graph-based visualizations

These reports provide a historical view of system resource utilization.

## Monitoring Stack

Infra-Watch can be integrated with a Prometheus and Grafana monitoring stack.

Node Exporter exposes system-level metrics which are scraped by Prometheus.

Grafana uses Prometheus as a data source to visualize system metrics through dashboards.

The monitoring flow is:

    Linux System
         |
         v
    Node Exporter
         |
         v
    Prometheus
         |
         v
    Grafana Dashboard

The dashboard provides visualization for metrics such as:

- CPU usage
- Memory usage
- Disk usage

## Service Management

Infra-Watch includes systemd units for managed execution:

    systemd/infrawatch.service
    systemd/infrawatch.timer

The service executes the collector while the timer controls its scheduled execution.

## Roadmap

- [x] System metrics collection
- [x] Load average monitoring
- [x] Process monitoring
- [x] Network statistics
- [x] Persistent CSV storage
- [x] Automated metric collection
- [x] Log rotation
- [x] SQLite storage
- [x] Threshold-based alerting
- [x] Slack webhook notifications
- [x] Alert cooldown
- [x] Automated report generation
- [x] HTML reports
- [x] Graph-based visualization
- [x] Service management with systemd
- [x] Prometheus integration
- [x] Node Exporter integration
- [x] Grafana dashboard
- [ ] Docker support

## Tech Stack

- Bash
- Linux
- systemd
- Prometheus
- Node Exporter
- Grafana
- Cron
- Logrotate
- SQLite
- Python
- Git
- Slack Webhooks

## Contributing

Contributions, suggestions, and improvements are welcome. Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Author

**Rishita Bisht**
