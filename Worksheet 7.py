import tkinter as tk
root = tk.Tk()
root.title("The Box")

mylabel = tk.Label(text="Triangle Area Calculator", fg="black", font="96").pack()
mylabel = tk.Label(text="Box 1: Width", fg="black", font="48").pack()
mylabel = tk.Label(text="Box 2: Height", fg="black", font="48").pack()


def showMessage():
    w = a.get()
    h = b.get()
    p = (w * h)*0.5
    tk.Label(root, text=p, fg="red", font="48").pack()

a = tk.IntVar()
mytext = tk.Entry(root, textvariable=a).pack()
b = tk.IntVar()
mytext = tk.Entry(root, textvariable=b).pack()

btn1 = tk.Button(root, text="Press Me!", command=showMessage).pack()

root.geometry("469x469")
root.mainloop()
