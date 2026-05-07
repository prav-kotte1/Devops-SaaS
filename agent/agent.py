import requests
import psutil
import time

BACKEND_URL = "http://backend:8000/metrics"

while True:
    data = {
        "server_name": "local-machine",
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
    }

    try:
        response = requests.post(BACKEND_URL, json=data)
        print(response.json())
    except Exception as e:
        print(e)

    time.sleep(5)