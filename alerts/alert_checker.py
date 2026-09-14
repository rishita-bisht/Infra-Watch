from dotenv import load_dotenv
import os
load_dotenv()
import requests
import time
import os

THRESHOLDS = {
    "cpu": 90,
    "mem": 90,
    "disk": 85
}

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

COOLDOWN_SECONDS = 1800  # 30 minutes
STATE_FILE = "alert_state.txt"

def get_latest_metrics(filepath):
    with open(filepath) as f:
        last_line = f.readlines()[-1].strip()
    
    timestamp, cpu, mem, disk = last_line.split(",")
    
    return {
        "timestamp": timestamp,
        "cpu": float(cpu),
        "mem": float(mem),
        "disk": float(disk)
    }

def check_thresholds(metrics):
    breaches = {}
    for key, limit in THRESHOLDS.items():
        if metrics[key] > limit:
            breaches[key] = f"{key.upper()} high: {metrics[key]}% (limit {limit}%)"
    return breaches

def send_slack_alert(message):
    payload = {"text": message}
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    return response.status_code == 200

def should_send_alert(alert_key):
    if not os.path.exists(STATE_FILE):
        return True
    with open(STATE_FILE) as f:
        state = dict(line.strip().split(",") for line in f if line.strip())
    last_time = float(state.get(alert_key, 0))
    return (time.time() - last_time) > COOLDOWN_SECONDS

def mark_alert_sent(alert_key):
    state = {}
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            state = dict(line.strip().split(",") for line in f if line.strip())
    state[alert_key] = str(time.time())
    with open(STATE_FILE, "w") as f:
        for k, v in state.items():
            f.write(f"{k},{v}\n")

if __name__ == "__main__":
    metrics = get_latest_metrics("../logs/metrics.csv")
    breaches = check_thresholds(metrics)

    if not breaches:
        print("All normal")
    else:
        for key, message in breaches.items():
            if should_send_alert(key):
                send_slack_alert(f"🚨 InfraWatch Alert:\n{message}")
                mark_alert_sent(key)
                print("Alert sent:", message)
            else:
                print("Skipped (cooldown active):", message)
