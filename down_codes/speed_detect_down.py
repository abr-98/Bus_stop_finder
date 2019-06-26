import pandas as pd



def speed_detect(name):
    speed=[6.94]
    df=pd.read_csv(name)
    print(len(df))
    l=len(df)
    i=1
    while i<l:

        time_prev=df.iloc[i-1]['time-stamp']
        time_now=df.iloc[i]['time-stamp']
        dist_prev=df.iloc[i-1]['cons_dist']
        dist_now=df.iloc[i]['cons_dist']

        hour_p,min_p,sec_p=time_prev.split(':')
        hour,min,sec=time_now.split(':')

        if abs(int(hour)-int(hour_p))>1:
                speed.append(6.94)

        else:
                time_total=(abs(int(hour)-int(hour_p)))*60+(abs(int(min)-int(min_p)))*60+abs((int(sec)-int(sec_p)))
                speed_ac=abs(float(dist_now)-float(dist_prev))/time_total
                speed.append(speed_ac)
       # print("a")
        i+=1
    df['Speed']=speed
    print(len(speed))
    df.to_csv(name,index=False)

def main():
    name=["details_54feet_down.csv","details_ukhra_down.csv","details_8B_down.csv","details_azone_down.csv"]
    for i in name:
        speed_detect(i)

main()

