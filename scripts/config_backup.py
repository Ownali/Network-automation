# ============================================
# Script 4: Configuration Backup
# Author: Own Ali
# Roll No: F20232661030
# Description: Simulates pulling running-config
#              from all routers and saves them
#              as timestamped backup files in
#              the configs/backups folder
# ============================================

import os
import datetime

# ── Router configurations (simulated running-config) ──
router_configs = {
    "Router0": """
!==================================================
! Running Configuration - Router0
! Backed up: {timestamp}
! Author   : Own Ali | F20232661030
!==================================================

version 15.1
hostname Router0

!
interface GigabitEthernet0/0
 description LAN - Switch0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
!
interface GigabitEthernet0/1
 description WAN - Link to Router1
 ip address 10.0.0.1 255.255.255.252
 no shutdown
!
router ospf 1
 network 192.168.1.0 0.0.0.255 area 0
 network 10.0.0.0 0.0.0.3 area 0
!
end
""",

    "Router1": """
!==================================================
! Running Configuration - Router1
! Backed up: {timestamp}
! Author   : Own Ali | F20232661030
!==================================================

version 15.1
hostname Router1

!
interface GigabitEthernet0/0
 description LAN - Switch1
 ip address 192.168.2.1 255.255.255.0
 no shutdown
!
interface GigabitEthernet0/1
 description WAN - Link to Router0
 ip address 10.0.0.2 255.255.255.252
 no shutdown
!
interface GigabitEthernet0/2
 description WAN - Link to Router2
 ip address 10.0.0.5 255.255.255.252
 no shutdown
!
router ospf 1
 network 192.168.2.0 0.0.0.255 area 0
 network 10.0.0.0 0.0.0.3 area 0
 network 10.0.0.4 0.0.0.3 area 0
!
end
""",

    "Router2": """
!==================================================
! Running Configuration - Router2
! Backed up: {timestamp}
! Author   : Own Ali | F20232661030
!==================================================

version 15.1
hostname Router2

!
interface GigabitEthernet0/0
 description LAN - Switch2
 ip address 192.168.3.1 255.255.255.0
 no shutdown
!
interface GigabitEthernet0/1
 description WAN - Link to Router1
 ip address 10.0.0.6 255.255.255.252
 no shutdown
!
router ospf 1
 network 192.168.3.0 0.0.0.255 area 0
 network 10.0.0.4 0.0.0.3 area 0
!
end
"""
}

# ── Backup a single router config ──
def backup_router(hostname, config_template, timestamp, backup_dir):
    config = config_template.format(timestamp=timestamp)
    date_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(backup_dir, f"{hostname}_backup_{date_str}.txt")
    with open(filename, "w") as f:
        f.write(config)
    return filename

# ── Main ──
def main():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    backup_dir = os.path.join("configs", "backups")
    os.makedirs(backup_dir, exist_ok=True)

    print("=" * 55)
    print("       CONFIGURATION BACKUP SCRIPT")
    print("       Author : Own Ali | Roll: F20232661030")
    print(f"       Time   : {timestamp}")
    print("=" * 55)
    print()

    backed_up = []
    for hostname, config in router_configs.items():
        filepath = backup_router(hostname, config, timestamp, backup_dir)
        backed_up.append(filepath)
        print(f"  [OK] {hostname} backup saved -> {filepath}")

    print()
    print("-" * 55)
    print(f"  Total backups created : {len(backed_up)}")
    print(f"  Backup location       : {backup_dir}/")
    print("-" * 55)

    # Save backup log
    log_file = os.path.join("docs", "backup_log.txt")
    os.makedirs("docs", exist_ok=True)
    with open(log_file, "a") as log:
        log.write(f"\n[{timestamp}] Backup completed\n")
        for path in backed_up:
            log.write(f"  -> {path}\n")

    print(f"\n  Backup log updated  -> {log_file}")
    print()
    print("  Backup completed successfully.")
    print("=" * 55)

if __name__ == "__main__":
    main()