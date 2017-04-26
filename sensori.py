from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
from DBconnect import connect
import subprocess
import time


camera = PiCamera()
pir = MotionSensor(4)
while True:
	if pir.motion_detected:
		filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpeg")
		camera.capture(filename)
		p = subprocess.Popen(["scp", filename, "pi@10.207.3.236:/home/pi/kuvat"])
		print("Motion detected!")
	time.sleep(1)
