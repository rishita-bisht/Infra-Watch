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
- Automated metric collection using cron
- Log rotation and compression
- SQLite-based metric storage
- Slack webhook alerting with cooldown
- Automated report generation
- Text reports
- HTML reports
- Graph-based metric visualization

## Project Structure

Infra-Watch/
├── collectors/
│   └── collector.sh
├── logs/
├── reports/
├── config/
├── .gitignore
├── LICENSE
└── README.md

## Requirements

- Linux (tested on Kali Linux)
- Bash
- Python
- SQLite
- Standard Linux utilities:
  - top
  - free
  - df
  - ps
  - ss
- cron
- logrotate

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

Infra-Watch uses cron to automatically execute the collector at a scheduled interval instead of requiring manual execution.

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

## Roadmap

- [x] System metrics collection
- [x] Load average monitoring
- [x] Process monitoring
- [x] Network statistics
- [x] Persistent CSV storage
- [x] Automated metric collection with cron
- [x] Log rotation
- [x] SQLite storage
- [x] Threshold-based alerting
- [x] Slack webhook notifications
- [x] Alert cooldown
- [x] Automated report generation
- [x] HTML reports
- [x] Graph-based visualization
- [ ] Service management with systemd
- [ ] Dashboard for visualization
- [ ] Docker support

## Tech Stack

- Bash
- Linux
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
