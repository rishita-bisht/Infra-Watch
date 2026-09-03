#!/bin/bash

TIMESTAMP=$(date +"%Y-%m-%dT%H:%M:%S")
CPU_IDLE=$(top -bn1 | grep "Cpu(s)" | awk -F',' '{print $4}' | awk '{print $1}')
CPU_USAGE=$(echo "100 - $CPU_IDLE" | bc)
MEM_USAGE=$(free -m | awk '/Mem:/ {printf "%.2f", ($3/$2)*100}')
DISK_USAGE=$(df -h / | tail -1 | awk '{print $5}' | sed 's/%//')

CSV_FILE="../logs/metrics.csv"

mkdir -p ../logs

# Add header only once
if [ ! -f "$CSV_FILE" ]; then
    echo "timestamp,cpu,mem,disk" > "$CSV_FILE"
fi

echo "$TIMESTAMP,$CPU_USAGE,$MEM_USAGE,$DISK_USAGE" >> "$CSV_FILE"

echo "Metrics saved to $CSV_FILE"
