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
import read_config
def accuracy(name):
    INPUT_FILE,OUTPUT_FOLDER,GROUND_TRUTH,DISTANCE_THRESHOLD,TIME_START,TIME_END,THRESHOLD, TRAIL_ID_RANGE,GROUND_TRUTH_THRESHOLD, FP_DISTANCE = read_config.read_config()
    df1=pd.read_csv('details_final.csv')
    print(name)
    df=df1[df1.Zone==name]
    model=Sequential()
#print(len(df))

#TRain
    X=df[['Zone','timelevel','count','cons_dist']].values
    X_d=pd.DataFrame(X)


    y=df['bs_predict'].values
    y_d=pd.DataFrame(y)
    y_d_2=pd.get_dummies(y_d)

    X_train, X_test, y_train, y_test = train_test_split(X_d,y_d,test_size=0.2,random_state=42)
#print(X_train)
    X_train_2=pd.get_dummies(X_train,columns=[0,1])
#X_train_2[1] = X_train_2[1].astype(float)
    X_train_2[2] = X_train_2[2].astype(float)
    X_train_2[3] = X_train_2[3].astype(float)
#y_train_2=pd.get_dummies(y_train)
    X_test_2=pd.get_dummies(X_test,columns=[0,1])
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
    model.add(Dropout(0.3))
    model.add(Dense(250, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.3))
    model.add(Dense(450, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.4))
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

    model.fit(X_train_2, y_train, epochs=550, callbacks=[early_stopping_monitor],batch_size=140)


#3
# evaluate the model
    scores = model.evaluate(X_test_2, y_test)
    scores_2 = model.evaluate(X_train_2, y_train)
#print(X_test)
#print(y_test)
#new_y_2=y_train[0].copy()
#new_y_d_2=pd.DataFrame(new_y_2)
#new_y=y_test[0].copy()
    #predictions=model.predict(X_test_2)
    print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
    print("\n%s: %.2f%%" % (model.metrics_names[1], scores_2[1]*100))

    #print(confusion_matrix(y_test,predictions))
    #print(classification_report(y_test,predictions))

#value_check=new_y.tolist()
#print(value_check)
#print(value_check)
    text=open('record_local.txt','a')
    text.write(str(name)+'\n')

    text.write("test="+str(scores[1]*100)+"\n")
    text.write("train="+str(scores_2[1]*100)+"\n")
    text.close()
#---------------------#
#new_y_d=pd.DataFrame(new_y)
#----------------------#
