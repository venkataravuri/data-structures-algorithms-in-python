from tkinter import N


hexa = []

result = []

num = int(input("Entner number:"))

des = 0

i = 0

temp = num

while temp > 0:
    rem = int(temp % 10)
    des = des + rem * pow(2, i)
    i += 1
    temp = int(temp / 10)

print("Decimal:", des)
