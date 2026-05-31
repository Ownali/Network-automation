# ============================================
# Script 1: Device Inventory
# Author: Own Ali
# Roll No: F20232661030
# Description: Stores all network device info
#              and prints a full inventory report
# ============================================

# Network devices inventory
devices = [
    {
        "hostname": "Router0",
        "type": "Router",
        "model": "Cisco 2911",
        "interfaces": {
            "GigabitEthernet0/0": "192.168.1.1",
            "GigabitEthernet0/1": "10.0.0.1"
        },
        "network": "192.168.1.0/24"
    },
    {
        "hostname": "Router1",
        "type": "Router",
        "model": "Cisco 2911",
        "interfaces": {
            "GigabitEthernet0/0": "192.168.2.1",
            "GigabitEthernet0/1": "10.0.0.2",
            "GigabitEthernet0/2": "10.0.0.5"
        },
        "network": "192.168.2.0/24"
    },
    {
        "hostname": "Router2",
        "type": "Router",
        "model": "Cisco 2911",
        "interfaces": {
            "GigabitEthernet0/0": "192.168.3.1",
            "GigabitEthernet0/1": "10.0.0.6"
        },
        "network": "192.168.3.0/24"
    },
    {
        "hostname": "Switch0",
        "type": "Switch",
        "model": "Cisco 2960",
        "interfaces": {
            "FastEthernet0/1": "PC0",
            "FastEthernet0/2": "PC1",
            "FastEthernet0/3": "Router0"
        },
        "network": "192.168.1.0/24"
    },
    {
        "hostname": "Switch1",
        "type": "Switch",
        "model": "Cisco 2960",
        "interfaces": {
            "FastEthernet0/1": "PC2",
            "FastEthernet0/2": "PC3",
            "FastEthernet0/3": "Router1"
        },
        "network": "192.168.2.0/24"
    },
    {
        "hostname": "Switch2",
        "type": "Switch",
        "model": "Cisco 2960",
        "interfaces": {
            "FastEthernet0/1": "PC4",
            "FastEthernet0/2": "PC5",
            "FastEthernet0/3": "Router2"
        },
        "network": "192.168.3.0/24"
    },
    {
        "hostname": "PC0", "type": "PC", "model": "PC-PT",
        "interfaces": {"FastEthernet0": "192.168.1.10"},
        "network": "192.168.1.0/24"
    },
    {
        "hostname": "PC1", "type": "PC", "model": "PC-PT",
        "interfaces": {"FastEthernet0": "192.168.1.11"},
        "network": "192.168.1.0/24"
    },
    {
        "hostname": "PC2", "type": "PC", "model": "PC-PT",
        "interfaces": {"FastEthernet0": "192.168.2.10"},
        "network": "192.168.2.0/24"
    },
    {
        "hostname": "PC3", "type": "PC", "model": "PC-PT",
        "interfaces": {"FastEthernet0": "192.168.2.11"},
        "network": "192.168.2.0/24"
    },
    {
        "hostname": "PC4", "type": "PC", "model": "PC-PT",
        "interfaces": {"FastEthernet0": "192.168.3.10"},
        "network": "192.168.3.0/24"
    },
    {
        "hostname": "PC5", "type": "PC", "model": "PC-PT",
        "interfaces": {"FastEthernet0": "192.168.3.11"},
        "network": "192.168.3.0/24"
    },
]

# ── Print inventory report ──
def print_inventory():
    print("=" * 55)
    print("       NETWORK DEVICE INVENTORY REPORT")
    print("       Author : Own Ali | Roll: F20232661030")
    print("=" * 55)

    routers = [d for d in devices if d["type"] == "Router"]
    switches = [d for d in devices if d["type"] == "Switch"]
    pcs = [d for d in devices if d["type"] == "PC"]

    print(f"\nTotal Devices  : {len(devices)}")
    print(f"  Routers      : {len(routers)}")
    print(f"  Switches     : {len(switches)}")
    print(f"  PCs          : {len(pcs)}")

    print("\n" + "-" * 55)
    print("ROUTERS")
    print("-" * 55)
    for r in routers:
        print(f"\n  Hostname : {r['hostname']}  ({r['model']})")
        print(f"  Network  : {r['network']}")
        for iface, ip in r["interfaces"].items():
            print(f"    {iface:30s} -> {ip}")

    print("\n" + "-" * 55)
    print("SWITCHES")
    print("-" * 55)
    for s in switches:
        print(f"\n  Hostname : {s['hostname']}  ({s['model']})")
        print(f"  Network  : {s['network']}")
        for iface, connected in s["interfaces"].items():
            print(f"    {iface:30s} -> {connected}")

    print("\n" + "-" * 55)
    print("END DEVICES (PCs)")
    print("-" * 55)
    for pc in pcs:
        ip = list(pc["interfaces"].values())[0]
        print(f"  {pc['hostname']:6s}  IP: {ip:16s}  Network: {pc['network']}")

    print("\n" + "=" * 55)
    print("  Inventory report complete.")
    print("=" * 55)

if __name__ == "__main__":
    print_inventory()