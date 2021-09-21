import os
import time
import numpy as np
from read_csv import load_features
from write_csv import save_features

# MODIFY HERE
sessions_folder   = '/media/richardt/EXTERNAL/MAHNOB-HCI/Sessions'            # folder with video (.avi) files
visFeat_folder = '/media/richardt/EXTERNAL/Train_Video/visual_features/'  # output folder
exe_openface  = '/home/richardt/OpenFace/build/bin/FeatureExtraction'  # MODIFY this path to the folder of OpenFace (version 1.0.0): https://github.com/TadasBaltrusaitis/OpenFace

traincount = 0
testcount = 0
devcount = 0

count=0
preText="DV"

nums = ['DV_656', 'DC_796', 'DV_806', 'DV_22', 'DV_672', 'DV_522', 'DV_2116', 'DV_922', 'DV_538', 'DV_792', 'DV_544', 'DV_2756', 'DV_2758', 'DV_2760', 'DV_2762', 'DV_2764', 'DV_2766', 'DV_2770', 'DV_1562', 'DV_1564', 'DV_1568', 'TR_1572', 'TR_1574', 'TR_1576', 'TR_1578', 'TR_1582', 'TR_1584', 'TR_1588', 'TR_1590', 'TR_1592', 'TR_1594', 'TR_1598', 'TR_1600', 'TR_2082', 'TS_2084', 'TS_2086', 'TS_2088']
['656', '796', '806', '22', '672', '522', '2116', '922', '538', '792', '544', '2756', '2758', '2760', '2762', '2764', '2766', '2770', '1562', '1564', '1568', '1572', '1574', '1576', '1578', '1582', '1584', '1588', '1590', '1592', '1594', '1598', '1600', '2082', '2084', '2086', '2088']

array = []

for fn in os.listdir(visFeat_folder):
     preText = fn[:2]
     session = fn[3:len(fn)-4]
     
     if preText == 'DV':
          devcount = devcount+1
     if preText == 'TR':
          traincount = traincount+1          
     if preText == 'TS':
          testcount = testcount+1
      
     state = False
     sesh_folder = os.path.join(sessions_folder+'/'+session)
     
     for f in os.listdir(sesh_folder):
          if f.lower().endswith('.avi'):
               state=True
               if "TR" in f or "DV" in f or "TS" in f:
                    print(f)
               else:
                    infile = sesh_folder+'/'+f
                    outfile = sesh_folder+'/'+fn[:len(fn)-4]+'.avi'
                    print(infile)
                    print(outfile)
                    os.rename(infile,outfile)
                    print("NAOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
     if state ==False:
          print("NO VIDEO FOUND FOR SESSION ",session)
          
    	 
     array.append(fn[:len(fn)-4]) 
    	 
print(array)
print(len(array))
print("Dev = ",devcount)
print("TRAIN = ",traincount)
print("TEST = ",testcount)

 
