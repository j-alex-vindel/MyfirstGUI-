from random import normalvariate as rnv
import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import statistics

window = tk.Tk()
window.title('Funnel Project')
window.geometry('900x900')
# --- FUNCTIONS ---
def rule1(): #!!! #funnel does not move
    simulation = int(entry4.get())
    mean = float(entry2.get())
    std = float(entry3.get())
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

def rule1_display(): #shows the results1
    result1m = rule1()
    mean = result1m[0]
    vari = result1m[1]
    dev = result1m[5]
    xs = result1m[2]
    ys = result1m[3]
    zs = result1m[4]
    xy = np.array([xs,ys])
    xyz = np.array([xs,ys,zs])
    Avg_2d = np.mean(xy)
    dev_2d = np.std(xy)
    var_2d = np.var(xy)
    Avg_3d = np.mean(xyz)
    dev_3d = np.std(xyz)
    var_3d = np.var(xyz)
    # **** 1D ****
    result1m_display = tk.Text(master=window, height=1,width=11)
    result1m_display.grid(column=4, row=12)
    result1m_display.insert(tk.END, mean)
    result1v_display = tk.Text(master=window, height=1,width=11)
    result1v_display.grid(column=5, row=12)
    result1v_display.insert(tk.END, vari)
    resultstd_display = tk.Text(master=window, heigh=1,width=11)
    resultstd_display.grid(column=6, row=12)
    resultstd_display.insert(tk.END, dev)
    # **** 2D ****
    result2dm_display = tk.Text(master=window, height=1,width=11)
    result2dm_display.grid(column=4, row=18)
    result2dm_display.insert(tk.END, Avg_2d)
    result2dv_display = tk.Text(master=window, height=1,width=11)
    result2dv_display.grid(column=5, row=18)
    result2dv_display.insert(tk.END, dev_2d)
    result2dstd_display = tk.Text(master=window, heigh=1,width=11)
    result2dstd_display.grid(column=6, row=18)
    result2dstd_display.insert(tk.END, var_2d)
    # **** 3D ****
    result3dm_display = tk.Text(master=window, height=1,width=11)
    result3dm_display.grid(column=4, row=23)
    result3dm_display.insert(tk.END, Avg_3d)
    result3dv_display = tk.Text(master=window, height=1,width=11)
    result3dv_display.grid(column=5, row=23)
    result3dv_display.insert(tk.END, dev_3d)
    result3dstd_display = tk.Text(master=window, heigh=1,width=11)
    result3dstd_display.grid(column=6, row=23)
    result3dstd_display.insert(tk.END, var_3d)

    fig = plt.figure()
    ax1 = fig.add_subplot(212)
    ax2 = fig.add_subplot(221)
    ax3 = fig.add_subplot(222, projection='3d')
    ax1.plot(ys, color='blue')
    ax2.scatter(xs,ys, color='blue', s=5, marker='o')
    ax3.scatter(xs,ys,zs, color='blue', marker='o')
    ax1.axhline(y=0)
    ax1.set_xlabel('Rule 1')
    ax2.axhline(y=0)
    ax2.axvline(x=0)
    ax2.axis([-7, 7, -7, 7])
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Z')
    plt.show()

def rule2(): #!! #funnel moves (-yk)
    simulation = int(entry4.get())
    mean = float(entry2.get())
    std = float(entry3.get())
    yposition = 0
    xposition = 0
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
        yposition = yposition - yk
        xposition = xposition - xk
        zposition = zposition - zk
    Avg2 = (sum(ys)/len(ys))
    Var2 = np.var(ys)
    dev = statistics.pstdev(ys)
    return (Avg2,Var2, xs, ys, zs, dev)

