from random import normalvariate as rnv
import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

window = tk.Tk()
window.title('Funnel Project')
window.geometry('900x900')

# --- FUNCTIONS ---

def rule1(): #!!! #funnel does not move
    simulation = int(entry3.get())
    mean = float(entry1.get())
    std = float(entry2.get())
    fig = plt.figure()
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
    return (Avg1, Var1)

def rule1_display(): #shows the results1
    result1m = rule1()
    mean = result1m[0]
    vari = result1m[1]
    result1m_display = tk.Text(master=window, height=1,width=11)
    result1m_display.grid(column=1, row=7)
    result1m_display.insert(tk.END, mean)
    result1v_display = tk.Text(master=window, height=1,width=11)
    result1v_display.grid(column=1, row=9)
    result1v_display.insert(tk.END, vari)

def rule2(): #!! #funnel moves (-yk)
    simulation = int(entry3.get())
    mean = float(entry1.get())
    std = float(entry2.get())
    fig = plt.figure()
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
    return (Avg2,Var2)

def rule2_display(): #shows the results2
    result2m = rule2()
    mean = result2m[0]
    vari = result2m[1]
    result2m_display = tk.Text(master=window, height=1,width=11)
    result2m_display.grid(column=2, row=7)
    result2m_display.insert(tk.END, mean)
    result2v_display = tk.Text(master=window, height=1,width=11)
    result2v_display.grid(column=2, row=9)
    result2v_display.insert(tk.END, vari)

def rule3(): # UPDATED!! #funnel moves from target menos yk
    simulation = int(entry3.get())
    mean = float(entry1.get())
    std = float(entry2.get())
    fig = plt.figure()
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
    return (Avg3,Var3)

def rule3_display(): #shows the results3
    result3m = rule3()
    mean = result3m[0]
    vari = result3m[1]
    result3m_display = tk.Text(master=window, height=1,width=11)
    result3m_display.grid(column=3, row=7)
    result3m_display.insert(tk.END, mean)
    result3v_display = tk.Text(master=window, height=1,width=11)
    result3v_display.grid(column=3, row=9)
    result3v_display.insert(tk.END, vari)

def rule4(): #UPDATED! #funnel moves to (yk-1)
    simulation = int(entry3.get())
    mean = float(entry1.get())
    std = float(entry2.get())
    fig = plt.figure()
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

    return (Avg4, Var4)

def rule4_display(): #shows the results4
    result4m = rule4()
    mean = result4m[0]
    vari = result4m[1]
    result4m_display = tk.Text(master=window, height=1,width=11)
    result4m_display.grid(column=4, row=7)
    result4m_display.insert(tk.END, mean)
    result4v_display =tk.Text(master=window, height=1,width=11)
    result4v_display.grid(column=4, row=9)
    result4v_display.insert(tk.END, vari)

# --- Scenario2  falta actulizar las ecuaciones!!!!!!!---

def rule12(): #funnel does not move
    simulation = int(entry3.get())
    mean = float(entry1.get())
    std = float(entry2.get())
    fig = plt.figure()
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
    Avg12 = (sum(ys)/len(ys))
    Var12 = np.var(ys)
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
    return (Avg12, Var12)

def rule12_display(): #shows the results1
    result12m = rule12()
    mean = result12m[0]
    vari = result12m[1]
    result12m_display = tk.Text(master=window, height=1,width=11)
    result12m_display.grid(column=1, row=17)
    result12m_display.insert(tk.END, mean)
    result12v_display = tk.Text(master=window, height=1,width=11)
    result12v_display.grid(column=1, row=19)
    result12v_display.insert(tk.END, vari)

def rule22(): #funnel moves (-yk)
    simulation = int(entry3.get())
    mean = float(entry1.get())
    std = float(entry2.get())
    fig = plt.figure()
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
    ax1 = fig.add_subplot(212)
    ax2 = fig.add_subplot(221)
    ax3 = fig.add_subplot(222, projection='3d')
    ax1.plot(ys, color='green')
    ax2.scatter(xs,ys, color='green', s=5, marker='*')
    ax3.scatter(xs,ys,zs, color='green', marker='*')
    ax1.axhline(y=0)
    ax1.set_xlabel('Rule 2 - Scenrio 2')
    ax2.axhline(y=0)
    ax2.axvline(x=0)
    ax2.axis([-7, 7, -7, 7])
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Z')
    return (Avg2,Var2)

