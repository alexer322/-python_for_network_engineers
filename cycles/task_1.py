# Задание 1: Запросить у пользователя ввод IP-адреса в формате 10.0.1.1. Ввод данных
# осуществляется в виде строки. В зависимости от типа адреса (описаны ниже), вывести на
# стандартный поток вывода:
# • «unicast» - если первый байт в диапазоне 1-223
# • «multicast» - если первый байт в диапазоне 224-239
# • «local broadcast» - если IP-адрес равен 255.255.255.255
# • «unassigned» - если IP-адрес равен 0.0.0.0
# • «unused» - во всех остальных случаях
# Ограничение: Все задания надо выполнять используя только пройденные темы.


# user_ip = '239.0.1.0'

def check_ip_add(ip_addres):
    octets = [int(octet) for octet in ip_addres.split('.')]
    if 1 <= octets[0] <= 223:
        return "unicast"
    elif 224 <= octets[0] <= 239:
        return "multicast"
    elif ip_addres == '255.255.255.255':
        return "local broadcast"   
    elif ip_addres == '0.0.0.0':
        return "unassigned"
          
    else:
        return 'unused'


user_ip = input("введи ip в формате 10.0.0.1")

result = check_ip_add(user_ip)
print(f"тип {result}")


