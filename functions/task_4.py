# Задача 4 Дан список целых чисел. Посчитать, сколько раз в нем встречается каждое
# число. Например, если дан список [1, 1, 3, 2, 1, 3, 4], то в нем число 1 встречается три раза,
# число 3 - два раза, числа 2 и 4 - по одному разу.

def check(a):
    new_list = []
    count = []
    for i in a:
       if i not in new_list:
          new_list.append(i)
          count.append(a.count(i))
    i = 0
    n = len(new_list)
    print(f"в листе {a} \n")
    while i < n:
        print(f"число {new_list[i]} - встречается {count[i]} ")
        i+=1
    print("\n")    



list = [1, 1, 3, 2, 1, 3, 4]
list2 = [33, 2, 22, 22, 1, 1, 5, 6, 3, 1]


check(list)
check(list2)
