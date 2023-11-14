# Поменять местами самый большой и самый маленький elementы списка


list = [10, 22, 4541, 12, 20, 222, 20]
print(list)

max_index = list.index(max(list))
min_index = list.index(min(list))

list[max_index], list[min_index] = list[min_index], list[max_index]

print(list)