

def generate_access_config(intf_vlan_mapping, access_template, psecurity=None):
    result = []

    for interface, vlan in intf_vlan_mapping.items():
        result.append(f"interface {interface}")

        for command in access_template:
            if "vlan" in command:
                result.append(f"{command} {vlan}")
            else:
                result.append(command)


        if psecurity:
            result.extend(psecurity)

    return result

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
"FastEthernet0/16": 17
}

port_security_template = [
"switchport port-security maximum 2",
"switchport port-security violation restrict",
"switchport port-security",
]



result_no_port_security = generate_access_config(access_config, access_mode_template)

for i in result_no_port_security:
    print(i)


result_port_security = generate_access_config(access_config, access_mode_template, port_security_template)


for i in result_port_security:
    print(i)


