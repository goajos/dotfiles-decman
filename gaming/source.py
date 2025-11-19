from decman import Directory, File, Module

from config import USER


class Gaming(Module):
    def __init__(self):
        super().__init__(name="gaming", enabled=True, version="1")

    def directories(self) -> dict[str, Directory]:
        return {
            f"/home/{USER}/Pictures": Directory(source_directory="gaming/icons"),
            f"/home/{USER}/.local/share/wine": Directory(
                source_directory="gaming/wine",
                permissions=0o755,
            ),
        }

    def pacman_packages(self) -> list[str]:
        return [
            "lib32-vulkan-intel",  # Open-source Vulkan driver for Intel GPUs - 32-bit
            "umu-launcher",  # The Unified Launcher for Windows Games on Linux, to run Proton with fixes outside of Steam
            "vulkan-intel",  # Open-source Vulkan driver for Intel GPUs
        ]
