from colorDescriptor import ColorDescriptor
import argparse
import glob
import cv2

#Parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True, help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True, help = "Path to the directory where the computed index will be stored")
args = vars(ap.parse_args())

cd = ColorDescriptor((8,12,3))

#Open output index file for writing
output = open(args["index"], "w")

#Use glob to grab filepaths of images
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
    #Extract image ID and load to image itself
    imageID = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)
    
    #Describe image
    features = cd.describe(image)
    
    #Write features to file
    features = [str(f) for f in features]
    output.write("%s,%s\n" % (imageID, ",".join(features)))
    
output.close()