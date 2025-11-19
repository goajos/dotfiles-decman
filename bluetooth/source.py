from decman import File, Module


class Bluetooth(Module):
    def __init__(self):
        super().__init__(name="bluetooth", enabled=True, version="1")

    def files(self) -> dict[str, File]:
        return {
            "/etc/bluetooth/main.conf": File(source_file="bluetooth/main.conf"),
        }

    def pacman_packages(self) -> list[str]:
        return [
            "bluez",  # Daemons for the bluetooth protocol stack
            "bluez-utils",  # Development and debugging utilities for the bluetooth protocol stack
        ]

    def systemd_units(self) -> list[str]:
        return ["bluetooth.service"]
