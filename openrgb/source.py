from decman import File, Module


# TODO: set this up as a system service like bluetooth/NetworkManager?
class OpenRGB(Module):
    def __init__(self):
        super().__init__(name="openrgb", enabled=True, version="1")

    def files(self) -> dict[str, File]:
        return {
            "home/jappe/.config/OpenRGB/1s-white-breathing.orp": File(
                source_file="openrgb/1s-white-breathing.orp"
            ),
        }

    def pacman_packages(self) -> list[str]:
        return [
            "openrgb",  # Open source RGB lighting control that doesn't depend on manufacturer software
        ]

    def systemd_units(self) -> list[str]:
        return [
            "openrgb.service",
        ]
