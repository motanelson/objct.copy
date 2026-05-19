import tkinter as tk

class myapp:
    def __init__(self,root:tk.Tk):
        self.root=root
        self.root.title("hello")
        self.root.configure(bg="black")


root=tk.Tk()
app=myapp(root)
root.mainloop()

