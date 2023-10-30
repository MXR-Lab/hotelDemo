import numpy as np
import cv2
import imutils as util

class ColorDescriptor:
    def __init__(self, bins):
        #Store number of bins
        self.bins = bins
        
    def describe(self, image):
        #Convert image to HSV and initialize features
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        features = []
        
        #Grab dimensions and compute center of image
        (h, w) = image.shape[:2]
        (cX, cY) = (int(w * 0.5), int(h * 0.5))
        
        #Separate image into four quadrants
        segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h), (0, cX, cY, h)]
        
        #Construct elliptical mask for center of image
        (axesX, axesY) = (int(w * 0.75) // 2, int(h * 0.75 ) // 2)
        ellipMask = np.zeros(image.shape[:2], dtype = "uint8")
        cv2.ellipse(ellipMask, (cX, cY), (axesX, axesY), 0, 0, 360, 255, -1)
        
        #Loop through segments
        for (startX, endX, startY, endY) in segments:
            #Construct a mask for each quadrant minus center ellipse
            cornerMask = np.zeros(image.shape[:2], dtype = "uint8")
            cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)
            cornerMask = cv2.subtract(cornerMask, ellipMask)
            #Extract color histogram from image and update feature vector
            hist = self.histogram(image, cornerMask)
            features.extend(hist)
            
        #Extract color histogram from center and update feature vector
        hist = self.histogram(image, ellipMask)
        features.extend(hist)
        
        return features

    def histogram(self, image, mask):
            #Extract 3D color histogram from masked region using supplied number of bins
            hist = cv2.calcHist([image], [0,1,2], mask, self.bins, [0,180,0,256,0,256])
            
            #Normalize histogram
            if util.is_cv2():
                hist = cv2.normalize(hist).flatten()
            else:
                hist = cv2.normalize(hist, hist).flatten()
                
            return hist