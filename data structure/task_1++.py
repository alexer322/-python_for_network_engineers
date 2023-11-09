import random

i=0
list=[]

while i < 10:

    value = random.randint(1, 10)
    list.append(value)
    i=i+1
print("сгенерированный лист", list)

# print((set)(list))

new_list = sorted(set(list), key=lambda x: list.index(x))  #Через множества и лямбду
print("после сортировки", new_list)
