import tkinter as tk
import pyautogui as py

position_x_y=()
position_list=[]

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.floater= FloatingWindow(self)
        

class FloatingWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.overrideredirect(True)
        self.label= tk.Label(self, text="Click on the grip to move")
        self.grip= tk.Label(self, bitmap="gray25")
        self.grip.pack(side="left", fill="y")
        self.label.pack(side="right", fill="both", expand=True)
        self.grip.bind("<ButtonPress-1>", self.start_move)
        self.grip.bind("<ButtonRelease-1>", self.stop_move)
        self.grip.bind("<B1-Motion>", self.do_move)
        self.grip.bind("<ButtonPress-1>", self.clickMouse1)

    def start_move(self, event):
        self.x= event.x
        self.y= event.y
    def stop_move(self, event):
        self.x= None
        self.y= None
    def do_move(self, event):
        deltax= event.x -self.x
        deltay= event.y -self.y
        x= self.winfo_x() + deltax
        y= self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

    def clickMouse1(self, event) :
        position_x_y=py.position()
        position_list.append(position_x_y)
        print(position_list)
        



app=App()



app.mainloop()