def rule2_display(): #shows the results2
    result2m = rule2()
    mean = result2m[0]
    vari = result2m[1]
    dev = result2m[5]
    xs = result2m[2]
    ys = result2m[3]
    zs = result2m[4]
    xy = np.array([xs,ys])
    xyz = np.array([xs,ys,zs])
    Avg_2d = np.mean(xy)
    dev_2d = np.std(xy)
    var_2d = np.var(xy)
    Avg_3d = np.mean(xyz)
    dev_3d = np.std(xyz)
    var_3d = np.var(xyz)

    result2m_display = tk.Text(master=window, height=1,width=11)
    result2m_display.grid(column=4, row=13)
    result2m_display.insert(tk.END, mean)
    result2v_display = tk.Text(master=window, height=1,width=11)
    result2v_display.grid(column=5, row=13)
    result2v_display.insert(tk.END, vari)
    resultstd_display = tk.Text(master=window, heigh=1,width=11)
    resultstd_display.grid(column=6, row=13)
    resultstd_display.insert(tk.END, dev)
    # **** 2D ****
    result2dm_display = tk.Text(master=window, height=1,width=11)
    result2dm_display.grid(column=4, row=19)
    result2dm_display.insert(tk.END, Avg_2d)
    result2dv_display = tk.Text(master=window, height=1,width=11)
    result2dv_display.grid(column=5, row=19)
    result2dv_display.insert(tk.END, dev_2d)
    result2dstd_display = tk.Text(master=window, heigh=1,width=11)
    result2dstd_display.grid(column=6, row=19)
    result2dstd_display.insert(tk.END, var_2d)
    # **** 3D ****
    result3dm_display = tk.Text(master=window, height=1,width=11)
    result3dm_display.grid(column=4, row=24)
    result3dm_display.insert(tk.END, Avg_3d)
    result3dv_display = tk.Text(master=window, height=1,width=11)
    result3dv_display.grid(column=5, row=24)
    result3dv_display.insert(tk.END, dev_3d)
    result3dstd_display = tk.Text(master=window, heigh=1,width=11)
    result3dstd_display.grid(column=6, row=24)
    result3dstd_display.insert(tk.END, var_3d)

    fig = plt.figure()
    ax1 = fig.add_subplot(212)
    ax2 = fig.add_subplot(221)
    ax3 = fig.add_subplot(222, projection='3d')
    ax1.plot(ys, color='green')
    ax2.scatter(xs,ys, color='green', s=5, marker='o')
    ax3.scatter(xs,ys,zs, color='green', marker='o')
    ax1.axhline(y=0)
    ax1.set_xlabel('Rule 2')
    ax2.axhline(y=0)
    ax2.axvline(x=0)
    ax2.axis([-7, 7, -7, 7])
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Z')
    plt.show()

def rule3(): # UPDATED!! #funnel moves from target minus yk
    simulation = int(entry4.get())
    mean = float(entry2.get())
    std = float(entry3.get())
    sposition = 0
    fyposition = 0
    fxposition = 0
    fzposition = 0
    xs = []
    ys = []
    zs = []
    for i in range(simulation):
        ynoise = rnv(mean,std)
        xnoise = rnv(mean, std)
        znoise = rnv(mean, std)
        yk = mean + (sposition + fyposition) + ynoise
        xk = mean + (sposition + fxposition) + xnoise
        zk = mean + (sposition + fzposition) + znoise
        ys.append(yk)
        xs.append(xk)
        zs.append(zk)
        fyposition = sposition - yk
        fxposition = sposition - xk
        fzposition = sposition - zk
    Avg3 = (sum(ys)/len(ys))
    Var3 = np.var(ys)
    dev = statistics.pstdev(ys)
    return (Avg3,Var3, xs, ys, zs, dev)

def rule3_display(): #shows the results3
    result3m = rule3()
    mean = result3m[0]
    vari = result3m[1]
    dev = result3m[5]
    xs = result3m[2]
    ys = result3m[3]
    zs = result3m[4]
    xy = np.array([xs,ys])
    xyz = np.array([xs,ys,zs])
    Avg_2d = np.mean(xy)
    dev_2d = np.std(xy)
    var_2d = np.var(xy)
    Avg_3d = np.mean(xyz)
    dev_3d = np.std(xyz)
    var_3d = np.var(xyz)

    result3m_display = tk.Text(master=window, height=1,width=11)
    result3m_display.grid(column=4, row=14)
    result3m_display.insert(tk.END, mean)
    result3v_display = tk.Text(master=window, height=1,width=11)
    result3v_display.grid(column=5, row=14)
    result3v_display.insert(tk.END, vari)
    resultstd_display = tk.Text(master=window, heigh=1,width=11)
    resultstd_display.grid(column=6, row=14)
    resultstd_display.insert(tk.END, dev)
    # **** 2D ****
    result2dm_display = tk.Text(master=window, height=1,width=11)
    result2dm_display.grid(column=4, row=20)
    result2dm_display.insert(tk.END, Avg_2d)
    result2dv_display = tk.Text(master=window, height=1,width=11)
    result2dv_display.grid(column=5, row=20)
    result2dv_display.insert(tk.END, dev_2d)
    result2dstd_display = tk.Text(master=window, heigh=1,width=11)
    result2dstd_display.grid(column=6, row=20)
    result2dstd_display.insert(tk.END, var_2d)
    # **** 3D ****
    result3dm_display = tk.Text(master=window, height=1,width=11)
    result3dm_display.grid(column=4, row=25)
    result3dm_display.insert(tk.END, Avg_3d)
    result3dv_display = tk.Text(master=window, height=1,width=11)
    result3dv_display.grid(column=5, row=25)
    result3dv_display.insert(tk.END, dev_3d)
    result3dstd_display = tk.Text(master=window, heigh=1,width=11)
    result3dstd_display.grid(column=6, row=25)
    result3dstd_display.insert(tk.END, var_3d)

    fig = plt.figure()
    ax1 = fig.add_subplot(212)
    ax2 = fig.add_subplot(221)
    ax3 = fig.add_subplot(222, projection='3d')
    ax1.plot(ys, color='pink')
    ax2.scatter(xs,ys, color='pink', s=5, marker='o')
    ax3.scatter(xs,ys,zs, color='pink', marker='o')
    ax1.axhline(y=0)
    ax1.set_xlabel('Rule 3')
    ax2.axhline(y=0)
    ax2.axvline(x=0)
    ax2.axis([-7, 7, -7, 7])
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Z')
    plt.show()

