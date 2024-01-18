# Задача 3
# Создать функцию print_ip_table, которая отображает таблицу доступных
# и недоступных IP-адресов.
# Функция ожидает как аргументы два списка:

# * список доступных IP-адресов
# * список недоступных IP-адресов
# Результат работы функции - вывод на стандартный поток вывода таблицы вида:
# Reachable Unreachable
# ----------- -------------
# 10.1.1.1 10.1.1.7
# 10.1.1.2 10.1.1.8
# 10.1.1.9
# """

def print_ip_table(reachable_ips, unreachable_ips):
    max_reachable = max(len(reachable_ips), 1)
    max_unreachable = max(len(unreachable_ips), 1)
    max_columns = max(max_reachable, max_unreachable)

    # print(max_reachable)
    # print(max_unreachable)


    print("Reachable\tUnreachable")
    print("-" * 10 + "\t" + "-" * 10)

    for i in range(max_columns):
        if i < len(reachable_ips):
            print(reachable_ips[i], end="\t")
        else:
            print(" " * 10, end="\t")

        if i < len(unreachable_ips):
            print(unreachable_ips[i])
        else:
            print()


reachable_addresses = ["10.1.1.1", "10.1.1.2", "10.1.1.9"]
unreachable_addresses = ["10.1.1.77", "10.1.1.8", "10.1.1.9", "10.1.1.9", "10.1.1.9"]

print_ip_table(reachable_addresses, unreachable_addresses)



