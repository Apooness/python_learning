import time
import speedtest

test = speedtest.Speedtest()

def downloadspeed():
    speed = round(test.download() / 1_000_000 ,2)
    return str(speed) + " Mbps"

def uploadspeed():
    speed = round(test.upload() / 1_000_000 ,2)
    return str(speed) + " Mbps"

if __name__ == "__main__":
    print(f"Download = {downloadspeed()}")
    print(f"Upload = {uploadspeed()}")
    time.sleep(5)
