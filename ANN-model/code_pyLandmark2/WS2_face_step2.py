import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

#----------------------------------------
csv_filename = 'faceLms.csv'
y_targets = ['normal','shock','smile'] #เรียงชื่อตามตัวอักษร
faceLms_model_filename = 'faceLms_model.h5'
#----------------------------------------

df = pd.read_csv(csv_filename)

print(df.head(8))
print(df.class_name.unique())

y,class_name = pd.factorize(df.class_name,sort=True)
print(class_name)
print(y)

x = df.drop('class_name',axis=1)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

y_train_1h = pd.get_dummies(y_train) # 1 hot format
y_test_1h = pd.get_dummies(y_test)
print(y_test_1h.head(20))
print(y_train_1h.shape)
print(y_test_1h.shape)

model = Sequential()

model.add(Dense(1024,activation='relu',input_shape=(936,)))
#model.add(Dense(512,activation='relu'))
model.add(Dense(3,activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer='AdaGrad',
              metrics=['accuracy'])

history = model.fit(x_train,y_train_1h,epochs=450,batch_size=8,verbose=1,validation_split=0.2)

df_hist = pd.DataFrame.from_dict(history.history)

print("Training Done")

df_hist['loss'].plot(style='b--',label='train')
df_hist['val_loss'].plot(style='r-',label='val')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.title('Loss')
plt.show()

df_hist['accuracy'].plot(style='b--',label='train')
df_hist['val_accuracy'].plot(style='r-',label='val')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend()
plt.title('Accuracy')
plt.show()

score = model.evaluate(x_test,y_test_1h,verbose=0)
print('test loss : ',score[0])
print('test accuracy : ',score[1])

model.save(faceLms_model_filename)

print(x_test.shape)
print(type(x_test))

y_pred = model.predict(x_test)
y_pred = np.argmax(y_pred,axis=1)

print(y_test)
print(y_pred)

print(confusion_matrix(y_test,y_pred))
print(accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))

ax = plt.subplot()
cm = confusion_matrix(y_test,y_pred)
sns.heatmap(cm,annot=True,ax=ax,cmap='coolwarm')

ax.set_xlabel('Predicted labels')
ax.set_ylabel('Actual labels')
ax.set_title('Confusion Matrix')
ax.xaxis.set_ticklabels(y_targets)
ax.yaxis.set_ticklabels(y_targets)
plt.show()        
