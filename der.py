from random import normalvariate as rnv
import numpy as np

def rule1(): #UPDATED!!! #funnel does not move
    simulation = 50
    mean = 0
    std = 1
    xposition = 0
    yposition = 0
    x1values = []
    sim1_values = []
    for i in range(simulation):
        ynoise = rnv(mean,std)
        xnoise = rnv(mean,std)
        yk = mean + yposition + ynoise
        xk = mean + xposition + xnoise
        sim1_values.append(yk)
        x1values.append(xk)
    Avg1 = (sum(sim1_values)/len(sim1_values))
    Var_sim1 = np.var(sim1_values)
    return (Avg1, Var_sim1)

test = rule1()
average = str(test[0])
variance = str(test[1])
print(average,'\n',variance)
print(type(average),'\n',type(variance))
#show_var = str(variance)
#print(show_avg[0:10])
#print(show_var[0:10])
