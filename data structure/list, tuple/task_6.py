# Задача 6 Дан список в виде списка списков, например [[1,2,3],[2,6,4],[3,4,5],[6,3,7]].
# Вывести список из элементов списка – без повторения, результат– [1,2,3,6,4,5,7]. Вывести
# списков из элементов списка, которые повторяются в исходном списке, результат –
# [2,3,4,6]

list = [[1, 2, 3], [2, 6, 4], [3, 4, 5], [6, 3, 7]]


new_list = []
re_elements = []

for i in list:
    for k in i:
        if k in new_list:
            re_elements.append(k)
        else:
            new_list.append(k)

# print(new_list)  #уникальные
# print(re_elements)      #повторы


re_elements_new = []

for i in re_elements:
  if i not in re_elements_new:
    re_elements_new.append(i)
print(f"Повторы {re_elements_new}")

