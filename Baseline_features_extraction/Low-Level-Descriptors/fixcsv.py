import os
import time
import numpy as np
import csv
import pandas as pd
from collections import defaultdict
# MODIFY HERE
folder_output   = '/media/richardt/EXTERNAL/MAHNOB-HCI/Sessions'            # folder with video (.avi) files
folder_data = '/media/richardt/EXTERNAL/Train_Video/visual_features/'  # output folder
exe_openface  = '/home/richardt/OpenFace/build/bin/FeatureExtraction'  # MODIFY this path to the folder of OpenFace (version 1.0.0): https://github.com/TadasBaltrusaitis/OpenFace

trainCount = 0
testCount = 0
devCount = 0

count=0
array2 = []

for fn in os.listdir(folder_data):
     if count>=0:
            
            infilename  = os.path.join(folder_data+fn)
            
            
            df = pd.read_csv(infilename, sep=';')
            name = df['name'][0]
            csvName = name[1:len(name)-1]
            csvSessionNum = csvName.split('_')[1]
            
            preText = fn[:2]
            filename = "'"+fn[:len(fn)-4]+"'"
            print(preText)
            if preText=='TR':
                trainCount = trainCount+1
            if preText=='TS':
                testCount = testCount+1
            if preText=='DV':
                devCount = devCount+1                               
            print(csvName)
            print(filename)
            df = df.replace(to_replace=name,value=filename)
            print(df['name'])
            df.to_csv(infilename)
     count = count+1

print("TRAIN = ",trainCount)
print("TEST = ",testCount)
print("DEV = ",devCount)
