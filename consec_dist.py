import csv
import pandas as pd
from lib import get_spherical_distance
import read_config
#s=df.iloc[i:i+1,0:2]
def insert_time(name):
	time_k=[]
	df=pd.read_csv(name)
	l=len(df)
	i=0
	while i<l:
		time_a=df.iloc[i][' time-stamp']
		time=str(time_a)
		t1,t2,t3=time.split(':')
		#print(t1)
		if int(t1)<9 and int(t2)<=59:
			time_k.append('1')
		elif int(t1)<13 and int(t2)<=59:
			time_k.append('2')
		elif int(t1)<17 and int(t2)<=59:
			time_k.append('3')
		else:
			time_k.append('4')
		i+=1
	#print(len(time_k))
	df['timelevel']=time_k
	df.to_csv(name,index=False)

def dec_zone(name):
	Lat_market=23.5631833333 
	Long_market=87.28356
	Lat_nc=23.5440616667 
	Long_nc=87.2887366667
	Lat_high=23.4946766667 
	Long_high=87.3168283333
	l_market=get_spherical_distance(Lat_market,Lat_nc,Long_market,Long_nc)
	l_nc=get_spherical_distance(Lat_nc,Lat_high,Long_nc,Long_high)
	zone=[]
	zone_class=[]

	df=pd.read_csv(name)
	l=len(df)
	i=0
	while i<l:
		Lat_a=df.iloc[i]['latitude']
		Long_a=df.iloc[i][' longitude']
		#if get_spherical_distance(Lat_a,Lat_market,Long_a,Long_market)+get_spherical_distance(Lat_a,Lat_nc,Long_a,Long_nc)==l_market:
		if get_spherical_distance(Lat_a,Lat_market,Long_a,Long_market)<l_market:
			zone.append('Market')
			zone_class.append('1')
		#elif get_spherical_distance(Lat_a,Lat_nc,Long_a,Long_nc)+get_spherical_distance(Lat_a,Lat_high,Long_a,Long_high)==l_nc:
		elif get_spherical_distance(Lat_a,Lat_nc,Long_a,Long_nc)<l_nc:
			zone.append('Normal city')
			zone_class.append('2')
		else:
			zone.append('Highway')
			zone_class.append('3')
		i+=1
	#WSSprint(zone)
	df['Zone']=zone
	df['Zone_class']=zone_class
	df.to_csv(name,index=False)

def cal_dist(name):
	distance=[150.453623567463]
	df=pd.read_csv(name)
	l=len(df)
	i=0
	while i+1<l:
		lat1=df.iloc[i]['latitude']
		long1=df.iloc[i][' longitude']
		lat2=df.iloc[i+1]['latitude']
		long2=df.iloc[i+1][' longitude']

		dist=get_spherical_distance(lat1,lat2,long1,long2)

		distance.append(dist)
		i+=1
	df['cons_dist']=distance
	df.to_csv(name,index=False)
	insert_time(name)
	dec_zone(name)

def main():
 	#ground_truth_file = "groundtruth/54feet.txt"
 	INPUT_FILE,OUTPUT_FOLDER,GROUND_TRUTH,DISTANCE_THRESHOLD,TIME_START,TIME_END,THRESHOLD, TRAIL_ID_RANGE,GROUND_TRUTH_THRESHOLD, FP_DISTANCE \
= read_config.read_config()
 	k="details_new/up_"
 	p=".txt_local_group_leader.csv"
 	l=TRAIL_ID_RANGE
 	i=1
 	while i<l:
 		if i==22 and '54feet' in GROUND_TRUTH:
 			i+=1
 			continue

 		i_s=str(i)

	 	bus_stop_file= k+i_s+p
	 	#print(i)
 		cal_dist(bus_stop_file)
 		#insert_time(bus_stop_file)
 		i+=1
main()