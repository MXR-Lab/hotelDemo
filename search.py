from colorDescriptor import ColorDescriptor
from searcher import Searcher
from resizeImage import Resize
import argparse
import cv2

#Construct and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True, help = "Path to the computed indexes")
ap.add_argument("-q", "--query", required = True, help = "Path to query image")
ap.add_argument("-r", "--result-path", required = True, help = "Path to image dataset")
args = vars(ap.parse_args())

#Initialize image descriptor
cd = ColorDescriptor((8,12,3))

#Load query image and describe it
query = cv2.imread(args["query"])
features = cd.describe(query)

#Perform search
searcher = Searcher(args["index"])
results = searcher.search(features)

#Display query
(h, w) = query.shape[:2]
width = 800
r = width / float(w)
dim = (width, int(h * r))
resizeQuery = cv2.resize(query, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Query", resizeQuery)

#Loop over results
for(score, resultID) in results:
    #Load result image and display it
    result = cv2.imread(resultID)
    #resize = Resize(result, width=1280)
    #resize = cv2.resize(result, (640,640))\
    (h, w) = result.shape[:2]
    width = 800
    r = width / float(w)
    dim = (width, int(h * r))
    resize = cv2.resize(result, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("Result", resize)
    cv2.waitKey(0)