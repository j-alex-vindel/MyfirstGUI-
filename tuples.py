from random import normalvariate as rnv
import numpy as np
import statistics

def rule1(): #!!! #funnel does not move
    simulation = 10
    mean = 0
    std = 1
    xposition = 0
    yposition = 0
    zposition = 0
    xs = []
    ys = []
    zs = []
    for i in range(simulation):
        ynoise = rnv(mean,std)
        xnoise = rnv(mean,std)
        znoise = rnv(mean,std)
        yk = mean + yposition + ynoise
        xk = mean + xposition + xnoise
        zk = mean + zposition + znoise
        ys.append(yk)
        xs.append(xk)
        zs.append(zk)
    Avg1 = (sum(ys)/len(ys))
    Var1 = np.var(ys)
    dev = statistics.pstdev(ys)
    return (Avg1, Var1, xs, ys, zs, dev)

x = rule1()

prom = x[0]
varz = x[1]
xs = x[2]
ys = x[3]
zs = x[4]
y = np.array([xs,ys,zs])
show = np.std(y)
prom = np.mean(y)
vara = show**2
vare = show*show

print('STD: ',show,'\nAverage: ',prom,'\nVar: ',vara,'\n2vara: ',vare)
