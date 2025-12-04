from decman import File, Module

from config import USER


class Bluetooth(Module):
    def __init__(self):
        super().__init__(name="bluetooth", enabled=True, version="1")

    def files(self) -> dict[str, File]:
        return {
            "/etc/bluetooth/main.conf": File(source_file="bluetooth/main.conf"),
            f"/home/{USER}/.config/systemd/user/bt-auto-connect.service": File(
                source_file="systemd/user/bt-auto-connect.service"
            ),
        }

    def pacman_packages(self) -> list[str]:
        return [
            "bluez",  # Daemons for the bluetooth protocol stack
            "bluez-utils",  # Development and debugging utilities for the bluetooth protocol stack
        ]

    def systemd_units(self) -> list[str]:
        return ["bluetooth.service"]

    def systemd_user_units(self) -> dict[str, list[str]]:
        return {
            f"{USER}": ["bt-auto-connect.service"],
        }
