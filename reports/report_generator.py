import csv
import matplotlib.pyplot as plt
from datetime import datetime

cpu_values = []
mem_values = []
disk_values = []
timestamps = []

with open('logs/metrics.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        timestamp, cpu, mem, disk = row
        timestamps.append(timestamp)
        cpu_values.append(float(cpu))
        mem_values.append(float(mem))
        disk_values.append(float(disk))

# Averages
avg_cpu = sum(cpu_values) / len(cpu_values)
avg_mem = sum(mem_values) / len(mem_values)
avg_disk = sum(disk_values) / len(disk_values)

# Peaks
max_cpu = max(cpu_values)
max_cpu_time = timestamps[cpu_values.index(max_cpu)]


with open('reports/report.txt', 'w') as f:
    f.write("=" * 40 + "\n")
    f.write("InfraWatch — System Metrics Report\n")
    f.write("=" * 40 + "\n")
    f.write(f"Total readings analyzed: {len(cpu_values)}\n\n")
    f.write(f"Average CPU Usage:  {avg_cpu:.1f}%\n")
    f.write(f"Average Mem Usage:  {avg_mem:.1f}%\n")
    f.write(f"Average Disk Usage: {avg_disk:.1f}%\n\n")
    f.write(f"Peak CPU: {max_cpu}% (at {max_cpu_time})\n")
    f.write("=" * 40 + "\n")

print("Report saved to reports/report.txt")


html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>InfraWatch Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background: #f4f4f4; }}
        h1 {{ color: #2c3e50; }}
        table {{ border-collapse: collapse; width: 60%; background: white; }}
        th, td {{ border: 1px solid #ddd; padding: 10px; text-align: left; }}
        th {{ background: #2c3e50; color: white; }}
        .peak {{ color: #c0392b; font-weight: bold; }}
    </style>
</head>
<body>
    <h1>InfraWatch — System Metrics Report</h1>
    <p>Total readings analyzed: {len(cpu_values)}</p>
    <table>
        <tr><th>Metric</th><th>Average</th></tr>
        <tr><td>CPU Usage</td><td>{avg_cpu:.1f}%</td></tr>
        <tr><td>Memory Usage</td><td>{avg_mem:.1f}%</td></tr>
        <tr><td>Disk Usage</td><td>{avg_disk:.1f}%</td></tr>
    </table>
    <p class="peak">Peak CPU: {max_cpu}% at {max_cpu_time}</p>
</body>
</html>
"""

with open('reports/report.html', 'w') as f:
    f.write(html_content)

print("HTML report saved to reports/report.html")

data = list(zip(timestamps, cpu_values, mem_values, disk_values))
data.sort(key=lambda x: x[0])

sorted_timestamps = [d[0] for d in data]
sorted_cpu = [d[1] for d in data]
sorted_mem = [d[2] for d in data]
sorted_disk = [d[3] for d in data]

# Timestamps ko actual datetime objects mein convert karo
dates = [datetime.fromisoformat(t) for t in sorted_timestamps]

plt.figure(figsize=(12, 6))
plt.plot(dates, sorted_cpu, label='CPU %', color='red')
plt.plot(dates, sorted_mem, label='Memory %', color='blue')
plt.plot(dates, sorted_disk, label='Disk %', color='green')

plt.xlabel('Time')
plt.ylabel('Usage %')
plt.title('InfraWatch — Metrics Over Time')
plt.legend()
plt.xticks(rotation=45, fontsize=8)
plt.tight_layout()

plt.savefig('reports/metrics_graph.png')
print("Graph saved to reports/metrics_graph.png")



