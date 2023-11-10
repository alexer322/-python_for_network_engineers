# Задание 4 Переделать скрипт из задания 3 таким образом, чтобы, при запросе параметра,
# которого нет в словаре устройства, отображалось сообщение 'Такого параметра нет'.
# Задание относится только к параметрам устройств, не к самим устройствам.
# > Попробуйте набрать неправильное имя параметра или несуществующий параметр,
# > чтобы увидеть какой будет результат. А затем выполняйте задание.
# Если выбран существующий параметр, вывести информацию о соответствующем
# параметре, указанного устройства.
# Пример выполнения скрипта:
# $ python task_5_1c.py
# Введите имя устройства: r1
# Введите имя параметра (ios, model, vendor, location, ip): ips
# Такого параметра нет


london_co = {
"r1": {
"location": "21 New Globe Walk",
"vendor": "Cisco",
"model": "4451",
"ios": "15.4",
"ip": "10.255.0.1",
},
"r2": {
"location": "21 New Globe Walk",
"vendor": "Cisco",
"model": "4451",
"ios": "15.4",
"ip": "10.255.0.2",
},
"sw1": {
"location": "21 New Globe Walk",
"vendor": "Cisco",
"model": "3850",
"ios": "3.6.XE",
"ip": "10.255.0.101",
"vlans": "10,20,30",
"routing": True,
},
}


# a = str(tuple(london_co.keys())).replace("'", '')
# device = input(f"Введи имя устройства {a} : ")

# b = str(tuple(london_co.get(device).keys())).replace("'", '')
# parameter = input(f"Введи параметр устройства {b} : ")

device = input(f"Введи имя устройства ({', '.join(london_co.keys())}) : ")
device_param = london_co.get(device)

parameter = input(f"Введи параметр устройства ({', '.join(london_co.get(device).keys())}) : ")
value = device_param.get(parameter, "Такого параметра нет")

print(value)
