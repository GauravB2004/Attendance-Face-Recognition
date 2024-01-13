# attendance_recorder.py
import csv
import os
from datetime import datetime

def record_attendance(name, attendance_log_path):
    today = datetime.now().strftime("%Y-%m-%d")
    time_now = datetime.now().strftime("%H:%M:%S")
    file_exists = os.path.isfile(attendance_log_path)

    with open(attendance_log_path, 'a', newline='') as csvfile:
        fieldnames = ['Name', 'Date', 'Time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({'Name': name, 'Date': today, 'Time': time_now})
