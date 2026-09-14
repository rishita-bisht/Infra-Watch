import sqlite3

conn = sqlite3.connect("metrics.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    cpu REAL,
    mem REAL,
    disk REAL
)
""")

conn.commit()
conn.close()
print("Database initialized")
