import tkinter as tk

def createNewWindow():
    newWindow = tk.Toplevel(app)
    newWindow.geometry("200x200")
    labelExample = tk.Label(newWindow, text = "New Window")
    buttonExample = tk.Button(newWindow, text = "New Window button",command=newWindow.destroy)
    buttonExample1= tk.Button(newWindow, 
              text="quit",
              command=app.destroy)
    buttonExample1.pack()

    labelExample.pack()
    buttonExample.pack()
    

app = tk.Tk()
app.geometry("200x200")
buttonExample = tk.Button(app, 
              text="Create new window",
              command=createNewWindow)
buttonExample.pack()



app.mainloop()