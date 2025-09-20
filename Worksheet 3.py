import math
budget = float(1000)
products = {
            1:{"name": "หมูสับกิโล", "price": 150.00},
            2:{"name": "เนื้ออกไก่", "price": 105.00},
            3:{"name": "ไก่บ้าน(ตัว)", "price": 120.00},
            4:{"name": "มาม่าต้มยํา", "price": 6.50},
            5:{"name": "ข้าวสาร", "price": 150.00},
            6:{"name": "น้ำตาล", "price": 20.00},
            7:{"name": "ปลากะป๋องสามแม่ครัว", "price": 10.00},
            8:{"name": "ซอสน้ำมันหอย", "price": 18.00},
            9:{"name": "ผงชูรส", "price": 10.25},
            10:{"name": "ไข่แผงคละเบอร์", "price": 120.25},
            11:{"name": "ชาเขียว", "price": 21.50},
            12:{"name": "Pepsi", "price": 29.50},
            13:{"name": "กาแฟ", "price": 15.75},
            14:{"name": "ขนมปังอบเนย", "price": 19.00},
            15:{"name": "ชาไทย", "price": 11.50},
            16:{"name": "น้ําเปล่า", "price": 15.15},
            17:{"name": "น้ําแข็ง", "price": 10.00}
            }
min_items = int(15)
selected_items = []
total_price = float(0)
item_count = int(0)
remaining_budget = budget
print("ร้านค้าอะไรไม่รู้")
print(f"คุนมีเงินอยู่ {budget:.2f} บาท สำหรับซื้อสินค้าอย่างน้อย {min_items} รายการ")
while True:
    for item_id, item_info in products.items():
        print(f"    {item_id}. {item_info['name']} ({item_info['price']:.2f} บาท)")
    print(f"สินค้าที่เลือกแล้ว: {len(selected_items)} รายการ")
    print(f"ใช้เงินไปแล้ว: {total_price:.2f} บาท")
    print(f"เงินคงเหลือ: {remaining_budget:.2f} บาท")
    try:
        choice = input(f"เลือกหมายเลขสินค้าที่ต้องการ (เลือก {min_items} รายการขึ้นไป) หรือ 'done' เมื่อเลือกเสร็จ: ")
        if choice == 'done':
            if len(selected_items) < min_items:
                print(f"คุณต้องเลือกสินค้าอย่างน้อย {min_items} รายการ กรุณาเลือกเพิ่มเติม")
                continue
            else:
                break
        item_id = int(choice)
        if item_id not in products:
            print("ไม่มีสินค้ารายการนี้ กรุณาเลือกหมายเลขที่ถูกต้อง")
            continue
        item_name = products[item_id]["name"]
        item_price = products[item_id]["price"]
        if item_name in [item['name'] for item in selected_items]:
            print(f"คุณได้เลือก {item_name} ไปแล้ว กรุณาเลือกรายการอื่น")
            continue
        if remaining_budget < item_price:
            print(f"เงินไม่พอสำหรับ {item_name} (ราคา {item_price:.2f} บาท)")
            continue
        selected_items.append({"id": item_id, "name": item_name, "price": item_price})
        total_price += item_price
        remaining_budget -= item_price
        print(f"เพิ่ม {item_name} ในตะกร้าแล้ว!")
    except ValueError:
        print(" กรุณาป้อนหมายเลขสินค้า หรือ 'done' ให้ถูกต้อง ")
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
print("รายการสินค้าที่คุณเลือก")
if not selected_items:
    print("ไม่มีสินค้าในตะกร้า")
else:
    for i, item in enumerate(selected_items, 1):
        print(f"    {i}. {item['name']} ({item['price']:.2f} บาท)")
print(f"ยอดรวมที่ใช้ไป: {total_price:.2f} บาท")
print(f"เงินตั้งต้น: {budget:.2f} บาท")
change = budget - total_price
print(f"เงินทอน: {change:.2f} บาท")


b = float(input(("ความยาวฐานสามเหลี่ยม=")))
h = float(input(("ความสูงสามเหลี่ยม=")))
a = 0.5*b*h
float (a)
print("พื้นที่สามเหลี่ยม=%.6f" % a)


print("เปลี่ยนค่าองศาเซลเซียสเป็นองศาฟาเรนไฮต์และเคลวิน")
c = float(input("ค่าองศาเซลเซียส="))
f = (9/5)*c + 32
k = c + 273.15
print(f"{c} องศาเซลเซียส = {f} องศาฟาเรนไฮต์ และ {k} องศาเคลวิน")


import math
a = {10, 20, 30, 40, 50,60}
b = {30, 40, 50, 60, 70,80}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))





