from tkinter import *
import pyqrcode
from PIL import ImageTk, Image

def generate_qr():
    name = name_entry.get()
    link = link_entry.get()
    if name and link:
        qr = pyqrcode.create(link)
        qr.png(f"{name}.png", scale=6)
        img = Image.open(f"{name}.png")
        img = img.resize((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        canvas.create_image(200, 320, image=img_tk)
        canvas.image = img_tk

root = Tk()
root.title("QRCode Generator")
canvas = Canvas(root, width=400, height=500)
canvas.pack()

app_label = Label(root, text="QRCode Generator", font=('Angsana New', 32,))
canvas.create_window(200, 50, window=app_label)

name_label = Label(root, text="ชื่อคิวอาร์โค้ด")
canvas.create_window(200, 100, window=name_label)

link_label = Label(root, text="URL")
canvas.create_window(200, 140, window=link_label)

name_entry = Entry(root)
canvas.create_window(200, 120, window=name_entry)

link_entry = Entry(root)
canvas.create_window(200, 160, window=link_entry)

button = Button(text="สร้างคิวอาร์โค้ด", command=generate_qr)
canvas.create_window(200, 190, window=button)

root.mainloop()