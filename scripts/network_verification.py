# ============================================
# Script 3: Network Verification
# Author: Own Ali
# Roll No: F20232661030
# Description: Pings all devices in the network,
#              logs pass/fail results and saves
#              a verification report to docs folder
# ============================================

import os
import datetime
import subprocess
import platform

# ── All devices to test ──
targets = [
    # Routers
    {"name": "Router0 - LAN",      "ip": "192.168.1.1"},
    {"name": "Router0 - WAN",      "ip": "10.0.0.1"},
    {"name": "Router1 - LAN",      "ip": "192.168.2.1"},
    {"name": "Router1 - WAN0",     "ip": "10.0.0.2"},
    {"name": "Router1 - WAN1",     "ip": "10.0.0.5"},
    {"name": "Router2 - LAN",      "ip": "192.168.3.1"},
    {"name": "Router2 - WAN",      "ip": "10.0.0.6"},
    # PCs
    {"name": "PC0",                "ip": "192.168.1.10"},
    {"name": "PC1",                "ip": "192.168.1.11"},
    {"name": "PC2",                "ip": "192.168.2.10"},
    {"name": "PC3",                "ip": "192.168.2.11"},
    {"name": "PC4",                "ip": "192.168.3.10"},
    {"name": "PC5",                "ip": "192.168.3.11"},
]

# ── Ping a single IP ──
def ping(ip):
    system = platform.system().lower()
    if system == "windows":
        cmd = ["ping", "-n", "2", "-w", "1000", ip]
    else:
        cmd = ["ping", "-c", "2", "-W", "1", ip]
    try:
        result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return result.returncode == 0
    except Exception:
        return False

# ── Run verification on all targets ──
def run_verification():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    results = []

    print("=" * 55)
    print("       NETWORK VERIFICATION REPORT")
    print("       Author : Own Ali | Roll: F20232661030")
    print(f"       Time   : {timestamp}")
    print("=" * 55)
    print()

    for target in targets:
        status = ping(target["ip"])
        result = "PASS" if status else "FAIL"
        results.append({
            "name": target["name"],
            "ip": target["ip"],
            "result": result
        })
        symbol = "[PASS]" if status else "[FAIL]"
        print(f"  {symbol}  {target['name']:25s}  {target['ip']}")

    # Summary
    passed = sum(1 for r in results if r["result"] == "PASS")
    failed = sum(1 for r in results if r["result"] == "FAIL")
    total  = len(results)

    print()
    print("-" * 55)
    print(f"  Total  : {total}")
    print(f"  Passed : {passed}")
    print(f"  Failed : {failed}")

    if failed == 0:
        print("  Status : ALL DEVICES REACHABLE")
    else:
        print("  Status : SOME DEVICES UNREACHABLE - CHECK CONFIG")
    print("-" * 55)

    return results, timestamp, passed, failed, total

# ── Save report to docs folder ──
def save_report(results, timestamp, passed, failed, total):
    os.makedirs("docs", exist_ok=True)
    date_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"docs/verification_report_{date_str}.txt"

    with open(filename, "w") as f:
        f.write("=" * 55 + "\n")
        f.write("       NETWORK VERIFICATION REPORT\n")
        f.write("       Author : Own Ali | Roll: F20232661030\n")
        f.write(f"       Time   : {timestamp}\n")
        f.write("=" * 55 + "\n\n")

        f.write(f"  {'Device':<25}  {'IP':<18}  {'Result'}\n")
        f.write("-" * 55 + "\n")
        for r in results:
            f.write(f"  {r['name']:<25}  {r['ip']:<18}  {r['result']}\n")

        f.write("\n" + "-" * 55 + "\n")
        f.write(f"  Total  : {total}\n")
        f.write(f"  Passed : {passed}\n")
        f.write(f"  Failed : {failed}\n")
        overall = "ALL DEVICES REACHABLE" if failed == 0 else "SOME DEVICES UNREACHABLE"
        f.write(f"  Status : {overall}\n")
        f.write("-" * 55 + "\n")

    print(f"\n  Report saved -> {filename}")
    return filename

# ── Main ──
if __name__ == "__main__":
    results, timestamp, passed, failed, total = run_verification()
    save_report(results, timestamp, passed, failed, total)