#!/usr/bin/python3
import subprocess
import time

MAC = "FC:91:5D:6C:BB:C5"
CHECK_INTERVAL = 5


def ensure_power_and_trust(mac_address: str):
    subprocess.run(["bluetoothctl", "power", "on"])
    subprocess.run(["bluetoothctl", "agent", "on"])
    subprocess.run(["bluetoothctl", "default-agent"])
    subprocess.run(["bluetoothctl", "trust", mac_address])


def is_connected(mac_address: str) -> bool:
    result = subprocess.run(
        ["bluetoothctl", "info", mac_address],
        capture_output=True,
        text=True,
    )
    return "Connected: yes" in result.stdout


def device_seen(mac_address: str) -> bool:
    result = subprocess.run(
        ["bluetoothctl", "devices"],
        capture_output=True,
        text=True,
    )
    return mac_address in result.stdout


def scan_for_device(mac_address: str) -> bool:
    subprocess.run(["bluetoothctl", "scan", "on"])
    while True:
        if device_seen(mac_address):
            break

    subprocess.run(["bluetoothctl", "scan", "off"])
    return device_seen(mac_address=mac_address)


def main():
    ensure_power_and_trust(mac_address=MAC)
    while True:
        if is_connected(MAC):
            time.sleep(CHECK_INTERVAL)
            continue

        seen = scan_for_device(mac_address=MAC)
        if seen:
            subprocess.run(["bluetoothctl", "connect", MAC])
            time.sleep(CHECK_INTERVAL)
        else:
            time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
