import requests
import time
import random
import threading

OPENHAB_URL = "http://localhost:8080/rest/items/"
NUM_DEVICES = 30
INTERVAL = 0.2  # 200ms delay between updates

def simulate_device(device_id):
    item_name = f"Virtual_Stress_Sensor_{device_id}"
    while True:
        val = round(random.uniform(15.0, 35.0), 2)
        try:
            headers = {'Content-Type': 'text/plain'}
            response = requests.post(f"{OPENHAB_URL}{item_name}", data=str(val), headers=headers, timeout=2)
        except Exception as e:
            pass
        time.sleep(INTERVAL)

if __name__ == "__main__":
    print(f"Starting stress test: Simulating {NUM_DEVICES} devices with high rate updates...")
    threads = []
    for i in range(NUM_DEVICES):
        t = threading.Thread(target=simulate_device, args=(i,))
        t.daemon = True
        threads.append(t)
        t.start()
        
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stress testing stopped.")
