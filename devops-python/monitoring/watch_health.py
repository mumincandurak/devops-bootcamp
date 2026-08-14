import requests
import time
from datetime import datetime

URL = "http://localhost:8000/health"
INTERVAL = 5

while True:
    try:
        r = requests.get(URL, timeout=3)
        status = "UP" if r.status_code == 200 else f"DEGRADED ({r.status_code})"
    except requests.exceptions.RequestException as e:
        status = f"DOWN ({e.__class__.__name__})"
    print(f"[{datetime.now().isoformat()}] {status}")
    time.sleep(INTERVAL)