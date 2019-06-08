import os
import sys
import pandas as pd
from read_config import read_config
from glob import glob
from lib import get_spherical_distance

INPUT_FILE,OUTPUT_FOLDER,GROUND_TRUTH,DISTANCE_THRESHOLD,TIME_START,TIME_END,THRESHOLD, TRAIL_ID_RANGE,GROUND_TRUTH_THRESHOLD, FP_DISTANCE = read_config()


l=TRAIL_ID_RANGE
i=0
#print(INPUT_FILE)
inp=INPUT_FILE+"/up_"
print(inp)
z=".txt"
check=[]
grd=[]
cnt=0
text=open(GROUND_TRUTH,'r')
f=text.readlines()
for j in f:
    lat1,long1=j.split(',')[:2]
    if lat1=='latitude' or lat1='Lat':
        continue
    k=[float(lat1),float(long1)]
    grd.append(k)

length=len(grd)
test=[]
for i in range(length):
    test.append(0)
s=1
while s<l:
    s_s=str(s)
    #print(inp+i_s)

    input_file=str(INPUT_FILE)+"/up_"+s_s+z
    print(input_file)
    if '54feet' in GROUND_TRUTH and s==22:
        s+=1
        continue
    df=pd.read_csv(input_file)
    p=len(df)
    j=0
    while j<p:

        check.append([float(df.iloc[j][0]),float(df.iloc[j][1])])
        j+=1
    s+=1

i=0
while i<length:
    for j in check:
        if get_spherical_distance(grd[i][0],j[0],grd[i][1],j[1])<10:
            test[i]=1
            
    i+=1

i=0
missing=[]
while i<length:
    if test[i]==0:
        cnt+=1
        missing.append(i)
    i+=1


text=open('record_local.txt','a')
text.write(GROUND_TRUTH+'\n')
text.write(str(cnt)+"\n")
for i in missing:
    text.write( str(i)+",")
text.write("\n")
text.close()





