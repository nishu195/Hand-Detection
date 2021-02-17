import cv2
import numpy as np
from imutils.video import VideoStream
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import subprocess, sys
import glob
tp=0
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)
hand_cascade = cv2.CascadeClassifier('hand.xml')#aufruf der model library für Handgestigerkennung

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array
	cv2.imshow("Gestig", image)#Vorschau Fenster der Handerkennung
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	hands = hand_cascade.detectMultiScale(image, 1.5, 2)#model zur Handgestig Erkennung
	contour = hands
	contour = np.array(contour)#counter formation
	if len(contour)>0:
		cap1 = cv2.VideoCapture(0)#usb kamera
		time.sleep(0.1)
		print(5)#timer zwischen Handerkennung und Aufnahme
		time.sleep(1)
		print(4)
		time.sleep(1)
		print(3)
		time.sleep(1)
		print(2)
		time.sleep(1)
		print(1)
		time.sleep(1)
		ret1,frame1 = cap1.read()#das Bild wird hier in frame1 variable gespeichert
		image_count = len(glob.glob1('./',"*.png"))
		tp=image_count
		name='Foto'+str(tp)+'.jpg'
		cv2.imwrite(name,frame1)#speichern des geschossenes Bildes
		cv2.imshow('aufnahme',frame1)#Vorschau Fenster der Aufnahme
		opener ="open" if sys.platform == "darwin" else "xdg-open"
		filename=name
		subprocess.call([opener, filename])
		break

	key = cv2.waitKey(1) & 0xFF
	rawCapture.truncate(0)
	if key == ord("q"):
		break
