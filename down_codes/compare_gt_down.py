from lib import get_spherical_distance
import pandas as pd
import os
import read_config_down
'''def read_file(file_name):

    file_obj = open(file_name).readlines()[1:]
    if file_obj==None:
    	print("n")
    	return
    for i in xrange(len(file_obj)):
        if "\r" in file_obj[i]:
            file_obj[i] = file_obj[i].split("\r")[0]
        if "\n" in file_obj[i]:
            file_obj[i] = file_obj[i].split("\n")[0]
        file_obj[i] = file_obj[i].split(",")
    return file_obj

def write_file(file_name,header,data):

	file_obj = open(file_name,"w")
	file_obj.write(header+"\n")

	for line in data:
		line = [str(i) for i in line]
		line = ",".join(line)+"\n"
		file_obj.write(line)

	file_obj.close()
'''



def compare_ground_truth(ground_truth_file, bus_stop_file,GROUND_TRUTH_THRESHOLD):

	gt=[]
	bus_stops=[]
	text = open(ground_truth_file,"r")
	gt_1=text.readlines()[1:]
	for gt_point in gt_1:
		gt_point=gt_point.replace('\n','')
		k=gt_point.split(',')
		#print(k)
		#print('\n')
		for i in k:
			gt.append(float(i))

	#print(gt)
	#print('\n')

	text.close()
	text = open(bus_stop_file,"r")
	bus_stops_1=text.readlines()[1:]
	for gt_point in bus_stops_1:
		gt_point=gt_point.replace('\n','')
		k=gt_point.split(',')
		#print(k)
		#print('\n')
		cnt=0
		for i in k:
			if cnt!=2:
				bus_stops.append(float(i))
				cnt+=1
		#bus_stops.append(k)
	#print(bus_stops)
	text.close()
	#bus_stops = read_file()
	df=pd.read_csv(bus_stop_file)

	#print "GT: ",len(gt)
	#print "all bus_stops: ",len(bus_stops)
	#print gt[0]
	#print bus_stops[0]

	#detected  = []
	#false_negative=[]

	#gt_dict={}
	used=[]
	stop=[]
	l_gt=len(gt)
	l_bs=len(bus_stops)
	cnt_gt=0
	#for gt_point in gt:
	while cnt_gt<l_gt:
		#distances = []

		#min_point = None
		#min_dist = 100000000000000
		cnt_bs=0
		#for bs_point in bus_stops:
		while cnt_bs<l_bs:
			#pas
			#print("p")
			if bus_stops[cnt_bs] in used and bus_stops[cnt_bs+1] in used:
				#print("l")
				cnt_bs+=2
				continue

			lats1 , longs1 = gt[cnt_gt],gt[cnt_gt+1]
			lat1,long1=float(lats1),float(longs1)

			lats2, longs2 = bus_stops[cnt_bs],bus_stops[cnt_bs+1]
			lat2,long2=float(lats2),float(longs2)
			#print(lats1,",",longs1,",",lats2,",",longs2)
			#print(lat1,",",long1,",",lat2,",",long2)
			dist = get_spherical_distance(lat1,lat2,long1,long2)
			#print(dist)
			#the stoppage at the closest distance goes at the end of the list
			if dist< GROUND_TRUTH_THRESHOLD:
				#min_dist = dist
				#min_point = bs_point
				stop.append(cnt_bs/2)
				used.append(bus_stops[cnt_bs])
				used.append(bus_stops[cnt_bs+1])
				#print(used)
			#else:
			#	stop.append("0")
			cnt_bs+=2
			#print("b")
			#print(l_gt)
			#print(l_bs)
			#print(cnt_bs)
		cnt_gt+=2
		#print(cnt_gt)
		#print("a")
	#print("s")
	#print(len(stop))
	#print(stop)
	stop_ac=[]
	k=0
	while k<l_bs/2:
		stop_ac.append(0)
		#print(len(stop_ac))
		k+=1
	j=0
	while j<l_bs/2:
		#pass
		if j in stop:
			stop_ac[j]=1
		j+=1
	#print(stop_ac)
	df['bs_predict']=stop_ac
	#print(df)
	df.to_csv(bus_stop_file,index=False)
		#gt_dict[gt_point[0]]= points

	'''if min_dist < GROUND_TRUTH_THRESHOLD:
			detected.append([gt_point[0]]+min_point)
		else:
			false_negative.append(gt_point)


	false_positive = bus_stops[:]

	# for i in gt_dict:
	# 	gt_dict[i].sort()
	for i,j in gt_dict.items():
		print i,len(j)

	for gt_id,bs_stops in gt_dict.items():
		
		for point in bs_stops[:-1]:
			bus_stops.remove(point)



	# print "$ ",len(gt_dict)

	for gt_id,bs_stops in gt_dict.items():
		
		# print "#################"
		for point in bs_stops:
			# print "Deleting ",point
			# print gt_id,point
			false_positive.remove(point)


	##removing false positives who are within 100m distance of each other
	false_positive_copy = false_positive[:]

	for i in xrange(len(false_positive_copy)):
		for j in xrange(i+1, len(false_positive_copy)):

			lat1 , long1 = false_positive_copy[i][:2]
			lat2, long2 = false_positive_copy[j][:2]
			dist = get_spherical_distance(lat1,lat2,long1,long2)

			if dist< FP_DISTANCE:
				if false_positive_copy[j] in false_positive:
					print i,j,dist
					print "removing: ",false_positive_copy[j]
					false_positive.remove(false_positive_copy[j])


	print "effective bus_stops: ", len(bus_stops)



	print "detected ", len(detected)



	# for bs_point in bus_stops:

	# 	found = False

	# 	for detected_point in detected:

	# 		if bs_point[:2] == detected_point[1:3]:
	# 			found = True
	# 			break

	# 	if found == False:
	# 		false_positive.append(bs_point)


	print "FP: ",len(false_positive),"(",len(false_positive)*100.0/len(bus_stops),"%",")"
	print "FN: ", len(false_negative),"(",len(false_negative)*100.0/len(gt),"%",")"

	

	return detected, false_positive, false_negative
'''



def main():
	INPUT_FILE,OUTPUT_FOLDER,GROUND_TRUTH,DISTANCE_THRESHOLD,TIME_START,TIME_END,THRESHOLD, TRAIL_ID_RANGE,GROUND_TRUTH_THRESHOLD, FP_DISTANCE \
= read_config_down.read_config()
	#ground_truth_file = "groundtruth/54feet.txt"
	ground_truth_file=GROUND_TRUTH
	k="details_new/down_"
	p=".txt_local_group_leader.csv"
	l=TRAIL_ID_RANGE
	i=1
	while i<l:
 		if i==22 and '54feet' in GROUND_TRUTH:
 			i+=1
 			continue
 		i_s=str(i)

	 	bus_stop_file= k+i_s+p
 		compare_ground_truth(ground_truth_file,bus_stop_file,20)
 		i+=1
	os.system("python3 consec_dist_down.py")
main()


