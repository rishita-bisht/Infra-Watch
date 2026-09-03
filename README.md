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

## Project Structure

```
Infra-Watch/
├── collectors/
│   └── collector.sh
├── logs/
├── .gitignore
└── README.md
```

## Requirements

- Linux (tested on Kali Linux)
- Bash
- Standard Linux utilities:
  - `top`
  - `free`
  - `df`
  - `ps`
  - `ss`

## Getting Started

Clone the repository:

```bash
git clone https://github.com/rishita-bisht/Infra-Watch.git
cd Infra-Watch
```

Make the script executable:

```bash
chmod +x collectors/collector.sh
```

Run the collector:

```bash
./collectors/collector.sh
```

## Metrics Collected

| Metric | Source |
|---------|--------|
| CPU Usage | `top` |
| Memory Usage | `free` |
| Disk Usage | `df` |
| Load Average | `/proc/loadavg` |
| Top Processes | `ps` |
| Network Statistics | `ss` |

## Roadmap

- [x] System metrics collection
- [x] Load average monitoring
- [x] Process monitoring
- [x] Network statistics
- [ ] Threshold-based alerting
- [ ] Scheduled metric collection
- [ ] Log rotation
- [ ] Service management with systemd
- [ ] Dashboard for visualization
- [ ] Docker support

## Tech Stack

- Bash
- Linux
- Git

## Contributing

Contributions, suggestions, and improvements are welcome. Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
