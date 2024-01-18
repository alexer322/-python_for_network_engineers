# Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
# но было бы удобно иметь возможность указывать адреса с помощью диапазона,
# например, 192.168.100.1-10.
# В этом задании необходимо создать функцию convert_ranges_to_ip_list,
# которая конвертирует список IP-адресов в разных форматах в список,
# где каждый IP-адрес указан отдельно.
# Функция ожидает как аргумент список, в котором содержатся IP-адреса
# и/или диапазоны IP-адресов.
# Элементы списка могут быть в формате:
# * 10.1.1.1
# * 10.1.1.1-10.1.1.10
# * 10.1.1.1-10
# Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
# адреса, включая последний адрес диапазона.
# Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
# последний октет адреса.
# Функция возвращает список IP-адресов.
# Например, если передать функции convert_ranges_to_ip_list такой список:
# ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
# Функция должна вернуть такой список:
# ['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
# '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']





input_list = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

result_list = []

for item in input_list:
    d = item.split('-')
    print(d)
    if len(d) == 1:
        result_list.append(d[0])
    else:
        start_ip = d[0]
        end_ip = d[1]
        # print(f"ddd {end_ip}")
        # base_ip = (start_ip[:-3])
        base_ip = '.'.join(start_ip.split('.')[:-1]) + '.'

        # print(base_ip)

        if '.' not in end_ip:
                start_octet = int(start_ip.split('.')[-1])
                # print(start_octet)
                end_octet = int(end_ip)

                # print(end_octet)
                for i in range(start_octet, end_octet + 1):
                    result_list.append(base_ip + str(i))
        else:
            start_ip_full = list(map(int, start_ip.split('.')))
            end_ip_full = list(map(int, end_ip.split('.')))
            # print(start_ip_full)
            # print(end_ip_full)
            while start_ip_full <= end_ip_full:
                result_list.append('.'.join(map(str, start_ip_full)))
                start_ip_full[3] += 1



print(f"result list ---  {result_list}")




