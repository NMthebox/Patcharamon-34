chest = float(input("กรุณากรอกรอบอก: "))

if chest <= 34:
    print("ขนาดเสื้อ: XS")
elif chest <= 36:
    print("ขนาดเสื้อ: S")
elif chest <= 38:
    print("ขนาดเสื้อ: M")
elif chest <= 40:
    print("ขนาดเสื้อ: L")
else:
    print("ขนาดเสื้อ: XL")


income = float(input("กรุณากรอกรายได้ต่อเดือน: "))

if income < 15000:
    print("รายได้น้อยกว่า 15000 บาท ไม่สามารถทำบัตรเครดิตได้")
elif income < 30000:
    print("รายได้น้อยกว่า 30000 บาท วงเงินคุณไม่สามารถทำบัตรได้")
elif income <= 89999:
    print("คุณทำบัตรเงินได้")
elif income <= 99999:
    print("คุณทำบัตรทองได้")
else:
    print("คุณทำบัตร Platinum ได้")


score = int(input("กรุณากรอกคะแนนเต็ม 100: "))

if score >= 80:
    print("เกรด A")
elif score >= 70:
    print("เกรด B")
elif score >= 60:
    print("เกรด C")
elif score >= 50:
    print("เกรด D")
else:
    print("เกรด F")


username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "Ad13n@23t":
    print("Welcome, admin")
else:
    print("You are not admin")


weight = float(input("กรุณากรอกน้ำหนัก (kg): "))
height = float(input("กรุณากรอกส่วนสูง (m): "))

bmi = weight / (height ** 2)

print(f"BMI is {bmi:.1f}")

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obesity")
