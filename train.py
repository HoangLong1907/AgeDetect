from labels import *
from model import *
from checkpoint import *

save = Model.fit(X_train,Y_train_2,batch_size=64,validation_data=(X_test,Y_test_2),epochs=100)
Model.save(r'C:\Users\Admin\Desktop\New folder\New folder\Age_sex_detection.h5')

Model.evaluate(X_test,Y_test_2)

pred=Model.predict(X_test)

pred[1]

i=0
Pred_l=[]
while(i<len(pred[0])):

  Pred_l.append(int(np.round(pred[0][i])))
  i+=1

from sklearn.metrics import confusion_matrix 

from sklearn.metrics import classification_report

report=classification_report(Y_test_2[0], Pred_l)

print(report)

results = confusion_matrix(Y_test_2[0], Pred_l)