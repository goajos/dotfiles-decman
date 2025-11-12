from decman import Directory, File, Module


class Waybar(Module):
    def __init__(self):
        super().__init__(name="waybar", enabled=True, version="1")

    def files(self) -> dict[str, File]:
        return {
            "home/jappe/.config/waybar/config.jsonc": File(
                source_file="waybar/config.jsonc"
            ),
            "home/jappe/.config/waybar/style.css": File(source_file="waybar/style.css"),
        }

    def directories(self) -> dict[str, Directory]:
        return {
            "/home/jappe/.config/waybar/scripts": Directory(
                source_directory="waybar/scripts"
            )
        }

    def pacman_packages(self) -> list[str]:
        return [
            "bc",  # An arbitrary precision calculator language
            "intel-gpu-tools",  # Tools for development and testing of the Intel DRM driver
            "turbostat",  # Report processor frequency and idle statistics
            "waybar",  # Highly customizable Wayland bar for Sway and Wlroots based compositors
        ]

    def systemd_units(self) -> list[str]:
        return ["waybar.service"]
