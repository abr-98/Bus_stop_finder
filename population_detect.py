import pandas as pd



def population(name):
    populate=[]
    population_class=[]
    df=pd.read_csv(name)
    print(len(df))
    l=len(df)
    i=0
    while i<l:
        if df.iloc[i]['Zone']=='Market' and df.iloc[i]['timelevel']==3:
            populate.append('dense')
            population_class.append('3')
        elif df.iloc[i]['Zone']=='Market' and df.iloc[i]['timelevel']==2:
            populate.append('dense')
            population_class.append('3')
        elif df.iloc[i]['Zone']=='Market' and df.iloc[i]['timelevel']==1:
            populate.append('sparse')
            population_class.append('1')
        elif df.iloc[i]['Zone']=='Market' and df.iloc[i]['timelevel']==4:
            populate.append('dense')
            population_class.append('3')
        elif df.iloc[i]['Zone']=='Highway' and df.iloc[i]['timelevel']==3:
            populate.append('medium')
            population_class.append('2')
        elif df.iloc[i]['Zone']=='Highway' and df.iloc[i]['timelevel']==2:
            populate.append('sparse')
            population_class.append('1')
        elif df.iloc[i]['Zone']=='Highway' and df.iloc[i]['timelevel']==1:
            populate.append('sparse')
            population_class.append('1')
        elif df.iloc[i]['Zone']=='Highway' and df.iloc[i]['timelevel']==4:
            populate.append('medium')
            population_class.append('2')
        elif df.iloc[i]['Zone']=='Normal city' and df.iloc[i]['timelevel']==3:
            populate.append('dense')
            population_class.append('3')
        elif df.iloc[i]['Zone']=='Normal city' and df.iloc[i]['timelevel']==2:
            populate.append('medium')
            population_class.append('2')
        elif df.iloc[i]['Zone']=='Market' and df.iloc[i]['timelevel']==1:
            populate.append('sparse')
            population_class.append('1') 
        else:
            populate.append('medium')
            population_class.append('2')
       # print("a")
        i+=1
    df['Population_density']=populate
    df['Population_class']=population_class
    print(len(populate))
    df.to_csv(name,index=False)

def main():
    name=["details_54feet_up.csv","details_ukhra_up.csv","details_8B_up.csv","details_azone_up.csv"]
    for i in name:
        population(i)

main()

