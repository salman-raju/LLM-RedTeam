import csv
import os
from datetime import datetime

LOG_FILE = "redteam_logs.csv"


def init_logger():
    """
    Creates CSV file with header if it doesn't exist.
    """
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "timestamp",
                "attack_type",
                "prompt",
                "response",
                "label"
            ])


def log_result(timestamp, attack_type, prompt, response, label):
    """
    Appends a result row to the CSV log file.
    """
    with open(LOG_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            timestamp,
            attack_type,
            prompt,
            response,
            label
        ])