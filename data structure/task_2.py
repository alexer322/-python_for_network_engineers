import random

i=0
list=[]

while i < 10:

    value = random.randint(1, 10)
    list.append(value)
    i=i+1

print("сгенерированный лист", list)

new_list=[]
count= []
for i in list:
  if i not in new_list:
    new_list.append(i)
    count.append(list.count(i))
print("после сортировки", new_list)

i=0
n=len(new_list)
while i < n:
    if count[i] in [2,3,4]:
        print("число", new_list[i], "повторяется", count[i], "раза")
    else:
       print("число", new_list[i], "повторяется", count[i], "раз")
    i+=1

