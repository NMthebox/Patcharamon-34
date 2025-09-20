
print("เกมทายตัวเลข 0-100")
target = 85
guess = int
count = 0
while (target != guess):
    guess = int(input("เดาเลข :"))
    if (0 > guess > 100):
        print("ขอโทษด้วยตัวเลขไม่อยู่ในช่วงระหว่าง 0-100 กรุณาทายใหม่")
        count += 1
    elif (guess < target):
        print("ขอโทษด้วยตัวเลขมีค่าน้อยเกินไปกว่าที่ตั้งไว้ กรุณาทายใหม่")
        count += 1
    elif (guess > target):
        print("ขอโทษด้วยตัวเลขมีค่ามากเกินไปกว่าที่ตั้งไว้ กรุณาทายใหม่")
        count += 1
count += 1
print(f"ยินดีด้วยคุณทายถูก คุณทายทั้งหมด {count} ครั้ง")


students = [
    "ธนวินท์", "ปภังกร", "พรพิพัฒน์", "ภูมิฉัตร", "ไวภพ", "ไอศูรย์", "วรท", "บึงพิพัฒน์", "พัทธนันท์",
    "รุจิภาส", "สรวิชญ์", "บุณยกร", "ชิษณุพงศ์", "สรยุทธ", "ฐตวรรณ", "จีรัชญ์", "ชยางกูร", "ไชยพศ",
    "ปองคุณ", "ศรัณยพงศ์", "รวิพล", "วิธวินท์", "ตรัยรัตน์", "ธาวิน", "วีรภัฏ", "จิรายุ", "เอกราช",
    "สิรวิชญ์", "ฐิติวัชร์", "เสฏพงศ์", "ภคินธ์", "ภณิตา", "กาญจนา", "ณัฐวิภา", "ธิชานัน",
    "นันทิชา", "อิษฎาอร", "พิมพ์มาดา", "สุวภัทร"
]
my_name = " พชรมน"
for name in students:
    if name != my_name:
        print(name)

print("1.", end=" ")
i= 1
while (i < 22):
    print(i, end=",")
    i+=2
print("\n2.", end=" ")
i = 2
while (i < 18):
    print(i, end=",")
    i+=3
print("\n3.", end=" ")
i = 100
while (i > -101):
    print(i, end=",")
    i-=10
print("\n4.", end=" ")
i = -30
while (i < 31):
    print(i, end=",")
    i+=10
print("\n5.", end=" ")
i = 15
while (i < 56):
    print(i, end=",")
    i+=8


print("โปรแกรมแสดงตารางแม่สูตรคูณ")
x = int(input("แสดงสูตรคูณแม่: "))
for i in range (1,13):
    print(f"{x} x {i} = {x*i}")

def sum_of_squares(numbers):
    total = 0
    for n in numbers:
        total += n ** 2
    return total
