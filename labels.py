from read_img import *
from plot import *

labels=[]

i=0
while i<len(ages):
  label=[]
  label.append([ages[i]])
  label.append([genders[i]])
  labels.append(label)
  i+=1

images_f_2=images_f/255
labels_f=np.array(labels)
images_f_2.shape

import tensorflow as tf
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test= train_test_split(images_f_2, labels_f,test_size=0.25)

Y_train[0:5]

Y_train_2=[Y_train[:,1],Y_train[:,0]]
Y_test_2=[Y_test[:,1],Y_test[:,0]]

Y_train_2[0][0:5]

Y_train_2[1][0:5]