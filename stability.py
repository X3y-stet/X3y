import subprocess
import sys

def check():
    print("--- Alexandria Network Stability Check ---")
    # We use a list ['curl', ...] instead of a string to avoid 'shell=True' risks
    command = [
        "curl", "-s", "-o", "/dev/null", 
        "-w", "%{http_code}", 
        "--connect-timeout", "3", 
        "--max-time", "5", 
        "https://google.com"
    ]
    
    try:
        # This handles the timeout and captures the output safely
        result = subprocess.run(command, capture_output=True, text=True, timeout=10)
        
        if result.stdout == "200":
            print("SUCCESS: Connection is stable.")
        else:
            print(f"WARNING: Network reached but returned HTTP {result.stdout}")
            
    except subprocess.TimeoutExpired:
        print("ERROR: Connection timed out. Your WE LAN might be lagging.")
    except FileNotFoundError:
        print("ERROR: 'curl' not found. Please run 'pkg install curl' in Termux.")
    except Exception as e:
        print(f"ANOMALY: An unexpected error occurred: {e}")

if __name__ == "__main__":
    check()
