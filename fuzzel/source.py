from decman import File, Module


class Fuzzel(Module):
    def __init__(self):
        super().__init__(name="fuzzel", enabled=True, version="1")

    def files(self) -> dict[str, File]:
        return {
            "home/jappe/.config/fuzzel/fuzzel.ini": File(
                source_file="fuzzel/fuzzel.ini"
            ),
        }

    def pacman_packages(self) -> list[str]:
        return [
            "fuzzel",  # Application launcher for wlroots based Wayland compositors
        ]
