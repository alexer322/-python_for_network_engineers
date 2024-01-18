# Задача 1 Написать программу, которая последовательно вызывает три функции.
# Функция 1 – подсчитывает для заданного отрезка чисел все числа, которые делятся нацело
# на 3, функция 2 – подсчитывает для заданного отрезка чисел все числа, которые делятся
# нацело на 4, Функция 3– подсчитывает для заданного отрезка чисел все числа, которые
# делятся нацело на 5

def division_by_3(start, end):
    count = 0
    for num in range(start, end + 1):
        if num % 3 == 0:
            count += 1
    return count

def division_by_4(start, end):
    count = 0
    for num in range(start, end + 1):
        if num % 4 == 0:
            count += 1
    return count

def division_by_5(start, end):
    count = 0
    for num in range(start, end + 1):
        if num % 5 == 0:
            count += 1
    return count


start_range = 1
end_range = 100


a = division_by_3(start_range, end_range)
b = division_by_4(start_range, end_range)
c = division_by_5(start_range, end_range)

print(f"Делится нацело на 3: {a} числа")
print(f"Делится нацело на 4: {b} числа")
print(f"Делится нацело на 5: {c} числа")
