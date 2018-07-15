# import the necessary packages
from __future__ import print_function
from FPS import FPS
import numpy as np
from aruco import aruco
from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse
import time
import cv2

resolution = (640,640)

 # construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100,
	help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=1,
	help="Whether or not frames should be displayed")
args = vars(ap.parse_args())

time.sleep(2.0)
fps = FPS().start()

Ar=aruco(98)
Ar.start()
st=time.time()
num = 0
# loop over some frames...this time using the threaded stream
while Ar.stopped==False:
        time.sleep(.1)

 
fps.stop()
#print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
#print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
print (100/(time.time()-st))
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
