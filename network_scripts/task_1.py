# Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
# Функция ожидает как аргумент список IP-адресов.
# Функция должна возвращать кортеж с двумя списками:
# * список доступных IP-адресов
# * список недоступных IP-адресов
# Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
# IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
# Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
# но для задания нужно проверять именно код. Это сделано для упрощения тестов.


import subprocess

def ping(ip_addresses):
    reachable_ip = []
    unreachable_ip = []

    for ip in ip_addresses:
        command = ['ping', ip] 
        print(command)
        try:
            d = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            print(d)
            reachable_ip.append(ip)
        except subprocess.CalledProcessError:
            unreachable_ip.append(ip)

    return reachable_ip, unreachable_ip



ip_list = ['192.168.1.1','33333.4444.5555' ,'8.8.8.8', '10.0.0.1', '8583', 'yandex.ru']
print(ip_list)
reachable, unreachable = ping(ip_list)

print("доступные IP-адреса:", reachable)
print("недоступные IP-адреса:", unreachable)