def rule22_display(): #shows the results2
    result22m = rule22()
    mean = result22m[0]
    vari = result22m[1]
    result22m_display = tk.Text(master=window, height=1,width=11)
    result22m_display.grid(column=2, row=17)
    result22m_display.insert(tk.END, mean)
    result22v_display = tk.Text(master=window, height=1,width=11)
    result22v_display.grid(column=2, row=19)
    result22v_display.insert(tk.END, vari)

def rule32(): #funnel moves from target minus yk
    simulation = int(entry3.get())
    mean = float(entry1.get())
    std = float(entry2.get())
    fig = plt.figure()
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
    return (Avg3,Var3)

def rule32_display(): #shows the results3
    result32m = rule32()
    mean = result32m[0]
    vari = result32m[1]
    result32m_display = tk.Text(master=window, height=1,width=11)
    result32m_display.grid(column=3, row=17)
    result32m_display.insert(tk.END, mean)
    result32v_display = tk.Text(master=window, height=1,width=11)
    result32v_display.grid(column=3, row=19)
    result32v_display.insert(tk.END, vari)

def rule42(): #funnel moves to (yk-1)
    simulation = int(entry3.get())
    mean = float(entry1.get())
    std = float(entry2.get())
    fig = plt.figure()
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

    return (Avg4, Var4)

def rule42_display(): #shows the results4
    result42m = rule42()
    mean = result42m[0]
    vari = result42m[1]
    result42m_display = tk.Text(master=window, height=1,width=11)
    result42m_display.grid(column=4, row=17)
    result42m_display.insert(tk.END, mean)
    result42v_display = tk.Text(master=window, height=1,width=11)
    result42v_display.grid(column=4, row=19)
    result42v_display.insert(tk.END, vari)

def graph():
    graph_display = plt.show()

# --- LABELS ---
label1 = tk.Label(text='Insert mean',bg='white')
label1.grid(column = 0, row=1)
label2 = tk.Label(text='Inser std', bg ='white')
label2.grid(column = 0, row=2)
label3 = tk.Label(text='Insert # runs', bg='white')
label3.grid(column = 0, row=3)
label4 = tk.Label(text='***Scenario1***\n***AVG***\n***VAR***')
label4.grid(column = 0, row=7)
label6 = tk.Label(text='Scenario 1',bg='green')
label6.grid(column = 0, row=4)
label7 = tk.Label(text='Scenario 2',bg='green')
label7.grid(column = 0, row=5)
label8 = tk.Label(text='***Scenario2***\n***AVG***\n***VAR***')
label8.grid(column = 0, row=17)
label9 = tk.Label(text='Insert phi')
label9.grid(column =2, row=2 )

# --- ENTRIES ---
entry1 = tk.Entry()
entry1.grid(column=1, row=1)
entry2 = tk.Entry()
entry2.grid(column=1, row=2)
entry3 = tk.Entry()
entry3.grid(column=1, row=3)
entry4 = tk.Entry()
entry4.grid(column=3, row=2)

# --- BUTTONS ---
button1 = tk.Button(text='Rule 1', command = rule1_display, bg = 'blue')
button1.grid(column=1,row=4)
button2 = tk.Button(text='Rule 2', command = rule2_display, bg = 'yellow')
button2.grid(column=2,row=4)
button3 = tk.Button(text='Rule 3', command = rule3_display, bg = 'pink')
button3.grid(column=3,row=4)
button4 = tk.Button(text='Rule 4', command = rule4_display, bg = 'purple')
button4.grid(column=4,row=4)
button5 = tk.Button(text='Graph', command = graph, bg='red')
button5.grid(column=4,row=6)
button6 = tk.Button(text='Rule 1', command = rule12_display, bg = 'blue')
button6.grid(column=1,row=5)
button7 = tk.Button(text='Rule 2', command = rule22_display, bg = 'yellow')
button7.grid(column=2,row=5)
button8 = tk.Button(text='Rule 3', command = rule32_display, bg = 'pink')
button8.grid(column=3,row=5)
button9 = tk.Button(text='Rule 4', command = rule42_display, bg = 'purple')
button9.grid(column=4,row=5)

window.mainloop()
