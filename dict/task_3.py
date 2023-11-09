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


device=(str(london_co.keys())).replace('[', '').replace(']', '').replace('dict_keys', '').replace("'", '')
print(device)
print(device)

print("Введи имя устройства", (device), ": ")
a=str(input())

print("\n\n\n\n\n")

parameter=(str((london_co.get(a)).keys())).replace('[', '').replace(']', '').replace('dict_keys', '').replace("'", '')



print("Введи параметр устройства", (parameter), ": ")
b=str(input())


print((london_co.get(a)).get(b))