def rule4(): #UPDATED! #funnel moves to (yk-1)
    simulation = int(entry4.get())
    mean = float(entry2.get())
    std = float(entry3.get())
    yposition = 0
    xposition = 0
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
        yposition = yk
        xposition = xk
        zposition = zk
    Avg4 = (sum(ys)/len(ys))
    Var4 = np.var(ys)
    dev = statistics.pstdev(ys)
    return (Avg4, Var4, xs, ys, xs, dev)

def rule4_display(): #shows the results4
    result4m = rule4()
    mean = result4m[0]
    vari = result4m[1]
    dev = result4m[5]
    xs = result4m[2]
    ys = result4m[3]
    zs = result4m[4]
    xy = np.array([xs,ys])
    xyz = np.array([xs,ys,zs])
    Avg_2d = np.mean(xy)
    dev_2d = np.std(xy)
    var_2d = np.var(xy)
    Avg_3d = np.mean(xyz)
    dev_3d = np.std(xyz)
    var_3d = np.var(xyz)

    result4m_display = tk.Text(master=window, height=1,width=11)
    result4m_display.grid(column=4, row=15)
    result4m_display.insert(tk.END, mean)
    result4v_display =tk.Text(master=window, height=1,width=11)
    result4v_display.grid(column=5, row=15)
    result4v_display.insert(tk.END, vari)
    resultstd_display = tk.Text(master=window, heigh=1,width=11)
    resultstd_display.grid(column=6, row=15)
    resultstd_display.insert(tk.END, dev)
    # **** 2D ****
    result2dm_display = tk.Text(master=window, height=1,width=11)
    result2dm_display.grid(column=4, row=21)
    result2dm_display.insert(tk.END, Avg_2d)
    result2dv_display = tk.Text(master=window, height=1,width=11)
    result2dv_display.grid(column=5, row=21)
    result2dv_display.insert(tk.END, dev_2d)
    result2dstd_display = tk.Text(master=window, heigh=1,width=11)
    result2dstd_display.grid(column=6, row=21)
    result2dstd_display.insert(tk.END, var_2d)
    # **** 3D ****
    result3dm_display = tk.Text(master=window, height=1,width=11)
    result3dm_display.grid(column=4, row=26)
    result3dm_display.insert(tk.END, Avg_3d)
    result3dv_display = tk.Text(master=window, height=1,width=11)
    result3dv_display.grid(column=5, row=26)
    result3dv_display.insert(tk.END, dev_3d)
    result3dstd_display = tk.Text(master=window, heigh=1,width=11)
    result3dstd_display.grid(column=6, row=26)
    result3dstd_display.insert(tk.END, var_3d)

    fig = plt.figure()
    ax1 = fig.add_subplot(212)
    ax2 = fig.add_subplot(221)
    ax3 = fig.add_subplot(222, projection='3d')
    ax1.plot(ys, color='purple')
    ax2.scatter(xs,ys, color='purple', s=5, marker='o')
    ax3.scatter(xs,ys,zs, color='purple', marker='o')
    ax1.axhline(y=0)
    ax1.set_xlabel('Rule 4')
    ax2.axhline(y=0)
    ax2.axvline(x=0)
    ax2.axis([-7, 7, -7, 7])
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Z')
    plt.show()

# *** Scenario 2 ***

