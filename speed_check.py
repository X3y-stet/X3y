import speedtest
def check_speed():
    print("Connecting to the fastest server...")
    st = speedtest.Speedtest()
    st.get_best_server()
    
    print("Testing Download...")
    dl = st.download() / 1_000_000
    
    print("Testing Upload...")
    ul = st.upload() / 1_000_000
    
    print(f"\nResults for your Alexandria connection:")
    print(f"Download: {dl:.2f} Mbps")
    print(f"Upload:   {ul:.2f} Mbps")

if __name__ == "__main__":
    check_speed()
