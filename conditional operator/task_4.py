# Напишите программу, которая определяет пройдет коробка с размерами a*b*c в
# ящик с размерами x*y*z

a = int(input("введи размер коробки - длина "))
if (a > 0):
    print("длина ящика", a)
else:
    exit()
b = int(input("введи размер коробки - ширина "))
if (b > 0):
    print("ширина ящика", b)
else:
    exit()
c = int(input("введи размер коробки - высота "))
if (c > 0):
    print("высота коробки", c)
else:
    exit()

x = int(input("введи ширину двери "))
y = int(input("введи высоту двери "))


if ( a < x and b < y ) or ( a < y and b < x ):
    print("Проходит")

elif ( b < x and c < y ) or ( b < y and c < x):
    print("Проходит")

elif ( a < x and c < y ) or ( a < y and c < x):
    print("Проходит")

else:
    print("Непроходит")