def rule12(): #!!! #funnel does not move
    simulation = int(entry4.get())
    mean = float(entry2.get())
    std = float(entry3.get())
    amean = float(entry5.get())
    astd = float(entry6.get())
    phi = float(entry7.get())
    xposition = 0
    yposition = 0
    zposition = 0
    nkx = xposition
    nky = yposition
    nkz = zposition
    xs = []
    ys = []
    zs = []
    for i in range(simulation):
        ynoise = rnv(mean,std)
        xnoise = rnv(mean,std)
        znoise = rnv(mean,std)
        aky = rnv(amean,astd)
        akx = rnv(amean,astd)
        akz = rnv(amean,astd)
        nkx = phi*nkx + akx
        nky = phi*nky + aky
        nkz = phi*nkz + akz
        yk = mean + nky + yposition + ynoise
        xk = mean + nkx + xposition + xnoise
        zk = mean + nkz + zposition + znoise
        ys.append(yk)
        xs.append(xk)
        zs.append(zk)

    Avg1 = (sum(ys)/len(ys))
    Var1 = np.var(ys)
    dev = statistics.pstdev(ys)
    return (Avg1, Var1, xs, ys, zs, dev)

def rule12_display(): #shows the results1
    result1m = rule12()
    mean = result1m[0]
    vari = result1m[1]
    dev = result1m[5]
    xs = result1m[2]
    ys = result1m[3]
    zs = result1m[4]
    xy = np.array([xs,ys])
    xyz = np.array([xs,ys,zs])
    Avg_2d = np.mean(xy)
    dev_2d = np.std(xy)
    var_2d = np.var(xy)
    Avg_3d = np.mean(xyz)
    dev_3d = np.std(xyz)
    var_3d = np.var(xyz)

    result1m_display = tk.Text(master=window, height=1,width=11)
    result1m_display.grid(column=8, row=12)
    result1m_display.insert(tk.END, mean)
    result1v_display = tk.Text(master=window, height=1,width=11)
    result1v_display.grid(column=9, row=12)
    result1v_display.insert(tk.END, vari)
    resultstd_display = tk.Text(master=window, heigh=1,width=11)
    resultstd_display.grid(column=10, row=12)
    resultstd_display.insert(tk.END, dev)
    # **** 2D ****
    result2dm_display = tk.Text(master=window, height=1,width=11)
    result2dm_display.grid(column=8, row=18)
    result2dm_display.insert(tk.END, Avg_2d)
    result2dv_display = tk.Text(master=window, height=1,width=11)
    result2dv_display.grid(column=9, row=18)
    result2dv_display.insert(tk.END, dev_2d)
    result2dstd_display = tk.Text(master=window, heigh=1,width=11)
    result2dstd_display.grid(column=10, row=18)
    result2dstd_display.insert(tk.END, var_2d)
    # **** 3D ****
    result3dm_display = tk.Text(master=window, height=1,width=11)
    result3dm_display.grid(column=8, row=23)
    result3dm_display.insert(tk.END, Avg_3d)
    result3dv_display = tk.Text(master=window, height=1,width=11)
    result3dv_display.grid(column=9, row=23)
    result3dv_display.insert(tk.END, dev_3d)
    result3dstd_display = tk.Text(master=window, heigh=1,width=11)
    result3dstd_display.grid(column=10, row=23)
    result3dstd_display.insert(tk.END, var_3d)

    fig = plt.figure()
    ax1 = fig.add_subplot(212)
    ax2 = fig.add_subplot(221)
    ax3 = fig.add_subplot(222, projection='3d')
    ax1.plot(ys, color='blue')
    ax2.scatter(xs,ys, color='blue', s=5, marker='*')
    ax3.scatter(xs,ys,zs, color='blue', marker='*')
    ax1.axhline(y=0)
    ax1.set_xlabel('Rule 1 - Scenario 2')
    ax2.axhline(y=0)
    ax2.axvline(x=0)
    ax2.axis([-7, 7, -7, 7])
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Z')
    plt.show()

def rule22(): #!! #funnel moves (-yk)
    simulation = int(entry4.get())
    mean = float(entry2.get())
    std = float(entry3.get())
    amean = float(entry5.get())
    astd = float(entry6.get())
    phi = float(entry7.get())
    yposition = 0
    xposition = 0
    zposition = 0
    nkx = xposition
    nky = yposition
    nkz = zposition
    xs = []
    ys = []
    zs = []
    for i in range(simulation):
        ynoise = rnv(mean,std)
        xnoise = rnv(mean,std)
        znoise = rnv(mean,std)
        aky = rnv(amean,astd)
        akx = rnv(amean,astd)
        akz = rnv(amean,astd)
        nkx = phi*nkx + akx
        nky = phi*nky + aky
        nkz = phi*nkz + akz
        yk = mean + nky + yposition + ynoise
        xk = mean + nkx + xposition + xnoise
        zk = mean + nkz + zposition + znoise
        ys.append(yk)
        xs.append(xk)
        zs.append(zk)
        yposition = yposition - yk
        xposition = xposition - xk
        zposition = zposition - zk

    Avg2 = (sum(ys)/len(ys))
    Var2 = np.var(ys)
    dev = statistics.pstdev(ys)
    return (Avg2,Var2, xs, ys, zs, dev)

