# Задача 1 Написать программу: дан список из 10 чисел, которые задаются с помощью
# датчика случайных чисел в диапазоне 1-10. Программа находит повторяющиеся
# elementы и удаляет их из списка. Например, дан список (1,1,1,2,3,4,2,3,4) результат
# (1,2,3,4)

import random

i = 0
list = []

while i < 10:

    value = random.randint(1, 10)
    list.append(value)
    i+=1
print(f"сгенерированный лист {list}")

# print((set)(list))

new_list = sorted(set(list), key=lambda x: list.index(x))  #Через множества и лямбду
print(f"после сортировки {new_list}")
