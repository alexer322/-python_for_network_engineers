# Задача 2 Написать программу: дан список из 10 чисел, которые задаются с помощью
# датчика случайных чисел. Программа находит повторяющиеся элементы и считает
# количество повторений. Например дан список (1,1,1,2,3,4,2,3,4) результат число 1
# повторяется 3 раза, число 2 – 2раза, число 3 - 2 раза, число 4 – 2 раза


import random

i = 0
list = []

while i < 10:

    value = random.randint(1, 10)
    list.append(value)
    i+=1

print("сгенерированный лист {list}")

new_list = []
count = []
for i in list:
  if i not in new_list:
    new_list.append(i)
    count.append(list.count(i))
print(f"после сортировки {new_list}")

i = 0
n = len(new_list)
while i < n:
    if count[i] in [2,3,4]:
        print(f"число {new_list[i]} повторяется {count[i]} раза")
    else:
       print(f"число {new_list[i]} повторяется {count[i]} раз")
    i+=1