def rule22_display(): #shows the results2
    result2m = rule22()
    mean = result2m[0]
    vari = result2m[1]
    dev = result2m[5]
    xs = result2m[2]
    ys = result2m[3]
    zs = result2m[4]
    xy = np.array([xs,ys])
    xyz = np.array([xs,ys,zs])
    Avg_2d = np.mean(xy)
    dev_2d = np.std(xy)
    var_2d = np.var(xy)
    Avg_3d = np.mean(xyz)
    dev_3d = np.std(xyz)
    var_3d = np.var(xyz)

    result2m_display = tk.Text(master=window, height=1,width=11)
    result2m_display.grid(column=8, row=13)
    result2m_display.insert(tk.END, mean)
    result2v_display = tk.Text(master=window, height=1,width=11)
    result2v_display.grid(column=9, row=13)
    result2v_display.insert(tk.END, vari)
    resultstd_display = tk.Text(master=window, heigh=1,width=11)
    resultstd_display.grid(column=10, row=13)
    resultstd_display.insert(tk.END, dev)
    # **** 2D ****
    result2dm_display = tk.Text(master=window, height=1,width=11)
    result2dm_display.grid(column=8, row=19)
    result2dm_display.insert(tk.END, Avg_2d)
    result2dv_display = tk.Text(master=window, height=1,width=11)
    result2dv_display.grid(column=9, row=19)
    result2dv_display.insert(tk.END, dev_2d)
    result2dstd_display = tk.Text(master=window, heigh=1,width=11)
    result2dstd_display.grid(column=10, row=19)
    result2dstd_display.insert(tk.END, var_2d)
    # **** 3D ****
    result3dm_display = tk.Text(master=window, height=1,width=11)
    result3dm_display.grid(column=8, row=24)
    result3dm_display.insert(tk.END, Avg_3d)
    result3dv_display = tk.Text(master=window, height=1,width=11)
    result3dv_display.grid(column=9, row=24)
    result3dv_display.insert(tk.END, dev_3d)
    result3dstd_display = tk.Text(master=window, heigh=1,width=11)
    result3dstd_display.grid(column=10, row=24)
    result3dstd_display.insert(tk.END, var_3d)

    fig = plt.figure()
    ax1 = fig.add_subplot(212)
    ax2 = fig.add_subplot(221)
    ax3 = fig.add_subplot(222, projection='3d')
    ax1.plot(ys, color='green')
    ax2.scatter(xs,ys, color='green', s=5, marker='*')
    ax3.scatter(xs,ys,zs, color='green', marker='*')
    ax1.axhline(y=0)
    ax1.set_xlabel('Rule 2 - Scenario 2')
    ax2.axhline(y=0)
    ax2.axvline(x=0)
    ax2.axis([-7, 7, -7, 7])
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Z')
    plt.show()

def rule32(): # UPDATED!! #funnel moves from target minus yk
    simulation = int(entry4.get())
    mean = float(entry2.get())
    std = float(entry3.get())
    amean = float(entry5.get())
    astd = float(entry6.get())
    phi = float(entry7.get())
    sposition = 0
    fyposition = 0
    fxposition = 0
    fzposition = 0
    nkx = fxposition
    nky = fyposition
    nkz = fyposition
    xs = []
    ys = []
    zs = []
    for i in range(simulation):
        ynoise = rnv(mean,std)
        xnoise = rnv(mean, std)
        znoise = rnv(mean, std)
        aky = rnv(amean,astd)
        akx = rnv(amean,astd)
        akz = rnv(amean,astd)
        nky = phi*nky + aky
        nkx = phi*nkx + akx
        nkz = phi*nkz + akz
        yk = mean + nky + (sposition + fyposition) + ynoise
        xk = mean + nkx + (sposition + fxposition) + xnoise
        zk = mean + nkz + (sposition + fzposition) + znoise
        ys.append(yk)
        xs.append(xk)
        zs.append(zk)
        fyposition = sposition - yk
        fxposition = sposition - xk
        fzposition = sposition - zk

    Avg3 = (sum(ys)/len(ys))
    Var3 = np.var(ys)
    dev = statistics.pstdev(ys)
    return (Avg3,Var3, xs, ys, zs, dev)

