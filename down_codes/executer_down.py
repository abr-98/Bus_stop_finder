import os
import read_config_down
import csv
import pandas as pd
INPUT_FILE,OUTPUT_FOLDER,GROUND_TRUTH,DISTANCE_THRESHOLD,TIME_START,TIME_END,THRESHOLD, TRAIL_ID_RANGE,GROUND_TRUTH_THRESHOLD, FP_DISTANCE \
=read_config_down.read_config()
if os.path.exists("details_new"):
	os.system("rm -r details_new")
os.system("python clustering_down.py")
k="details/down_"
os.mkdir("details_new")
p=".txt_local_group_leader.csv"
r=".txt_local_group_leader.txt"
l=TRAIL_ID_RANGE
i=1
while i<l:
	if i==22 and '54feet' in GROUND_TRUTH:
 		i+=1
 		continue
	i_s=str(i)
	n=k+i_s+r
	cmd="cp "+n+" details_new/"
	#print(cmd)
	os.system(cmd)
	cmd="mv details_new/down_"+i_s+r+" "+"details_new/down_"+i_s+p
	#print(cmd)
	os.system(cmd)
	i+=1
os.system("python3 compare_gt_down.py")

if '54feet' in GROUND_TRUTH:
	if os.path.exists('details_54feet_down'):
		os.system("rm -r details_54feet_down")
	os.mkdir("details_54feet_down")
	text=open("details_54feet_down.csv",'w')
	text.write("latitude,longitude,time-stamp,count,trail_number,local_group_number,bs_predict,cons_dist,timelevel,Zone,Zone_class\n")
	text.close()

	cmd="mv details_new/* details_54feet_down"
	os.system(cmd)
	os.system("rm -r details_new")

if 'ukhra' in GROUND_TRUTH:
	if os.path.exists('details_ukhra_down'):
		os.system("rm -r details_ukhra_down")
	os.mkdir("details_ukhra_down")
	text=open("details_ukhra_down.csv",'w')
	text.write("latitude,longitude,time-stamp,count,trail_number,local_group_number,bs_predict,cons_dist,timelevel,Zone,Zone_class\n")
	text.close()

	cmd="mv details_new/* details_ukhra_down"
	os.system(cmd)
	os.system("rm -r details_new")
if '8B' in GROUND_TRUTH:
	if os.path.exists('details_8B_down'):
		os.system("rm -r details_8B_down")
	os.mkdir("details_8B_down")
	text=open("details_8B_down.csv",'w')
	text.write("latitude,longitude,time-stamp,count,trail_number,local_group_number,bs_predict,cons_dist,timelevel,Zone,Zone_class\n")
	text.close()

	cmd="mv details_new/* details_8B_down"
	os.system(cmd)
	os.system("rm -r details_new")
if 'azone' in GROUND_TRUTH:
	if os.path.exists('details_azone_down'):
		os.system("rm -r details_azone_down")
	os.mkdir("details_azone_down")
	text=open("details_azone_down.csv",'w')
	text.write("latitude,longitude,time-stamp,count,trail_number,local_group_number,bs_predict,cons_dist,timelevel,Zone,Zone_class\n")
	text.close()

	cmd="mv details_new/* details_azone_down"
	os.system(cmd)
	os.system("rm -r details_new")


name_54="details_54feet_down.csv"
name_8B="details_8B_down.csv"
name_a="details_azone_down.csv"
name_uk="details_ukhra_down.csv"

l=TRAIL_ID_RANGE
i=1
while i<l:
	#print(l)
	#print(i)
	if i==22 and '54feet' in GROUND_TRUTH:
 		i+=1
 		continue
	i_s=str(i)
	
	if '54feet' in GROUND_TRUTH:
		text=open("details_54feet_down.csv",'a')
		name1="details_54feet_down/down_"+i_s+p
		#print(name1)
		#df=pd.read_csv(name_54)
		df1=pd.read_csv(name1)
		l2=len(df1)
		j=0
		while j<l2:
			t=str(df1.iloc[j][0])+","+str(df1.iloc[j][1])+","+str(df1.iloc[j][2])+","+str(df1.iloc[j][3])+","+str(df1.iloc[j][4])+","+str(df1.iloc[j][5])+","+str(df1.iloc[j][6])+","+str(df1.iloc[j][7])+","+str(df1.iloc[j][8])+","+str(df1.iloc[j][9])+","+str(df1.iloc[j][10])+"\n"
			text.write(t)
			j+=1
		text.close()
		i+=1
			#	i_s=str(i)
		#pd.concat([df,df1],ignore_index=True)

		#df.to_csv(name_54)
	if 'azone' in GROUND_TRUTH:
		text=open("details_azone_down.csv",'a')
		name1="details_azone_down/down_"+i_s+p
		#print(name1)
		#df=pd.read_csv(name_54)
		df1=pd.read_csv(name1)
		l2=len(df1)
		j=0
		while j<l2:
			t=str(df1.iloc[j][0])+","+str(df1.iloc[j][1])+","+str(df1.iloc[j][2])+","+str(df1.iloc[j][3])+","+str(df1.iloc[j][4])+","+str(df1.iloc[j][5])+","+str(df1.iloc[j][6])+","+str(df1.iloc[j][7])+","+str(df1.iloc[j][8])+","+str(df1.iloc[j][9])+","+str(df1.iloc[j][10])+"\n"
			text.write(t)
			j+=1
		text.close()
		i+=1
	if '8B' in GROUND_TRUTH:
		text=open("details_8B_down.csv",'a')
		name1="details_8B_down/down_"+i_s+p
		#print(name1)
		#df=pd.read_csv(name_54)
		df1=pd.read_csv(name1)
		l2=len(df1)
		j=0
		while j<l2:
			t=str(df1.iloc[j][0])+","+str(df1.iloc[j][1])+","+str(df1.iloc[j][2])+","+str(df1.iloc[j][3])+","+str(df1.iloc[j][4])+","+str(df1.iloc[j][5])+","+str(df1.iloc[j][6])+","+str(df1.iloc[j][7])+","+str(df1.iloc[j][8])+","+str(df1.iloc[j][9])+","+str(df1.iloc[j][10])+"\n"
			text.write(t)
			j+=1
		text.close()
		i+=1
	if 'ukhra' in GROUND_TRUTH:
		text=open("details_ukhra_down.csv",'a')
		name1="details_ukhra_down/down_"+i_s+p
		#df=pd.read_csv(name_uk)
		df1=pd.read_csv(name1)
		l2=len(df1)
		j=0
		while j<l2:
			t=str(df1.iloc[j][0])+","+str(df1.iloc[j][1])+","+str(df1.iloc[j][2])+","+str(df1.iloc[j][3])+","+str(df1.iloc[j][4])+","+str(df1.iloc[j][5])+","+str(df1.iloc[j][6])+","+str(df1.iloc[j][7])+","+str(df1.iloc[j][8])+","+str(df1.iloc[j][9])+","+str(df1.iloc[j][10])+"\n"
			text.write(t)
			j+=1
		text.close()
		i+=1
		#i+=1
			#	i_s=str(i)
		#pd.concat([df,df1],ignore_index=True)

		#df.to_csv(name_uk)

		