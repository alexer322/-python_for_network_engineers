import random

i=0
list=[]

while i < 10:

    value = random.randint(1, 10)
    list.append(value)
    i=i+1

print("сгенерированный лист", list)

new_list=[]

for i in list:
  if i not in new_list:
    new_list.append(i)
print("после сортировки", new_list)
 
