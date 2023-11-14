
a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
c = float(input("Введите длину третьей стороны: "))


if a + b > c and a + c > b and b + c > a:    # Проверка существования треугольника
    if a == b == c:                            # Проверка типа треугольника
        print("Равносторонний")
    elif a == b or a == c or b == c:
        print("Равнобедренный")
    elif a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
        print("Прямоугольный")
    else:
        print("Обычный")
else:
    print("Треугольник не может существовать")