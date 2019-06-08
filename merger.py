import os,csv,pandas as pd,glob

'''df=pd.concat(map(pd.read_csv,glob.glob(os.path.join('',"details*.csv"))))
'''
#os.system('python3 executer.py')
name='details_final.csv'
if os.path.exists(name):
	os.system("rm -r details_final.csv")

path=''
all_files=glob.glob(os.path.join(path,"details*.csv"))

df_from_each_file=(pd.read_csv(f)for f in all_files)
concatenated_df=pd.concat(df_from_each_file,ignore_index=True)

concatenated_df.to_csv(name,index=False)

