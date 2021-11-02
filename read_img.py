import os

fldr = r'C:\Users\Admin\Desktop\New folder\New folder\UTKFaceNhap'

files=os.listdir(fldr)
print(int(files[0].split('_')[0]))
print(files[0])

import cv2
ages=[]
genders=[]
images=[]

for i, fle in enumerate(files):
  age=int(fle.split('_')[0])
  gender=int(fle.split('_')[1])
  total=fldr+'/'+fle
  image=cv2.imread(total)

  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  image= cv2.resize(image,(48,48))
  images.append(image)
#   if i % 1000 == 0:
#     print(i)

for fle in files:
  age=int(fle.split('_')[0])
  gender=int(fle.split('_')[1])
  ages.append(age)
  genders.append(gender)

#from google.colab.patches import cv2_imshow
import cv2
#cv2.imshow(images[50])

#print(ages[80])
#print(genders[80])

import numpy as np
images_f=np.array(images)
genders_f=np.array(genders)
ages_f=np.array(ages)

np.save(r'C:\Users\Admin\Desktop\New folder\New folder\Nhap\image.npy',images_f)
np.save(r'C:\Users\Admin\Desktop\New folder\New folder\Nhap\gender.npy',genders_f)
np.save(r'C:\Users\Admin\Desktop\New folder\New folder\Nhap\age.npy',ages_f)

values, counts = np.unique(genders_f, return_counts=True)
print(counts)