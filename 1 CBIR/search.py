from colordescriptor import ColorDescriptor
from searcher import Searcher
import argparse, cv2
import numpy as np

ap=argparse.ArgumentParser()
ap.add_argument('-i','--index',required=True,help='path to where the computed index will be stored')
ap.add_argument('-q','--query',required=True,help='path to the query image')
ap.add_argument('-r','--result-path',required=True,help='path to the result path')
args=vars(ap.parse_args())
print args
cd=ColorDescriptor((8,12,3))
query=cv2.imread(args['query'])
features=cd.describe(query)

searther=Searcher(args['index'])
results=searther.search(features)

cv2.imshow("Query",query)

for (score,resultID) in results:
    result=cv2.imread(args['result_path']+"\\"+resultID)
    cv2.imshow('Result',result)
    cv2.waitKey(0)
