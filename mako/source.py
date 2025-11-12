from decman import File, Module


class Mako(Module):
    def __init__(self):
        super().__init__(name="mako", enabled=True, version="1")

    def files(self) -> dict[str, File]:
        return {
            "home/jappe/.config/mako/config": File(source_file="mako/config"),
        }

    def pacman_packages(self) -> list[str]:
        return [
            "mako",  # Lightweight notification daemon for Wayland
        ]

    def systemd_units(self) -> list[str]:
        return [
            "mako.service",
        ]
