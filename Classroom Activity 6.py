import tkinter as tk

def show_info():
    label_result.config(
        text="ชื่อ : น.ส. พชรมน พลค้อ : ม.5/8 เลขที่ : 34"
    )

root = tk.Tk()
root.title("แสดงข้อมูลนักเรียน")
root.geometry("300x200")

btn_show = tk.Button(root, text="แสดงข้อมูล", command=show_info)
btn_show.pack(pady=10)

label_result = tk.Label(root, text="", font=("TH Sarabun New", 14))
label_result.pack(pady=10)

root.mainloop()
