from read_img import *
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
gender = ['Male', 'Female']
values=[4372,5047]
ax.bar(gender,values)
plt.show()

values, counts = np.unique(ages_f, return_counts=True)
print(counts)

val=values.tolist()
cnt=counts.tolist()

plt.plot(counts)
plt.xlabel('ages')
plt.ylabel('distribution')
plt.show()