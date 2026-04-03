import subprocess
import datetime
import os

# Target: Alexandria Optimization
SERVERS = {"Cloudflare": "1.1.1.1", "Google": "8.8.8.8"}
LOG_FILE = "stability.log"

def get_ping_stats(ip):
    # -c 5 (5 pings), -i 0.2 (Fast interval to keep antenna awake)
    cmd = ["ping", "-c", "5", "-i", "0.2", ip]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        # Extract mdev (jitter)
        stats = res.stdout.split("/")[-1].split(" ")[0]
        return float(stats)
    return 999.0

def main():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cf_jitter = get_ping_stats(SERVERS["Cloudflare"])
    
    status = f"[{timestamp}] CF Jitter: {cf_jitter}ms"
    
    # Auto-alert if jitter is high
    if cf_jitter > 20:
        status += " | ⚠️ HIGH JITTER"
        
    print(status)
    with open(LOG_FILE, "a") as f:
        f.write(status + "\n")

if __name__ == "__main__":
    main()
