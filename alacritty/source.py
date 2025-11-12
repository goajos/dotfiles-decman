from decman import Directory, File, Module


class Alacritty(Module):
    def __init__(self):
        super().__init__(name="alacritty", enabled=True, version="1")

    def files(self) -> dict[str, File]:
        return {
            "home/jappe/.config/alacritty/alacritty.toml": File(
                source_file="alacritty/alacritty.toml"
            ),
        }

    def directories(self) -> dict[str, Directory]:
        return {
            "/home/jappe/.config/alacritty/themes": Directory(
                source_directory="alacritty/themes"
            )
        }

    def pacman_packages(self) -> list[str]:
        return [
            "alacritty",  # A cross-platform, GPU-accelerated terminal emulator
        ]
