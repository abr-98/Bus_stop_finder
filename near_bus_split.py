import pandas as pd
import csv

df=pd.read_csv('False_Positive_test1.csv')

lat1=[]
lat2=[]
long1=[]
long2=[]

for i in range(1,len(df)):
    if (df.iloc[i]['prediction_per'])>68:
        lat1.append(df.iloc[i]['latitude'])
        long1.append(df.iloc[i]['longitude'])
    else:
        lat2.append(df.iloc[i]['latitude'])
        long2.append(df.iloc[i]['longitude'])


text_fp=open('false_positive_over_60.csv','w')
text_fp.write('latitude,longitude\n')

text_fn=open('false_positive_under_60.csv','w')
text_fn.write('latitude,longitude\n')

for j in range(1,len(lat1)):
    text_fp.write(str(lat1[j])+","+str(long1[j])+"\n")
text_fp.close()

for j in range(1,len(lat2)):
    text_fn.write(str(lat2[j])+","+str(long2[j])+"\n")
text_fn.close()