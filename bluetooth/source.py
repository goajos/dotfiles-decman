from decman import File, Module

from config import USER


class Bluetooth(Module):
    def __init__(self):
        super().__init__(name="bluetooth", enabled=True, version="1")

    def files(self) -> dict[str, File]:
        return {
            "/etc/bluetooth/main.conf": File(source_file="bluetooth/main.conf"),
            f"/home/{USER}/.local/bin/auto_connect.py": File(
                source_file="bluetooth/scripts/auto_connect.py", permissions=0o755
            ),
            f"/home/{USER}/.config/systemd/user/auto-connect.service": File(
                source_file="systemd/user/auto-connect.service"
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
            f"{USER}": ["auto-connect.service"],
        }
