from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
import DBconnect
import time
import subprocess

camera = PiCamera()
pir = MotionSensor(4)
while True:
	if pir.motion_detected:
		filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpeg")
		camera.capture(filename)
		p = subprocess.Popen(["scp", filename, "pi@10.207.3.236:/home/pi/kuvat"])
		print("Motion detected!")
		DBconnect.connect()
	time.sleep(1)