def rule32_display(): #shows the results3
    result3m = rule32()
    mean = result3m[0]
    vari = result3m[1]
    dev = result3m[5]
    xs = result3m[2]
    ys = result3m[3]
    zs = result3m[4]
    xy = np.array([xs,ys])
    xyz = np.array([xs,ys,zs])
    Avg_2d = np.mean(xy)
    dev_2d = np.std(xy)
    var_2d = np.var(xy)
    Avg_3d = np.mean(xyz)
    dev_3d = np.std(xyz)
    var_3d = np.var(xyz)

    result3m_display = tk.Text(master=window, height=1,width=11)
    result3m_display.grid(column=8, row=14)
    result3m_display.insert(tk.END, mean)
    result3v_display = tk.Text(master=window, height=1,width=11)
    result3v_display.grid(column=9, row=14)
    result3v_display.insert(tk.END, vari)
    resultstd_display = tk.Text(master=window, heigh=1,width=11)
    resultstd_display.grid(column=10, row=14)
    resultstd_display.insert(tk.END, dev)
    # **** 2D ****
    result2dm_display = tk.Text(master=window, height=1,width=11)
    result2dm_display.grid(column=8, row=20)
    result2dm_display.insert(tk.END, Avg_2d)
    result2dv_display = tk.Text(master=window, height=1,width=11)
    result2dv_display.grid(column=9, row=20)
    result2dv_display.insert(tk.END, dev_2d)
    result2dstd_display = tk.Text(master=window, heigh=1,width=11)
    result2dstd_display.grid(column=10, row=20)
    result2dstd_display.insert(tk.END, var_2d)
    # **** 3D ****
    result3dm_display = tk.Text(master=window, height=1,width=11)
    result3dm_display.grid(column=8, row=25)
    result3dm_display.insert(tk.END, Avg_3d)
    result3dv_display = tk.Text(master=window, height=1,width=11)
    result3dv_display.grid(column=9, row=25)
    result3dv_display.insert(tk.END, dev_3d)
    result3dstd_display = tk.Text(master=window, heigh=1,width=11)
    result3dstd_display.grid(column=10, row=25)
    result3dstd_display.insert(tk.END, var_3d)

    fig = plt.figure()
    ax1 = fig.add_subplot(212)
    ax2 = fig.add_subplot(221)
    ax3 = fig.add_subplot(222, projection='3d')
    ax1.plot(ys, color='pink')
    ax2.scatter(xs,ys, color='pink', s=5, marker='*')
    ax3.scatter(xs,ys,zs, color='pink', marker='*')
    ax1.axhline(y=0)
    ax1.set_xlabel('Rule 3 - Scenario 2')
    ax2.axhline(y=0)
    ax2.axvline(x=0)
    ax2.axis([-7, 7, -7, 7])
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Z')
    plt.show()

def rule42(): #UPDATED! #funnel moves to (yk-1)
    simulation = int(entry4.get())
    mean = float(entry2.get())
    std = float(entry3.get())
    amean = float(entry5.get())
    astd = float(entry6.get())
    phi = float(entry7.get())
    yposition = 0
    xposition = 0
    zposition = 0
    nkx = xposition
    nky = yposition
    nkz = zposition
    xs = []
    ys = []
    zs = []
    for i in range(simulation):
        ynoise = rnv(mean,std)
        xnoise = rnv(mean,std)
        znoise = rnv(mean,std)
        aky = rnv(amean,astd)
        akx = rnv(amean,astd)
        akz = rnv(amean,astd)
        nky = phi*nky + aky
        nkx = phi*nkx + akx
        nkz = phi*nkz + akz
        yk = mean + nky + yposition + ynoise
        xk = mean + nkx + xposition + xnoise
        zk = mean + nkz + zposition + znoise
        ys.append(yk)
        xs.append(xk)
        zs.append(zk)
        yposition = yk
        xposition = xk
        zposition = zk

    Avg4 = (sum(ys)/len(ys))
    Var4 = np.var(ys)
    dev = statistics.pstdev(ys)
    return (Avg4, Var4, xs, ys, xs, dev)

