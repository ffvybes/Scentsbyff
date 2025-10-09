import requests
import sys
import time

def check_health(url="http://localhost:8080"):
    print("...Checking if website is up and running")
    time.sleep(2)
    try:
        r = requests.get(url)
        if r.status_code == 200:
            print("✅ Website is running successfully!")
        else:
            print(f"⚠ Website returned status code: {r.status_code}")
    except Exception as e:
        print(f"❌ Website check failed: {e}")
        sys.exit(1)

if _name_ == "_main_":
    check_health()