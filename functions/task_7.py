# Задание 7

# Создать функцию generate_access_config, которая генерирует конфигурацию

# для access-портов.

def generate_access_config(intf_vlan_mapping, access_template):
    result = []
    for interface, vlan in intf_vlan_mapping.items():
        result.append(f"interface {interface}")
        for command in access_template:
            if "vlan" in command:
                result.append(f"{command}, {vlan}")
            else:
                result.append(f"{command}")
    return result
# intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
# {'FastEthernet0/12':10,
# 'FastEthernet0/14':11,
# 'FastEthernet0/16':17}


access_mode_template = [
"switchport mode access",
"switchport access vlan",
"switchport nonegotiate",
"spanning-tree portfast",
"spanning-tree bpduguard enable",
]

access_config = {
"FastEthernet0/12": 10,
"FastEthernet0/14": 11,
"FastEthernet0/16": 17}

access_config_2 = {
"FastEthernet0/03": 100,
"FastEthernet0/07": 101,
"FastEthernet0/09": 107,
}

a = generate_access_config(access_config, access_mode_template)
print(a)

# for i in a:
#     print(i)

b = generate_access_config(access_config_2, access_mode_template)


print(b)

# for i in b:
#     print(i)