def rule42_display(): #shows the results4
    result4m = rule42()
    mean = result4m[0]
    vari = result4m[1]
    dev = result4m[5]
    xs = result4m[2]
    ys = result4m[3]
    zs = result4m[4]
    xy = np.array([xs,ys])
    xyz = np.array([xs,ys,zs])
    Avg_2d = np.mean(xy)
    dev_2d = np.std(xy)
    var_2d = np.var(xy)
    Avg_3d = np.mean(xyz)
    dev_3d = np.std(xyz)
    var_3d = np.var(xyz)

    result4m_display = tk.Text(master=window, height=1,width=11)
    result4m_display.grid(column=8, row=15)
    result4m_display.insert(tk.END, mean)
    result4v_display =tk.Text(master=window, height=1,width=11)
    result4v_display.grid(column=9, row=15)
    result4v_display.insert(tk.END, vari)
    resultstd_display = tk.Text(master=window, heigh=1,width=11)
    resultstd_display.grid(column=10, row=15)
    resultstd_display.insert(tk.END, dev)
    # **** 2D ****
    result2dm_display = tk.Text(master=window, height=1,width=11)
    result2dm_display.grid(column=8, row=21)
    result2dm_display.insert(tk.END, Avg_2d)
    result2dv_display = tk.Text(master=window, height=1,width=11)
    result2dv_display.grid(column=9, row=21)
    result2dv_display.insert(tk.END, dev_2d)
    result2dstd_display = tk.Text(master=window, heigh=1,width=11)
    result2dstd_display.grid(column=10, row=21)
    result2dstd_display.insert(tk.END, var_2d)
    # **** 3D ****
    result3dm_display = tk.Text(master=window, height=1,width=11)
    result3dm_display.grid(column=8, row=26)
    result3dm_display.insert(tk.END, Avg_3d)
    result3dv_display = tk.Text(master=window, height=1,width=11)
    result3dv_display.grid(column=9, row=26)
    result3dv_display.insert(tk.END, dev_3d)
    result3dstd_display = tk.Text(master=window, heigh=1,width=11)
    result3dstd_display.grid(column=10, row=26)
    result3dstd_display.insert(tk.END, var_3d)

    fig = plt.figure()
    ax1 = fig.add_subplot(212)
    ax2 = fig.add_subplot(221)
    ax3 = fig.add_subplot(222, projection='3d')
    ax1.plot(ys, color='purple')
    ax2.scatter(xs,ys, color='purple', s=5, marker='*')
    ax3.scatter(xs,ys,zs, color='purple', marker='*')
    ax1.axhline(y=0)
    ax1.set_xlabel('Rule 4 - Scenario 2')
    ax2.axhline(y=0)
    ax2.axvline(x=0)
    ax2.axis([-7, 7, -7, 7])
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Z')
    plt.show()

def performance():
    estd = float(entry3.get())
    astd = float(entry6.get())
    phi = float(entry7.get())

    Vrule1 = (1/(1-(phi**2))) * ((astd)**2) + ((estd)**2)
    Vrule2 = (2/(1+phi)) * ((astd)**2) + (2*((estd)**2))
    if Vrule1 > Vrule2:
        show = 'Rule 1 better'
        label42 = tk.Label(text= show, bg='gold')
        label42.grid(column=7,row=28)
    elif Vrule1 == Vrule2:
        show1 = 'Rules are the same'
        label43 = tk.Label(text=show1, bg='gold')
        label43.grid(column=7,row=28)
    else:
        show2 = 'Rule2 better'
        label43 = tk.Label(text=show2, bg='gold')
        label43.grid(column=7,row=28)


