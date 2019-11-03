import pandas as pd 
import numpy as np
from keras.models import Sequential 
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import to_categorical
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from keras.layers.normalization import BatchNormalization


df1=pd.read_csv('train_bus_1.csv')
df2=pd.read_csv('test_bus_1.csv')

model=Sequential()
#print(len(df))

#TRain
X_1=df1[['zone_class','time_level','next_stop_distance','total_waiting_time','wifi_count','honks','Population_class','rsi','week_class']].values
X1_train=pd.DataFrame(X_1)


y_1=df1[['bus_stop','latitude','longitude']].values
Y1_train_k=pd.DataFrame(y_1)
#y_d_2=pd.get_dummies(y_d)
Y_1=df1[['zone_class','time_level','next_stop_distance','total_waiting_time','wifi_count','honks','Population_class','rsi','week_class']].values
X1_test=pd.DataFrame(Y_1)


y_2=df1[['bus_stop','latitude','longitude']].values
Y1_test_k=pd.DataFrame(y_2)

#X_train, X_test, y_train_k, y_test_k = train_test_split(X_d,y_d,test_size=0.2,random_state=42)
#print(X_train)
y_train1=Y1_train_k[0].copy()
y_train=pd.DataFrame(y_train1)
y_test1=Y1_test_k[0].copy()
y_test=pd.DataFrame(y_test1)

#l=len(y_test_k)
#i=0
bs=Y1_test_k[0].copy()
bs_l=bs.tolist()
lat=Y1_test_k[1].copy()
lat_l=lat.tolist()

long=Y1_test_k[2].copy()
long_l=long.tolist()

z=X1_test[0].copy()
z_l=z.tolist()

t=X1_test[1].copy()
t_l=t.tolist()

n=X1_test[2].copy()
n_l=n.tolist()

tw=X1_test[3].copy()
tw_l=tw.tolist()

w=X1_test[4].copy()
w_l=w.tolist()

h=X1_test[5].copy()
h_l=h.tolist()

p=X1_test[6].copy()
p_l=p.tolist()

r=X1_test[7].copy()
r_l=r.tolist()

wc=X1_test[8].copy()
wc_l=wc.tolist()

X_train_2=pd.get_dummies(X1_train,columns=[0,1,6,8])
#X_train_2[1] = X_train_2[1].astype(float)

#y_train_2=pd.get_dummies(y_train)
X_test_2=pd.get_dummies(X1_test,columns=[0,1,6,8])
#X_test_2[1] = X_test_2[1].astype(float)

#y_test_2=pd.get_dummies(y_test)
#n_cols=X_train_2.shape[1]
n_cols=X_train_2.shape[1]
#y_test_2=pd.get_dummies(y_test)
n_cols=X_train_2.shape[1]
print(n_cols)
print(X_train_2)
model.add(Dense(200, activation='relu', input_shape=(n_cols,)))
model.add(BatchNormalization())
model.add(Dropout(0.2))
model.add(Dense(200, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.3))
model.add(Dense(250, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.3))
model.add(Dense(300, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.4))
model.add(Dense(350, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.4))
model.add(Dense(450, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(500, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(550, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))

model.add(Dense(650, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))

'''model.add(Dense(800, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))'''
model.add(Dense(700, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

early_stopping_monitor = EarlyStopping(patience=3)
#X_d_2=to_categorical(X_d)
#y_d_2=to_categorical(y_d)
from keras.optimizers import SGD
#sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(optimizer='RMSprop', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train_2, y_train, epochs=400, callbacks=[early_stopping_monitor],batch_size=100)


#3
# evaluate the model
scores = model.evaluate(X_test_2, y_test)
scores_2 = model.evaluate(X_train_2, y_train)
#print(X_test)
#print(y_test)
#new_y_2=y_train[0].copy()
#new_y_d_2=pd.DataFrame(new_y_2)
#new_y=y_test[0].copy()
predictions=model.predict(X_test_2)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
print("\n%s: %.2f%%" % (model.metrics_names[1], scores_2[1]*100))

text=open('total_accuracy','w')
text.write("test="+str(scores[1]*100)+"\n")
text.write("train="+str(scores_2[1]*100)+"\n")
text.close()

#value_check=new_y.tolist()
#print(value_check)
#print(value_check)

#---------------------#
#new_y_d=pd.DataFrame(new_y)
#----------------------#
prediction=[]
for x in predictions:
    #print(x)
    k_1=round(x[0])
    k_1_i=int(k_1)
    prediction.append(k_1_i)
    #k_1_s=str(k_1_i)
    #print(k_1_i)
#print(prediction)
actual=y_test.values.tolist()
given=[]
for i in actual:
    given.append(i[0])
#print(given)

text_fp=open('False_Positive_test.csv','w')
text_fp.write('latitude,longitude,zone_class,time_level,next_stop_distance,total_waiting_time,wifi_count,honks,Population_class,rsi,week_class,bus_stop\n')

text_fn=open('False_Negative_test.csv','w')
text_fn.write('latitude,longitude,zone_class,time_level,next_stop_distance,total_waiting_time,wifi_count,honks,Population_class,rsi,week_class,bus_stop\n')

text_tp=open('True_Positive_test.csv','w')
text_tp.write('latitude,longitude,zone_class,time_level,next_stop_distance,total_waiting_time,wifi_count,honks,Population_class,rsi,week_class,bus_stop\n')

text_tn=open('True_Negative_test.csv','w')
text_tn.write('latitude,longitude,zone_class,time_level,next_stop_distance,total_waiting_time,wifi_count,honks,Population_class,rsi,week_class,bus_stop\n')

l=len(y_test)
j=0

while j<l:
    if given[j]==1 and prediction[j]==0:
        text_fn.write(str(lat_l[j])+","+str(long_l[j])+","+str(z_l[j])+","+str(t_l[j])+","+str(n_l[j])+","+str(tw_l[j])+","+str(w_l[j])+","+str(h_l[j])+","+str(p_l[j])+","+str(r_l[j])+","+str(wc_l[j])+","+str(bs_l[j])+"\n")
    if given[j]==0 and prediction[j]==1:
        text_fp.write(str(lat_l[j])+","+str(long_l[j])+","+str(z_l[j])+","+str(t_l[j])+","+str(n_l[j])+","+str(tw_l[j])+","+str(w_l[j])+","+str(h_l[j])+","+str(p_l[j])+","+str(r_l[j])+","+str(wc_l[j])+","+str(bs_l[j])+"\n")
    if given[j]==1 and prediction[j]==1:
        text_tp.write(str(lat_l[j])+","+str(long_l[j])+","+str(z_l[j])+","+str(t_l[j])+","+str(n_l[j])+","+str(tw_l[j])+","+str(w_l[j])+","+str(h_l[j])+","+str(p_l[j])+","+str(r_l[j])+","+str(wc_l[j])+","+str(bs_l[j])+"\n")
    if given[j]==0 and prediction[j]==0:
        text_tn.write(str(lat_l[j])+","+str(long_l[j])+","+str(z_l[j])+","+str(t_l[j])+","+str(n_l[j])+","+str(tw_l[j])+","+str(w_l[j])+","+str(h_l[j])+","+str(p_l[j])+","+str(r_l[j])+","+str(wc_l[j])+","+str(bs_l[j])+"\n")
    j+=1

text_fn.close()
text_fp.close()
text_tp.close()
text_tn.close()


    