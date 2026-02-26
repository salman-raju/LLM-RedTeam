import csv
import os
from datetime import datetime

LOG_FILE = "logs.csv"

def init_logger():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Timestamp",
                "Attack Type",
                "Prompt",
                "Response",
                "Label",
                "Score",
                "Vulnerability Type"
            ])

def log_result(attack_type, prompt, response, label, score, vuln_type):
    with open(LOG_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            attack_type,
            prompt,
            response,
            label,
            score,
            vuln_type
        ])