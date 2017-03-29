from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
import time

camera = PiCamera()
pir = MotionSensor(4)
while True:
	if pir.motion_detected:
		filename = datetime.now().strftime("%Y-%d-%m_%H.%M.%S.jpeg")
		camera.capture(filename)
		print("Motion detected!")
	time.sleep(1)
