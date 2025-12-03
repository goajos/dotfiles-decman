#!/usr/bin/python3
import subprocess
import time

MAC = "FC:91:5D:6C:BB:C5"
CONNECT_COOLDOWN = 5
SLEEP_TIMER = 1


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


def ensure_power_and_agent():
    subprocess.run(["bluetoothctl", "power", "on"])
    subprocess.run(["bluetoothctl", "agent", "on"])
    subprocess.run(["bluetoothctl", "default-agent"])


def trust_device(mac_address: str):
    subprocess.run(["bluetoothctl", "trust", mac_address])


def scan_on():
    subprocess.run(["bluetoothctl", "scan", "on"])


def main():
    ensure_power_and_agent()
    trust_device(mac_address=MAC)
    scan_on()

    while True:
        if device_seen(mac_address=MAC):
            if not is_connected(mac_address=MAC):
                print(f"auto-connect: Connecting to device {MAC}...")
                subprocess.run(["bluetoothctl", "connect", MAC])
                time.sleep(CONNECT_COOLDOWN)
            else:
                time.sleep(SLEEP_TIMER)
        else:
            time.sleep(SLEEP_TIMER)


if __name__ == "__main__":
    main()
