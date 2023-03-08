import psutil
import time
import json

TRACKING_INTERVAL = 60

FILE_PATH = "tracking_data.json"

# Get the current active process
def track_website_usage():
    current_process = psutil.Process(psutil.Process().pid)
    current_process_name = current_process.name()

    # Check if current process is s web browser
    if current_process_name.startswith("chrome"):
        current_tab = current_process.memory_info().rss / (1024 ** 2)

        with open(FILE_PATH, ""r) as f: