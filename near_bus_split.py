import pandas as pd
import csv

df=pd.read_csv('False_Positive_test1.csv')

lat1=[]
lat2=[]
z1=[]
z2=[]
t1=[]
t2=[]
nsd1=[]
nsd2=[]
twt1=[]
twt2=[]
wc1=[]
wc2=[]
h1=[]
h2=[]
pc1=[]
pc2=[]
rsi1=[]
rsi2=[]
week1=[]
week2=[]
bs_st1=[]
bs_st2=[]
pred1=[]
pred2=[]
long1=[]
long2=[]
sig1=[]
sig2=[]

for i in range(1,len(df)):
    if (df.iloc[i]['prediction_per'])>63:
        lat1.append(df.iloc[i]['latitude'])
        long1.append(df.iloc[i]['longitude'])
        z1.append(df.iloc[i]['zone_class'])
        t1.append(df.iloc[i]['time_level'])
        nsd1.append(df.iloc[i]['next_stop_distance'])
        twt1.append(df.iloc[i]['total_waiting_time'])
        wc1.append(df.iloc[i]['wifi_count'])
        h1.append(df.iloc[i]['honks'])
        pc1.append(df.iloc[i]['Population_class'])
        rsi1.append(df.iloc[i]['rsi'])
        week1.append(df.iloc[i]['week_class'])
        bs_st1.append(df.iloc[i]['bus_stop'])
        pred1.append(df.iloc[i]['prediction_per'])
        sig1.append(df.iloc[i]['Signal'])
    else:
        lat2.append(df.iloc[i]['latitude'])
        long2.append(df.iloc[i]['longitude'])
        z2.append(df.iloc[i]['zone_class'])
        t2.append(df.iloc[i]['time_level'])
        nsd2.append(df.iloc[i]['next_stop_distance'])
        twt2.append(df.iloc[i]['total_waiting_time'])
        wc2.append(df.iloc[i]['wifi_count'])
        h2.append(df.iloc[i]['honks'])
        pc2.append(df.iloc[i]['Population_class'])
        rsi2.append(df.iloc[i]['rsi'])
        week2.append(df.iloc[i]['week_class'])
        bs_st2.append(df.iloc[i]['bus_stop'])
        pred2.append(df.iloc[i]['prediction_per'])
        sig2.append(df.iloc[i]['Signal'])


text_fp=open('false_positive_over_60.csv','w')
text_fp.write('latitude,longitude,zone_class,time_level,next_stop_distance,total_waiting_time,wifi_count,honks,Population_class,rsi,week_class,bus_stop,prediction_per,Signal\n')

text_fn=open('false_positive_under_60.csv','w')
text_fn.write('latitude,longitude,zone_class,time_level,next_stop_distance,total_waiting_time,wifi_count,honks,Population_class,rsi,week_class,bus_stop,prediction_per,Signal\n')

for j in range(1,len(lat1)):
    text_fp.write(str(lat1[j])+","+str(long1[j])+","+str(z1[j])+","+str(t1[j])+","+str(nsd1[j])+","+str(twt1[j])+","+str(wc1[j])+","+str(h1[j])+","+str(pc1[j])+","+str(rsi1[j])+","+str(week1[j])+","+str(bs_st1[j])+","+str(pred1[j])+","+str(sig1)+"\n")
text_fp.close()

for j in range(1,len(lat2)):
    text_fn.write(str(lat2[j])+","+str(long2[j])+","+str(z2[j])+","+str(t2[j])+","+str(nsd2[j])+","+str(twt2[j])+","+str(wc2[j])+","+str(h2[j])+","+str(pc2[j])+","+str(rsi2[j])+","+str(week2[j])+","+str(bs_st2[j])+","+str(pred2[j])+","+str(sig2)+"\n")
text_fn.close()