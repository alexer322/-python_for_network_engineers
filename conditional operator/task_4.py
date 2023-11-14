# Напишите программу, которая определяет пройдет коробка с размерами a*b*c в
# ящик с размерами x*y*z


a = float(input("Введите длину коробки (a): "))     # Ввод размеров коробки
b = float(input("Введите ширину коробки (b): "))
c = float(input("Введите высоту коробки (c): "))


x = float(input("Введите длину ящика (x): "))     # Ввод размеров ящика
y = float(input("Введите ширину ящика (y): "))
z = float(input("Введите высоту ящика (z): "))


flag = False

if  (a <= x and b <= y and c <= z) or (a <= y and b <= x and c <= z) or \
    (a <= x and b <= z and c <= y) or (a <= z and b <= x and c <= y) or \
    (a <= y and b <= z and c <= x) or (a <= z and b <= y and c <= x):
    flag = True

if flag:
    print("Коробка проходит.")
else:
    print("Коробка не проходит.")
