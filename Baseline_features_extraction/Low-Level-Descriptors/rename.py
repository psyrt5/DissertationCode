import os
import time
import numpy as np
from read_csv import load_features
from write_csv import save_features

# MODIFY HERE
folder_data   = '/media/richardt/EXTERNAL/MAHNOB-HCI/Sessions'            # folder with video (.avi) files
folder_output = '/media/richardt/EXTERNAL/Train_Video/visual_features/'  # output folder
exe_openface  = '/home/richardt/OpenFace/build/bin/FeatureExtraction'  # MODIFY this path to the folder of OpenFace (version 1.0.0): https://github.com/TadasBaltrusaitis/OpenFace

traincount = 0
testcount = 0
devcount = 0

count=0
preText="DV"

for session in os.listdir(folder_data):
    session_name = folder_data+'/'+session
    print(session_name)
    for fn in os.listdir(session_name):
    	if fn.lower().endswith('.avis'):
             #print(str(os.path.splitext(fn)[0]).lower())
             if str(os.path.splitext(fn)[0].lower()).startswith('tr'):
                  traincount = traincount+1
                  print(os.path.splitext(fn)[0])
                  for f in os.listdir(folder_output):
                           if f.lower().endswith(session+'.csv'):
                                  print("match!")
                                  session_num = os.path.splitext(session)[0]
                                  #print(session_num)
                                  infilename  = os.path.join(folder_output + '/'+f)
                                  #print("INSTANCE NAME = "+ instname)
                                  newfn = os.path.join(session_name+'/TR_'+session_num+'.avi')
                                  #print("NEW FN = ",newfn)
                                  os.rename(infilename,newfn)
                  
             if str(os.path.splitext(fn)[0].lower()).startswith('ts'):
                  testcount = testcount+1
                  print(os.path.splitext(fn)[0])
                  for f in os.listdir(folder_output):
                           if f.lower().endswith(session+'.csv'):
                                  print("match!")
                                  session_num = os.path.splitext(session)[0]
                                  #print(session_num)
                                  infilename  = os.path.join(folder_output + '/'+f)
                                  #print("INSTANCE NAME = "+ instname)
                                  newfn = os.path.join(session_name+'/TS_'+session_num+'.avi')
                                  #print("NEW FN = ",newfn)
                                  os.rename(infilename,newfn)
                                  
             if str(os.path.splitext(fn)[0].lower()).startswith('dv'):
                  devcount = devcount+1
                  print(os.path.splitext(fn)[0])
                  for f in os.listdir(folder_output):
                           if f.lower().endswith(session+'.csv'):
                                  print("match!")
                                  session_num = os.path.splitext(session)[0]
                                  #print(session_num)
                                  infilename  = os.path.join(folder_output + '/'+f)
                                  #print("INSTANCE NAME = "+ instname)
                                  newfn = os.path.join(session_name+'/DV_'+session_num+'.csv')
                                  #print("NEW FN = ",newfn)
                                  os.rename(infilename,newfn)
                  
                  
                  
             infilename  = os.path.join(session_name + '/'+fn)
             
             if count==132:
                 preText = "TS"
             elif count == 264:
                 preText = "TR"
             elif count > 443:
                 #print("Complete")
                 break
             
             
             session_num = os.path.splitext(session)[0]
             #print(session_num)
             instname = preText+'_'+ session_num
             #print("INSTANCE NAME = "+ instname)
             newfn = os.path.join(session_name+'/'+ preText+'_'+session_num+'.avi')
             #print("NEW FN = ",newfn)
             #os.rename(infilename,newfn)
             
             
             count= count+1
             
             
print("train = ", traincount)
print("Test = ", testcount)
print("Dev = ", devcount)

