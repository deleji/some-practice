from colordescriptor import ColorDescriptor
import argparse
import glob
import cv2
import numpy as np

ap=argparse.ArgumentParser()
ap.add_argument('-d','--dataset',required=True,help='path to the \
                directory that contains the images to be indexed')
ap.add_argument('-i','--index',required=True,help='path to \
                where the computed index will be stored')
args=vars(ap.parse_args())
print args
cd=ColorDescriptor((8,12,3))
output=open(args['index'],'w')

for imagePath in glob.glob(args['dataset']+'\*.png'):
    imageID=imagePath[imagePath.rfind('t')+2:]
    image=cv2.imread(imagePath)
    features=cd.describe(image)
    features=[str(f) for f in features]
    output.write('%s,%s\n'%(imageID,','.join(features)))

output.close()
