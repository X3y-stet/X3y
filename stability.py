import os
def check():
    # A simple way to check connection without pinging
    response = os.system("curl -s --head  --request GET https://google.com | grep '200 OK'")
    if response == 0:
        print("Stable")
    else:
        print("Unstable")
check()
