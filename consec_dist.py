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

def dec_zone(name,GROUND_TRUTH):
	#print(GROUND_TRUTH)
	zone=[]
	zone_class=[]
	l_market=[]
	l_nc=[]
	l_highway=[]
	df=pd.read_csv(name)
	if '54feet' in GROUND_TRUTH:
		Lat_market=23.5631833333 
		Long_market=87.28356
		Lat_nc=23.5440616667 
		Long_nc=87.2887366667
		Lat_high=23.4946766667 
		Long_high=87.3168283333
		l_market.append(get_spherical_distance(Lat_market,Lat_nc,Long_market,Long_nc))
		l_nc.append(get_spherical_distance(Lat_nc,Lat_high,Long_nc,Long_high))
		

		
		l=len(df)
		#print(l)
		i=0
		while i<l:
			#print("a ",i)
			Lat_a=df.iloc[i]['latitude']
			Long_a=df.iloc[i][' longitude']
			#if get_spherical_distance(Lat_a,Lat_market,Long_a,Long_market)+get_spherical_distance(Lat_a,Lat_nc,Long_a,Long_nc)==l_market:
			if get_spherical_distance(Lat_a,Lat_market,Long_a,Long_market)<l_market[0]:
				zone.append('Market')
				zone_class.append('1')
		#elif get_spherical_distance(Lat_a,Lat_nc,Long_a,Long_nc)+get_spherical_distance(Lat_a,Lat_high,Long_a,Long_high)==l_nc:
			elif get_spherical_distance(Lat_a,Lat_nc,Long_a,Long_nc)<l_nc[0]:
				zone.append('Normal city')
				zone_class.append('2')
			else:
				zone.append('Highway')
				zone_class.append('3')
			#print(len(zone))
			#print(zone)
			i+=1
	if 'azone' in GROUND_TRUTH:
		Lat_market=[23.5481833333]
		Long_market=[87.3024633333]
		Lat_nc=[23.564295,23.5074966667]
		Long_nc=[87.28288,87.3101183333]
		Lat_high=[23.5702466667,23.5355883333]
		Long_high=[87.3025383333,87.2982133333]
		Lat=23.494395
		Long=87.317125
		
		l_market.append(get_spherical_distance(Lat_market[0],Lat_high[1],Long_market[0],Long_high[1]))
		#l_market.append(get_spherical_distance(Lat_market[1],Lat_high[0],Long_market[1],Long_high[0]))
		l_nc.append(get_spherical_distance(Lat_nc[0],Lat_high[0],Long_nc[0],Long_high[0]))
		l_nc.append(get_spherical_distance(Lat_nc[1],Lat,Long_nc[1],Long))
		l_highway.append(get_spherical_distance(Lat_high[0],Lat_market[0],Long_high[0],Long_market[0]))
		l_highway.append(get_spherical_distance(Lat_high[1],Lat_nc[1],Long_high[1],Long_nc[1]))
		
		#df=pd.read_csv(name)
		l=len(df)
		#print(l)
		i=0
		while i<l:
			#print("a ",i)
			Lat_a=df.iloc[i]['latitude']
			Long_a=df.iloc[i][' longitude']
			#if get_spherical_distance(Lat_a,Lat_market,Long_a,Long_market)+get_spherical_distance(Lat_a,Lat_nc,Long_a,Long_nc)==l_market:
			if get_spherical_distance(Lat_a,Lat_market[0],Long_a,Long_market[0])<l_market[0]:
				zone.append('Market')
				zone_class.append('1')
		#elif get_spherical_distance(Lat_a,Lat_nc,Long_a,Long_nc)+get_spherical_distance(Lat_a,Lat_high,Long_a,Long_high)==l_nc:
			elif get_spherical_distance(Lat_a,Lat_nc[0],Long_a,Long_nc[0])<l_nc[0] or get_spherical_distance(Lat_a,Lat_nc[1],Long_a,Long_nc[1])<l_nc[1]:
				zone.append('Normal city')
				zone_class.append('2')
			else:
				zone.append('Highway')
				zone_class.append('3')
			#rint(len(zone))
			#print(zone)
			i+=1
	if 'ukhra' in GROUND_TRUTH:
		Lat_market=[23.56451,23.5887733333]
		Long_market=[87.2823233333,87.2085283333]
		Lat_nc=[23.6109329268,23.6407509281]
		Long_nc=[87.217555195,87.2265615539]
		Lat_high=[23.5505989912,23.6276064719]
		Long_high=[87.2686366159,87.2219748885]
		Lat=23.6523530924
		Long=87.2431245943
		
		l_market.append(get_spherical_distance(Lat_market[0],Lat_high[0],Long_market[0],Long_high[0]))
		l_market.append(get_spherical_distance(Lat_market[1],Lat_high[0],Long_market[1],Long_high[0]))
		l_nc.append(get_spherical_distance(Lat_nc[0],Lat_high[1],Long_nc[0],Long_high[1]))
		l_nc.append(get_spherical_distance(Lat_nc[1],Lat,Long_nc[1],Long))
		l_highway.append(get_spherical_distance(Lat_high[0],Lat_market[0],Long_high[0],Long_market[0]))
		l_highway.append(get_spherical_distance(Lat_high[1],Lat_nc[0],Long_high[1],Long_nc[0]))
		
		#df=pd.read_csv(name)
		l=len(df)
		#print(l)
		i=0
		while i<l:
			#print("a ",i)
			Lat_a=df.iloc[i]['latitude']
			Long_a=df.iloc[i][' longitude']
			#if get_spherical_distance(Lat_a,Lat_market,Long_a,Long_market)+get_spherical_distance(Lat_a,Lat_nc,Long_a,Long_nc)==l_market:
			if get_spherical_distance(Lat_a,Lat_market[0],Long_a,Long_market[0])<l_market[0] or get_spherical_distance(Lat_a,Lat_market[1],Long_a,Long_market[1])<l_market[1]:
				zone.append('Market')
				zone_class.append('1')
		#elif get_spherical_distance(Lat_a,Lat_nc,Long_a,Long_nc)+get_spherical_distance(Lat_a,Lat_high,Long_a,Long_high)==l_nc:
			elif get_spherical_distance(Lat_a,Lat_nc[0],Long_a,Long_nc[0])<l_nc[0] or get_spherical_distance(Lat_a,Lat_nc[1],Long_a,Long_nc[1])<l_nc[1]:
				zone.append('Normal city')
				zone_class.append('2')
			else:
				zone.append('Highway')
				zone_class.append('3')
			#print(len(zone))
			#print(zone)
			i+=1
	if '8B' in GROUND_TRUTH:
		Lat_market=[23.56451333,23.52723683,23.5158748,23.49778284]
		Long_market=[87.28308833,87.3419682,87.3548276,87.33484252]
		Lat_nc=[23.56451333,23.53399268,23.52339667]
		Long_nc=[87.28308833,87.34188019,87.33937167]
		Lat_high=[23.54631667,23.50425167]
		Long_high=[87.31860333,87.35286333]
		Lat=23.50697833
		Long=87.31082333
		
		l_market.append(get_spherical_distance(Lat_market[0],Lat_high[0],Long_market[0],Long_high[0]))
		l_market.append(get_spherical_distance(Lat_market[1],Lat_nc[2],Long_market[1],Long_nc[2]))
		l_market.append(get_spherical_distance(Lat_market[2],Lat_high[1],Long_market[2],Long_high[1]))
		l_market.append(get_spherical_distance(Lat_market[3],Lat,Long_market[3],Long))
		l_nc.append(get_spherical_distance(Lat_nc[0],Lat_market[0],Long_nc[0],Long_market[0]))
		l_nc.append(get_spherical_distance(Lat_nc[1],Lat_market[2],Long_nc[1],Long_market[2]))
		l_nc.append(get_spherical_distance(Lat_nc[2],Lat_market[2],Long_nc[2],Long_market[2]))
		l_highway.append(get_spherical_distance(Lat_high[0],Lat_nc[1],Long_high[0],Long_nc[1]))
		l_highway.append(get_spherical_distance(Lat_high[1],Lat_market[3],Long_high[1],Long_market[3]))
		
		#df=pd.read_csv(name)
		l=len(df)
		#print(l)
		i=0
		while i<l:
			#print("a ",i)
			Lat_a=df.iloc[i]['latitude']
			Long_a=df.iloc[i][' longitude']
			#if get_spherical_distance(Lat_a,Lat_market,Long_a,Long_market)+get_spherical_distance(Lat_a,Lat_nc,Long_a,Long_nc)==l_market:
			if get_spherical_distance(Lat_a,Lat_market[0],Long_a,Long_market[0])<l_market[0] or get_spherical_distance(Lat_a,Lat_market[1],Long_a,Long_market[1])<l_market[1] or get_spherical_distance(Lat_a,Lat_market[2],Long_a,Long_market[2])<l_market[2] or get_spherical_distance(Lat_a,Lat_market[3],Long_a,Long_market[3])<l_market[3]:
				zone.append('Market')
				zone_class.append('1')
		#elif get_spherical_distance(Lat_a,Lat_nc,Long_a,Long_nc)+get_spherical_distance(Lat_a,Lat_high,Long_a,Long_high)==l_nc:
			elif get_spherical_distance(Lat_a,Lat_nc[0],Long_a,Long_nc[0])<l_nc[0] or get_spherical_distance(Lat_a,Lat_nc[1],Long_a,Long_nc[1])<l_nc[1] or get_spherical_distance(Lat_a,Lat_nc[2],Long_a,Long_nc[2])<l_nc[2]:
				zone.append('Normal city')
				zone_class.append('2')
			else:
				zone.append('Highway')
				zone_class.append('3')
			#print(len(zone))
			#print(zone)
			i+=1
	#WSSprint(zone)
	#print(zone)
	#print(len(zone))
	df['Zone']=zone
	df['Zone_class']=zone_class
	df.to_csv(name,index=False)

def cal_dist(name,GROUND_TRUTH):
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
	#print(GROUND_TRUTH)
	dec_zone(name,GROUND_TRUTH)

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
 		cal_dist(bus_stop_file,GROUND_TRUTH)
 		#insert_time(bus_stop_file)
 		i+=1
main()