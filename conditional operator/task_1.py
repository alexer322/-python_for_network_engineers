# Напишите программу, которая запрашивает у пользователя три числа в диапазоне
# 1-1000. Компьютер генерирует два случайных числа в диапазоне 1-100, которые
# определяют отрезок. Определить какие числа указанные пользователям попали в
# отрезок.

import random

nums = []

i = 0
while i < 3:

    num = int(input(f"Введи число {i + 1} (от 1 до 1000): "))

    if 1 <= num <= 1000:
        nums.append(num)
        i+=1
    else:
        print("Введи число в диапазоне от 1 до 1000")
   

# print(nums)

i = 0
check_list = []
while i < 2:

    value = random.randint(1, 1000)
    check_list.append(value)
    i+=1

# print(check_list)
min_check_list = min(check_list)
max_check_list = max(check_list)
print(f"Отрезок сгенерился от {min_check_list} до {max_check_list}")


for num in nums:
    if min_check_list <= num <= max_check_list:
        print(f"Число {num} попадает в указанный отрезок.")
    else:
        print(f"Число {num} не попадает в указанный отрезок.")