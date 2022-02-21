import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

xs =[6,4,5,7,8]
ys =[1,4,5,6,7]
zs =[6,4,5,4,6]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs,ys,zs, zdir='z')
plt.show()
