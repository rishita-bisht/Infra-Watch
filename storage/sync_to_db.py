import sqlite3
import csv

CSV_FILE = "../logs/metrics.csv"
DB_FILE = "metrics.db"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Get the last timestamp already in DB
cursor.execute("SELECT MAX(timestamp) FROM metrics")
last_synced = cursor.fetchone()[0]

with open(CSV_FILE) as f:
    reader = csv.DictReader(f)
    new_rows = 0
    for row in reader:
        if last_synced is None or row["timestamp"] > last_synced:
            cursor.execute(
                "INSERT INTO metrics (timestamp, cpu, mem, disk) VALUES (?, ?, ?, ?)",
                (row["timestamp"], float(row["cpu"]), float(row["mem"]), float(row["disk"]))
            )
            new_rows += 1

conn.commit()
conn.close()
print(f"Synced {new_rows} new rows")
