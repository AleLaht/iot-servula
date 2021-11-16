from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
import DBconnect
import time
import subprocess



camera = PiCamera()
pir = MotionSensor(4)
camera.vflip = True
while True:
	if pir.motion_detected:
		date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpeg")
		DBconnect.connect()
		camera.capture("kuvat/" + filename)
		p = subprocess.Popen(["scp", "kuvat/" + filename, "*USERNAME@IPADDRESS*:/var/www/html/kuvat"])
		print("Motion detected!")
	time.sleep(5)
