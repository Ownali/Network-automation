# ============================================
# Script 2: Configuration Generator
# Author: Own Ali
# Roll No: F20232661030
# Description: Automatically generates Cisco IOS
#              configuration commands for all routers
#              and saves them to the configs folder
# ============================================

import os
import datetime

# ── Device configuration data ──
routers = [
    {
        "hostname": "Router0",
        "interfaces": [
            {
                "name": "GigabitEthernet0/0",
                "ip": "192.168.1.1",
                "mask": "255.255.255.0",
                "description": "LAN - Switch0"
            },
            {
                "name": "GigabitEthernet0/1",
                "ip": "10.0.0.1",
                "mask": "255.255.255.252",
                "description": "WAN - Link to Router1"
            }
        ],
        "ospf_networks": [
            ("192.168.1.0", "0.0.0.255"),
            ("10.0.0.0",    "0.0.0.3")
        ]
    },
    {
        "hostname": "Router1",
        "interfaces": [
            {
                "name": "GigabitEthernet0/0",
                "ip": "192.168.2.1",
                "mask": "255.255.255.0",
                "description": "LAN - Switch1"
            },
            {
                "name": "GigabitEthernet0/1",
                "ip": "10.0.0.2",
                "mask": "255.255.255.252",
                "description": "WAN - Link to Router0"
            },
            {
                "name": "GigabitEthernet0/2",
                "ip": "10.0.0.5",
                "mask": "255.255.255.252",
                "description": "WAN - Link to Router2"
            }
        ],
        "ospf_networks": [
            ("192.168.2.0", "0.0.0.255"),
            ("10.0.0.0",    "0.0.0.3"),
            ("10.0.0.4",    "0.0.0.3")
        ]
    },
    {
        "hostname": "Router2",
        "interfaces": [
            {
                "name": "GigabitEthernet0/0",
                "ip": "192.168.3.1",
                "mask": "255.255.255.0",
                "description": "LAN - Switch2"
            },
            {
                "name": "GigabitEthernet0/1",
                "ip": "10.0.0.6",
                "mask": "255.255.255.252",
                "description": "WAN - Link to Router1"
            }
        ],
        "ospf_networks": [
            ("192.168.3.0", "0.0.0.255"),
            ("10.0.0.4",    "0.0.0.3")
        ]
    }
]

# ── Generate IOS config for one router ──
def generate_config(router):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = []

    lines.append("!" + "=" * 50)
    lines.append(f"! Device    : {router['hostname']}")
    lines.append(f"! Generated : {timestamp}")
    lines.append(f"! Author    : Own Ali | F20232661030")
    lines.append("!" + "=" * 50)
    lines.append("")
    lines.append("enable")
    lines.append("configure terminal")
    lines.append("")

    # Hostname
    lines.append(f"hostname {router['hostname']}")
    lines.append("")

    # Interfaces
    for iface in router["interfaces"]:
        lines.append(f"interface {iface['name']}")
        lines.append(f" description {iface['description']}")
        lines.append(f" ip address {iface['ip']} {iface['mask']}")
        lines.append(f" no shutdown")
        lines.append("!")

    lines.append("")

    # OSPF
    lines.append("router ospf 1")
    for network, wildcard in router["ospf_networks"]:
        lines.append(f" network {network} {wildcard} area 0")
    lines.append("!")
    lines.append("")
    lines.append("end")
    lines.append("write memory")
    lines.append("")

    return "\n".join(lines)

# ── Save config to file ──
def save_config(hostname, config_text):
    os.makedirs("configs", exist_ok=True)
    filename = f"configs/{hostname}_config.txt"
    with open(filename, "w") as f:
        f.write(config_text)
    return filename

# ── Main ──
def main():
    print("=" * 55)
    print("       CISCO IOS CONFIGURATION GENERATOR")
    print("       Author : Own Ali | Roll: F20232661030")
    print("=" * 55)
    print()

    for router in routers:
        config = generate_config(router)
        filepath = save_config(router["hostname"], config)
        print(f"  [OK] {router['hostname']} config saved -> {filepath}")

    print()
    print("-" * 55)
    print("  All configurations generated successfully.")
    print("  Files saved in the configs/ folder.")
    print("-" * 55)
    print()

    # Preview Router0 config
    print("  PREVIEW - Router0 Configuration:")
    print("-" * 55)
    with open("configs/Router0_config.txt", "r") as f:
        print(f.read())

if __name__ == "__main__":
    main()