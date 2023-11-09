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



class MyDict(dict):
    def get(self, key, default=None):
        return super().get(key, "Такого параметра нет")
# my_dict = {"a": 1, "b": 2}
# new = MyDict(my_dict)
# print(new.get("a"))
# print(new.get("c"))

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


device = (str(london_co.keys())).replace('[', '').replace(']', '').replace('dict_keys', '').replace("'", '')

# print(device)
print(f"Введи имя устройства {device}: ")
a = str(input())

print("\n\n\n")

parameter = (str((london_co.get(a)).keys())).replace('[', '').replace(']', '').replace('dict_keys', '').replace("'", '')
# print(parameter)

print(f"Введи параметр устройства {parameter}: ")
b = str(input())

new_london_co = MyDict(london_co.get(a))

print(new_london_co.get(b))

