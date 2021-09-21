#!/bin/python2
# python2 script
# Extract acoustic LLDs (MFCC and eGeMAPS sets from openSMILE)
# Output: csv files

import os
import time

# MODIFY HERE
feature_type  = 'mfcc'       # 'mfcc' or 'egemaps'                                                   ********************************************Changed from mfcc
folder_data   = '/media/richardt/2134-14F6/RichardT_Diss/'  # folder with audio (.wav) files
exe_opensmile = '/home/richardt/opensmile/build/progsrc/smilextract/SMILExtract'  # MODIFY this path to the folder of the SMILExtract (version 2.3) executable
path_config   = '/home/richardt/opensmile/config/'              # MODIFY this path to the config folder of opensmile 2.3 - no POSIX here on cygwin (windows) **************changed from /mfcc/

if feature_type=='mfcc':
    folder_output = '/media/richardt/2134-14F6/'  # output folder
    conf_smileconf = path_config + 'mfcc/MFCC12_0_D_A.conf'  # MFCCs 0-12 with delta and acceleration coefficients
    opensmile_options = '-configfile ' + conf_smileconf + ' -appendcsv 0 -timestampcsv 1 -headercsv 1'  # options from standard_data_output_lldonly.conf.inc
    outputoption = '-csvoutput'  # options from standard_data_output_lldonly.conf.inc
elif feature_type=='egemaps':
    folder_output = '/media/richardt/2134-14F6/'  # output folder
    conf_smileconf = path_config + 'egemaps/v01a/eGeMAPSv01a.conf'  # eGeMAPS feature set
    opensmile_options = '-configfile ' + conf_smileconf + ' -appendcsvlld 0 -timestampcsvlld 1 -headercsvlld 1'  # options from standard_data_output.conf.inc
    outputoption = '-lldcsvoutput'  # options from standard_data_output.conf.inc
else:
    print('Error: Feature type ' + feature_type + ' unknown!')


if not os.path.exists(folder_output):
    os.mkdir(folder_output)

print(os.listdir(folder_data))

count=0
midCount=1
endCount =0

files = ['9001','9002','9003']

inst = ['AC_9001','AC_9002','AC_9003']



for session in range(len(files)):
    num = files[session]
    instname = inst[session]
    if num !=instname[3:]:
        break
    
    session_name = folder_data+'/'+num
    for fn in os.listdir(session_name):
        if fn.lower().endswith('.wav'):
             infilename  = session_name + '/'+fn
             
             #instname    = os.path.splitext(fn)[0]
             print("INSTANCE NAME = "+ instname)
             
             outfilename = folder_output + instname + '.csv'
             opensmile_call = exe_opensmile + ' ' + opensmile_options + ' -inputfile ' + infilename + ' ' + outputoption + ' ' + outfilename + ' -instname ' + instname + ' -output ?'  # (disabling htk output)
             os.system(opensmile_call)
             
             count = count + 1
             
             time.sleep(0.01)

if os.path.exists('smile.log'):
    os.remove('smile.log')
else:
    print("Smile Log Doesn't Exist")
