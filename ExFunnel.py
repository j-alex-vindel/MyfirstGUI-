from random import normalvariate as rnv
import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np

window = tk.Tk()
window.title('Funnel Project')
window.geometry('400x400')

# --- Functions---
def rule1(): #calcultes and does the simulation
    simulation = int(entry3.get()) #entry 3 number of runs
    mean = float(entry1.get()) #entry1 mean
    std = float(entry2.get()) #entry2 std
    fig = plt.figure()
    position = 0
    x_values = []
    sim_values = []
    for i in range(simulation):
        noise = rnv(mean,std)
        Yk = mean + position + noise
        sim_values.append(Yk)
        x_values.append(position)
        position = position - Yk

    Avg = (sum(sim_values)/len(sim_values))
    Var_sim = np.var(sim_values)
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    ax1.plot(sim_values, color='blue')
    ax2.scatter(x_values,sim_values, color='green')

    return (Avg,Var_sim)

def rule1_display():
    result1 = rule1()
    result1_display = tk.Text(master=window, height=4,width=20)
    result1_display.grid(column=1, row=6)
    result1_display.insert(tk.END, result1[0])
    result1_display.grid(column=1, row=7)
    result1_display.insert(tk.END, result1[1])
def graph_show():
    graph1 = plt.show()
    graph_disp = tk.Text(master=window)
    graph_disp.grid(column=2,row=5)
    graph_disp.insert(tk.END, graph1)

# --- Labels ---
label1 = tk.Label(text='Funnel Experiment')
label1.grid(column = 0, row=0)
label2 = tk.Label(text='Insert mean: ')
label2.grid(column = 0,row=1)
label3 = tk.Label(text='Insert std: ')
label3.grid(column = 0, row=2)
label4 = tk.Label(text='Insert number of simulation runs: ')
label4.grid(column = 0, row=3)
label5 = tk.Label(text='***Avg***')
label5.grid(column = 0, row=6)
label6 = tk.Label(text='***VAR***')
label6.grid(column=0, row=7)

# --- Entries ---
entry1 = tk.Entry()
entry1.grid(column=1, row=1)
entry2 = tk.Entry()
entry2.grid(column=1, row=2)
entry3 = tk.Entry()
entry3.grid(column=1, row=3)

# --- Buttons ---
button1 = tk.Button(text='Rule 1',command = rule1_display, bg = 'blue')
button1.grid(column=0,row=4)
button2 = tk.Button(text='Graph',command = graph_show, bg = 'blue')
button2.grid(column=1,row=4)
button3 = tk.Button(text='Rule 2', bg = 'yellow')
button3.grid(column=3,row=4)





window.mainloop()
