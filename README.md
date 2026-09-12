# Infra-Watch

A lightweight Linux infrastructure monitoring tool built with Bash.

Infra-Watch collects essential system metrics from a Linux machine, stores them persistently, and automatically collects them on a scheduled interval.

## Features

- CPU utilization monitoring
- Memory utilization monitoring
- Disk utilization monitoring
- Persistent CSV-based metric storage
- Automatic metric collection using cron
- Timestamped metric history
- Load average monitoring
- Top 5 CPU-consuming processes
- Network statistics

## Project Structure

```text
Infra-Watch/
├── collectors/
│   └── collector.sh
├── logs/
│   ├── metrics.csv
│   └── cron.log
├── .gitignore
├── LICENSE
└── README.md
```

## Requirements

- Linux
- Bash
- `bc`
- Standard Linux utilities:
  - `top`
  - `free`
  - `df`
  - `ps`
  - `ss`
  - `cron`

## Getting Started

Clone the repository:

```bash
git clone https://github.com/rishita-bisht/Infra-Watch.git
cd Infra-Watch
```

Make the collector executable:

```bash
chmod +x collectors/collector.sh
```

Run the collector manually:

```bash
./collectors/collector.sh
```

## Metrics Collected

| Metric | Source |
|---|---|
| CPU Usage | `top -bn1` |
| Memory Usage | `free -m` |
| Disk Usage | `df -h /` |
| Load Average | `/proc/loadavg` |
| Top CPU Processes | `ps` |
| Network Statistics | `ss` |

## Data Storage

Collected metrics are stored in `logs/metrics.csv`.

Each execution appends a new timestamped row without overwriting previous data.

Example:

```csv
timestamp,cpu,mem,disk
2026-09-09T00:14:01,4.3,70.68,52
```

The CSV header is created automatically when the file does not already exist.

## Scheduling

Infra-Watch uses cron to run the collector automatically every 2 minutes.

Example cron entry:

```cron
*/2 * * * * /home/huiii/infrawatch/collectors/collector.sh >> /home/huiii/infrawatch/logs/cron.log 2>&1
```

This allows the system to collect metrics continuously without requiring manual execution.

## Lessons Learned

### Relative Paths and Cron

The collector initially used relative paths such as:

```text
../logs/metrics.csv
```

These worked when the script was executed manually from the `collectors` directory but failed when executed through cron.

Cron does not necessarily execute a script from the directory where the script is located.

The collector was therefore updated to use absolute paths for its output files, ensuring consistent behavior regardless of how the script is executed.

## Current Status

The monitoring pipeline currently supports:

- System metric collection
- Persistent metric storage
- Automated collection through cron

## Roadmap

- [x] System metrics collection
- [x] Persistent CSV storage
- [x] Automated collection with cron
- [ ] Threshold-based alerting
- [ ] Log rotation
- [ ] Service management with systemd
- [ ] Historical data analysis
- [ ] Dashboard and visualization
- [ ] Docker deployment

## Tech Stack

- Bash
- Linux
- Cron
- Git

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**Rishita Bisht**

[GitHub](https://github.com/rishita-bisht)





















