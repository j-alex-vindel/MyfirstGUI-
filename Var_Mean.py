from random import normalvariate as rnv
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
position = 0
val_sim = []
x_val = []
for i in range(500):
    noise = rnv(0,1)
    Yk = position + noise
    val_sim.append(Yk)
    x_val.append(position)
    avg = sum(val_sim) / len(val_sim)
    position = position - Yk

Total_avg = sum(val_sim) / len(val_sim)
Total_var = np.var(val_sim)
#print (val_sim)
#print (x_val)
print('Av:', Total_avg,'\n','Var:', Total_var)
#plt.plot(val_sim)
#plt.scatter(x_val,val_sim, color='green')
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.plot(val_sim, color='blue')
ax2.scatter(x_val,val_sim, color='green')


plt.show()
