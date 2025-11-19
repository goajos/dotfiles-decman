from decman import File, Module

from config import USER


class OpenRGB(Module):
    def __init__(self):
        super().__init__(name="openrgb", enabled=True, version="1")

    def files(self) -> dict[str, File]:
        return {
            f"/home/{USER}/.config/OpenRGB/1s-white-breathing.orp": File(
                source_file="openrgb/1s-white-breathing.orp"
            ),
            f"/home/{USER}/.config/systemd/user/openrgb.service": File(
                source_file="systemd/user/openrgb.service"
            ),
        }

    def pacman_packages(self) -> list[str]:
        return [
            "openrgb",  # Open source RGB lighting control that doesn't depend on manufacturer software
        ]

    def systemd_user_units(self) -> dict[str, list[str]]:
        return {
            f"{USER}": [
                "openrgb.service",
            ]
        }
