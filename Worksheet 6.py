def numsum(a,b):
    sum = a+b
    return sum
print(numsum(4,6))


def power(a):
    return a**2
print(power(25))


def num_to_month_str(a):
    if a == 1:
        return("January")
    elif a == 2:
        return("February")
    elif a == 3:
        return("March")
    elif a == 4:
        return("April")
    elif a == 5:
        return("May")
    elif a == 6:
        return("June")
    elif a == 7:
        return("July")
    elif a == 8:
        return("August")
    elif a == 9:
        return("Sebtember")
    elif a == 10:
        return("October")
    elif a == 11:
        return("November")
    elif a == 12:
        return("December")
num = int(input(""))
print(num_to_month_str(num))


def join3str(str1,str2,str3):
    return (str1+str2+str3)
x1 = str(input(""))
x2 = str(input(""))
x3 = str(input(""))
print(join3str(x1,x2,x3))


def discountcal(price, discount):
    return price*(discount/100)
x = int(input("price: "))
y = int(input("discount: "))
print(discountcal(x,y))
