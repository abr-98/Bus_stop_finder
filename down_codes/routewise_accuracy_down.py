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

def accuracy(name):
    df=pd.read_csv(name)

   
    model=Sequential()
#print(len(df))

#TRain
    X=df[['Zone','timelevel','count','cons_dist','Population_density']].values
    X_d=pd.DataFrame(X)


    y=df[['bs_predict','latitude','longitude']].values
    y_d=pd.DataFrame(y)
    y_d_2=pd.get_dummies(y_d)

    X_train, X_test, y_train_k, y_test_k = train_test_split(X_d,y_d,test_size=0.2,random_state=42)
#print(X_train)
    y_train1=y_train_k[0].copy()
    y_train=pd.DataFrame(y_train1)
    y_test1=y_test_k[0].copy()
    y_test=pd.DataFrame(y_test1)

#l=len(y_test_k)
#i=0
    lat=y_test_k[1].copy()
    lat_l=lat.tolist()

    long=y_test_k[2].copy()
    long_l=long.tolist()
    

    X_train_2=pd.get_dummies(X_train,columns=[0,1,4])
#X_train_2[1] = X_train_2[1].astype(float)
    X_train_2[2] = X_train_2[2].astype(float)
    X_train_2[3] = X_train_2[3].astype(float)
#y_train_2=pd.get_dummies(y_train)
    X_test_2=pd.get_dummies(X_test,columns=[0,1,4])
#X_test_2[1] = X_test_2[1].astype(float)
    X_test_2[2] = X_test_2[2].astype(float)
    X_test_2[3] = X_test_2[3].astype(float)
#y_test_2=pd.get_dummies(y_test)
    n_cols=X_train_2.shape[1]
    print(n_cols)
    print(X_train_2)

    model.add(Dense(200, activation='relu', input_shape=(n_cols,)))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
    model.add(Dense(250, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
    model.add(Dense(250, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.3))
    model.add(Dense(450, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.3))
    model.add(Dense(500, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.4))
    model.add(Dense(600, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.4))
    model.add(Dense(800, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.3))
    model.add(Dense(900, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.4))
    model.add(Dense(1, activation='sigmoid'))

    early_stopping_monitor = EarlyStopping(patience=3)
#X_d_2=to_categorical(X_d)
#y_d_2=to_categorical(y_d)
    from keras.optimizers import SGD
#sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(optimizer='RMSprop', loss='binary_crossentropy', metrics=['accuracy'])

    model.fit(X_train_2, y_train, epochs=550, callbacks=[early_stopping_monitor],batch_size=150)


#3
# evaluate the model
    scores = model.evaluate(X_test_2, y_test)
    scores_2 = model.evaluate(X_train_2, y_train)
#print(X_test)
#print(y_test)
#new_y_2=y_train[0].copy()
#new_y_d_2=pd.DataFrame(new_y_2)
    text_l=open('routewise_accuracy.txt','a')
    text_l.write(name+"\n")
#new_y=y_test[0].copy()
    predictions=model.predict(X_test_2)
    print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
    print("\n%s: %.2f%%" % (model.metrics_names[1], scores_2[1]*100))
#value_check=new_y.tolist()
    text_l.write('test='+str(scores[1]*100)+'\n')

    text_l.write('train='+str(scores_2[1]*100)+'\n')
#print(value_check)
#print(value_check)
    text_l.close()
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
    if '54feet' in name:
        fn='False_Negative_54feet.csv'
        fp='False_Positive_54feet.csv'
        tp='True_Positive_54feet.csv'
        tn='True_Negative_54feet.csv'
    if 'ukhra' in name:
        fn='False_Negative_ukhra.csv'
        fp='False_Positive_ukhra.csv'
        tp='True_Positive_ukhra.csv'
        tn='True_Negative_ukhra.csv'
    if 'azone' in name:
        fn='False_Negative_azone.csv'
        fp='False_Positive_azone.csv'
        tp='True_Positive_azone.csv'
        tn='True_Negative_azone.csv'
    if '8B' in name:
        fn='False_Negative_8B.csv'
        fp='False_Positive_8B.csv'
        tp='True_Positive_8B.csv'
        tn='True_Negative_8B.csv'

    text_fp=open(fp,'w')
    text_fp.write('latitude,longitude\n')

    text_fn=open(fn,'w')
    text_fn.write('latitude,longitude\n')

    text_tp=open(tp,'w')
    text_tp.write('latitude,longitude\n')

    text_tn=open(tn,'w')
    text_tn.write('latitude,longitude\n')

    l=len(y_test)
    j=0

    while j<l:
        if given[j]==1 and prediction[j]==0:
            text_fn.write(str(lat_l[j])+","+str(long_l[j])+"\n")
        if given[j]==0 and prediction[j]==1:
            text_fp.write(str(lat_l[j])+","+str(long_l[j])+"\n")
        if given[j]==1 and prediction[j]==1:
            text_tp.write(str(lat_l[j])+","+str(long_l[j])+"\n")
        if given[j]==0 and prediction[j]==0:
            text_tn.write(str(lat_l[j])+","+str(long_l[j])+"\n")
        j+=1

    text_fn.close()
    text_fp.close()
    text_tp.close()
    text_tn.close()


    