# --- LABELS ---
label1 = tk.Label(text='FUNNEL EXPERIMENT', bg='gold')
label1.grid(column = 0, row=0)
label2 = tk.Label(text='ek mean',bg='yellow')
label2.grid(column = 0, row=1)
label3 = tk.Label(text='ek std', bg ='yellow')
label3.grid(column = 0, row=2)
label4 = tk.Label(text='Insert # runs', bg='red')
label4.grid(column = 0, row=3)
label5 = tk.Label(text='ak mean', bg='orange')
label5.grid(column = 11, row=1)
label6 = tk.Label(text='ak std', bg='orange')
label6.grid(column = 11, row=2)
label7 = tk.Label(text='Phi', bg='light blue')
label7.grid(column = 11, row=3)
label8 = tk.Label(text='Scenario 1', bg='light green')
label8.grid(column = 1, row=5)
label8 = tk.Label(text='Scenario 2', bg='light green')
label8.grid(column = 10, row=5)
label9 = tk.Label(text='Average', bg='light green')
label9.grid(column = 4, row=11)
label10 = tk.Label(text='Variance', bg='light green')
label10.grid(column = 5, row=11)
label11 = tk.Label(text='Average', bg='light green')
label11.grid(column = 8, row=11)
label12 = tk.Label(text='Variance', bg='light green')
label12.grid(column = 9, row=11)
label13 = tk.Label(text='R1', bg='blue')
label13.grid(column = 3, row=12)
label14 = tk.Label(text='R2', bg='green')
label14.grid(column = 3, row=13)
label15 = tk.Label(text='R3', bg='pink')
label15.grid(column = 3, row=14)
label16 = tk.Label(text='R4', bg='purple')
label16.grid(column = 3, row=15)
label17 = tk.Label(text='R1', bg='blue')
label17.grid(column = 7, row=12)
label18 = tk.Label(text='R2', bg='green')
label18.grid(column = 7, row=13)
label19 = tk.Label(text='R3', bg='pink')
label19.grid(column = 7, row=14)
label20 = tk.Label(text='R4', bg='purple')
label20.grid(column = 7, row=15)
label21 = tk.Label(text='1 Dimension', bg='light green')
label21.grid(column = 8, row=10)
label22 = tk.Label(text='Std', bg='Light green')
label22.grid(column = 6, row=11)
label23 = tk.Label(text='Std', bg='Light green')
label23.grid(column = 10, row=11)
label24 = tk.Label(text='2 Dimension', bg='light green')
label24.grid(column = 8, row=17)
label25 = tk.Label(text='R1', bg='blue')
label25.grid(column = 3, row=18)
label26 = tk.Label(text='R2', bg='green')
label26.grid(column = 3, row=19)
label27 = tk.Label(text='R3', bg='pink')
label27.grid(column = 3, row=20)
label28 = tk.Label(text='R4', bg='purple')
label28.grid(column = 3, row=21)
label29 = tk.Label(text='R1', bg='blue')
label29.grid(column = 7, row=18)
label30 = tk.Label(text='R2', bg='green')
label30.grid(column = 7, row=19)
label31 = tk.Label(text='R3', bg='pink')
label31.grid(column = 7, row=20)
label32 = tk.Label(text='R4', bg='purple')
label32.grid(column = 7, row=21)
label33 = tk.Label(text='3 Dimension', bg='light green')
label33.grid(column = 8, row=22)
label34 = tk.Label(text='R1', bg='blue')
label34.grid(column = 3, row=23)
label35 = tk.Label(text='R2', bg='green')
label35.grid(column = 3, row=24)
label36 = tk.Label(text='R3', bg='pink')
label36.grid(column = 3, row=25)
label37 = tk.Label(text='R4', bg='purple')
label37.grid(column = 3, row=26)
label38 = tk.Label(text='R1', bg='blue')
label38.grid(column = 7, row=23)
label39 = tk.Label(text='R2', bg='green')
label39.grid(column = 7, row=24)
label40 = tk.Label(text='R3', bg='pink')
label40.grid(column = 7, row=25)
label41 = tk.Label(text='R4', bg='purple')
label41.grid(column = 7, row=26)


# --- ENTRIES ---
entry2 = tk.Entry() # ek mean
entry2.grid(column=1, row=1)
entry3 = tk.Entry()
entry3.grid(column=1, row=2) # ek std
entry4 = tk.Entry()
entry4.grid(column=1, row=3) # runs
entry5 = tk.Entry()
entry5.grid(column=10, row=1) # ak mean
entry6 = tk.Entry()
entry6.grid(column=10, row=2) # ak std
entry7 = tk.Entry()
entry7.grid(column=10, row=3) # phi

# --- BUTTONS ---
button1 = tk.Button(text='Rule 1', command = rule1_display, bg = 'blue')
button1.grid(column=1,row=6)
button2 = tk.Button(text='Rule 2', command = rule2_display, bg = 'green')
button2.grid(column=1,row=7)
button3 = tk.Button(text='Rule 3', command = rule3_display,  bg = 'pink')
button3.grid(column=1,row=8)
button4 = tk.Button(text='Rule 4', command = rule4_display, bg = 'purple')
button4.grid(column=1,row=9)
button6 = tk.Button(text='Rule 1', command = rule12_display, bg = 'blue')
button6.grid(column=10,row=6)
button7 = tk.Button(text='Rule 2', command = rule22_display, bg = 'green')
button7.grid(column=10,row=7)
button8 = tk.Button(text='Rule 3', command = rule32_display, bg = 'pink')
button8.grid(column=10,row=8)
button9 = tk.Button(text='Rule 4', command = rule42_display, bg = 'purple')
button9.grid(column=10,row=9)
#button10 = tk.Button(text='Performance', command = performance, bg='gold')
#button10.grid(column=7,row=27)


window.mainloop()
