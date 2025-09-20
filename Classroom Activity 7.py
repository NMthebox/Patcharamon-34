import tkinter as tk

def countdown(time_left):
    if time_left > 0:
        label.config(text=str(time_left))
        root.after(1000, countdown, time_left - 1)  # เรียกตัวเองใหม่ทุก 1 วิ
    else:
        label.config(
            text="ชื่อ - นามสกุล: น.ส.พชรมน พลค้อ"
                 "ชื่อเล่น: เนย"
                 "ห้องเรียน: ม.5/8"
                 "แผนการเรียน: วิทย์-คณิต เทคโน"
                 "อยากเรียนคณะ: วิศวกรรมศาสตร์ สาขาอิเล็กทรอนิค"
        )

root = tk.Tk()
root.title("นับเวลาถอยหลัง")
root.geometry("400x250")

label = tk.Label(root, text="", font=("TH Sarabun New", 20))
label.pack(pady=40)

countdown(10)

root.mainloop()
