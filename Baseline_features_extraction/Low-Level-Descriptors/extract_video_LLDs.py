#!/bin/python2
# python2 script
# Extract visual LLDs (FAU likelihoods) for video files of AVEC 2019
# Output: csv files

import os
import time
import numpy as np
from read_csv import load_features
from write_csv import save_features

# MODIFY HERE
folder_data   = '/media/richardt/2134-14F6/RichardT_Diss/'            # folder with video (.avi) files
folder_output = '/media/richardt/2134-14F6/Actual_Video/'  # output folder
exe_openface  = '/home/richardt/OpenFace/build/bin/FeatureExtraction'  # MODIFY this path to the folder of OpenFace (version 1.0.0): https://github.com/TadasBaltrusaitis/OpenFace

conf_openface = '-aus'  # Facial Action Units

if not os.path.exists(folder_output):
    os.mkdir(folder_output)

# Header for visual feature files (FAUs)
header_output_file = 'name;frameTime;confidence;AU01_r;AU02_r;AU04_r;AU05_r;AU06_r;AU07_r;AU09_r;AU10_r;AU12_r;AU14_r;AU15_r;AU17_r;AU20_r;AU23_r;AU25_r;AU26_r;AU45_r'  # 17 AU intensities

lostSessions =['9001','9002','9003']
outFiles = ['AC_9001.csv','AC_9002.csv','AC_9003.csv']

    
count=0
preText="AC"

for i in range(len(lostSessions)):
    session = lostSessions[i]
    outFile = outFiles[i]
    instname = outFile[:len(outFile)-4]
    print(instname)
    session_name = folder_data+'/'+session
    for fn in os.listdir(session_name):
        if fn.lower().endswith('.avi'):
             infilename  = os.path.join(session_name + '/'+fn)
             print(infilename)
             
#            os.rename(infilename, os.path.join(session_name+'/'+instname+'.avi'))
#             infilename = os.path.join(session_name+'/'+instname+'.avi')
             
            # if count==132:
            #     preText = "TS"
            # elif count == 264:
            #     preText = "TR"
            # elif count > 443:
            #     print("Complete")
            #     break
             
             
             #session_num = os.path.splitext(session)[0]
             #print(session_num)
             
             #print("INSTANCE NAME = "+ instname)
             #newfn = os.path.join(session_name+'/'+ preText+'_'+session_num+'.avi')
             #print("NEW FN = ",newfn)
             #os.rename(infilename,newfn)
             
             
             outfilename = folder_output + outFile
             openface_call = exe_openface + ' ' + conf_openface + ' -f ' + infilename + ' -out_dir ' + folder_output
             os.system(openface_call)
             time.sleep(0.03)
             
             print(outfilename)
             #Re-format files (as required by, e.g., openXBOW)
             features = load_features(outfilename, skip_header=True, skip_instname=False, delim=',')
             features = np.delete(features, [0,1,4,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39], 1)  # removing: frame, face_id, confidence, FAU present (c, 1/0)
             save_features(outfilename, features, append=False, instname=instname, header=header_output_file, delim=';', precision=3)
              
