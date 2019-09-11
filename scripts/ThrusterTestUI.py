#!/usr/bin/env python3
import rospy
import tkinter as tk

root = tk.Tk()
root.title("Thruster Test")

frame = tk.Frame(root)
frame.pack()

min_label = tk.Label(frame,
                     text = "Motor Min",
                     fg = "black")
min_label.pack()

motor_min = tk.Entry(frame,
                     text = "Motor Min Here",
                     fg = "black")
motor_min.pack()

min_label = tk.Label(frame,
                     text = "Motor Max",
                     fg = "black")
min_label.pack()

motor_max = tk.Entry(frame,
                     text = "Motor Max Here",
                     fg = "black")
motor_max.pack()

Start  = tk.Button(frame,
                   text = "Start",
                   fg = "green",
                   command = quit)
Start.pack(side = tk.LEFT)



Stop = tk.Button(frame,
                 text = "Stop",
                 fg = "red",
                 command = quit)
Stop.pack(side = tk.RIGHT)
root.mainloop()


