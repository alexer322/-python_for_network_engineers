# В скрипте сделан генератор конфигурации для access-портов. Сделать
# аналогичный генератор конфигурации для портов trunk. В транках ситуация усложняется
# тем, что VLANов может быть много, и надо понимать, что с ним делать. Поэтому в
# соответствии каждому порту стоит список и первый (нулевой) элемент списка указывает
# как воспринимать номера VLAN, которые идут дальше.

access_template = [
"switchport mode access",
"switchport access vlan",
"spanning-tree portfast",
"spanning-tree bpduguard enable",
]

trunk_template = [
"switchport trunk encapsulation dot1q",
"switchport mode trunk",
"switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}


for intf, vlan in access.items():
    print(f"interface FastEthernet {intf}")

    for command in access_template:
        if command.endswith("access vlan"):
            print(f" {command} {vlan}")
        else:
            print(f" {command}")
    print('\n')

print("trunk options\n")

for intf, vlan_list in trunk.items():
    print(f"interface FastEthernet {intf}")

    for command in trunk_template:
        if command.endswith("allowed vlan"):
            option = vlan_list[0]
            # print(option)
            vlans = ",".join(vlan_list[1:])
            # print(vlans)
            if option == "add":
                print(f" {command} add {vlans}")
            elif option == "del":
                print(f" {command} remove {vlans}")
            elif option == "only":
                print(f" {command} {vlans}")
        else:
            print(f" {command}")
    print('\n')
