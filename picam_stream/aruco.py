import numpy as np
import cv2
import math
import numpy as np
from threading import Thread
from piVideoStream import PiVideoStream
import time
class aruco:

   def __init__(self,aid,resolution=(640,640)):

      self.dictionary = (cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250))
      self.dist = np.zeros(2)
      self.resolution=np.asarray(resolution)
      self.centre=np.zeros(2)
      self.aruco_id=aid
      self.sec=np.zeros(2)
      self.stopped = False
   
   def find(self):
      num=0
      vs=PiVideoStream().start()
      time.sleep(5)
      while True:       
         img=vs.read()
         try:
            self.get_aruco(img)
            self.get_section(img)
            num=num+1
            print num
            if num==100:
               self.stopped=True
            if self.stopped==True:
               vs.stop()
               return
            
         except:
            pass
            #print 'not in'

   def start(self):
      
      Thread(target=self.find, args=()).start()
      return self
   

   def stop(self):
      self.stopped = True


   def section(self):
      return self.sec


   def check(self):
      
      print("dictionary",self.dictionary,type(self.dictionary))
      print("distance",self.dist,type(self.dist))
      print("resolution",self.resolution,type(self.resolution))
      print("centre",self.centre,type(self.centre))
      print("aruco",self.aruco_id,type(self.aruco_id))
      print("section",self.sec,type(self.sec))
    
   def get_aruco(self,img):
      
          corners,marker_ids,reject = cv2.aruco.detectMarkers(img,self.dictionary)
          if (marker_ids)>0:
             if self.aruco_id in marker_ids:
                  marker_ids=((marker_ids)[:,0]).tolist().index(self.aruco_id)
                  corners = np.asarray(corners)
                  corners=(corners[marker_ids][0,:])
                  self.centre=np.mean(corners,axis=0)
             else:
                  self.centre=[-1,-1]
          else:
              self.centre=[-1,-1]
          return


   def get_errors(self):
      
         self.dist[0]=self.resolution[0]-np.floor(self.centre[0])
         self.dist[1]=self.resolution[1]-np.floor(self.centre[1])
         print self.dist
         return


   def get_section(self,img):
      
         unitx=np.floor(self.resolution[0]/6)
         unity=np.floor(self.resolution[1]/6)

         self.sec[0] = np.ceil(self.centre[0] / unitx)
         self.sec[1] = np.ceil(self.centre[1] / unity)
         
         return

      
