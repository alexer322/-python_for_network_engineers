# Задание 2: Сделать копию скрипта задания 1 Добавить проверку введенного IP-адреса.
# Адрес считается корректно заданным, если он:
# • состоит из 4 чисел (а не букв или других символов)
# • числа разделенны точкой
# • каждое число в диапазоне от 0 до 255
# Если адрес задан неправильно, выводить сообщение: «Неправильный IP-адрес».
# Сообщение «Неправильный IP-адрес» должно выводиться только один раз, даже если
# несколько пунктов выше не выполнены.

# tuple = (True, 1, 0)
# x = all(tuple)
# print(x)

# user_ip = '99.0.1.255'

def check_on_valid(ip_addres):
    try:
        octets = [int(octet) for octet in ip_addres.split('.')]
        return len(octets) == 4 and all(0 <= octet <= 255 for octet in octets)
    
    except ValueError:
        return False
    
def check_ip_add(ip_addres):
    if not check_on_valid(ip_addres):
        return "неправильный ip"

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

user_ip = input("введи ip в формате 10.0.0.1\n")

result = check_ip_add(user_ip)
print(f"{result}")

