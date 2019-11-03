import pandas as pd
from sklearn.model_selection import train_test_split

df=pd.read_csv('feature.csv')


#TRain
X=df[['zone_class','time_level','next_stop_distance','total_waiting_time','wifi_count','honks','Population_class','rsi','week_class']].values
X_d=pd.DataFrame(X)
#X_d_2=pd.get_dummies(X_d)

y=df[['bus_stop','latitude','longitude']].values
y_d=pd.DataFrame(y)
#y_d_2=pd.get_dummies(y_d)

X_train, X_test, y_train, y_test = train_test_split(X_d,y_d,test_size=0.2,random_state=42)
X_train = pd.concat([X_train, y_train], axis=1,ignore_index=True)
X_test = pd.concat([X_test, y_test], axis=1,ignore_index=True)

#X_train.join(y_train)
#X_test.join(y_test)
X_train.columns = ['zone_class','time_level','next_stop_distance','total_waiting_time','wifi_count','honks','Population_class','rsi','week_class','bus_stop','latitude','longitude']

X_test.columns = ['zone_class','time_level','next_stop_distance','total_waiting_time','wifi_count','honks','Population_class','rsi','week_class','bus_stop','latitude','longitude']
X_train.to_csv('train_bus_1.csv')
X_test.to_csv('test_bus_1.csv')