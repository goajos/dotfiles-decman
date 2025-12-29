#!/usr/bin/env python
from decman import Directory, File, Module

from config import USER


# TODO: what to do with the .exe files/installers?
# TODO: what to do with app icons?
class Gaming(Module):
    def __init__(self):
        super().__init__(name="gaming", enabled=True, version="1")

    def files(self) -> dict[str, File]:
        return {
            f"/home/{USER}/.local/share/applications/steam_app_default.desktop": File(
                source_file="gaming/steam_app_default/steam_app_default.desktop"
            ),
            f"/home/{USER}/Pictures/steam.png": File(
                source_file="gaming/steam_app_default/steam.png"
            ),
            f"/home/{USER}/.local/share/applications/steam_app_3062740.desktop": File(
                source_file="gaming/galaxy/steam_app_3062740.desktop"
            ),
            f"/home/{USER}/Pictures/galaxy.png": File(
                source_file="gaming/galaxy/galaxy.png"
            ),
        }

    def directories(self) -> dict[str, Directory]:
        return {
            f"/home/{USER}/.local/share/applications/wine": Directory(
                source_directory="gaming/wine"
            ),
        }

    def pacman_packages(self) -> list[str]:
        return [
            "lib32-vulkan-intel",  # Open-source Vulkan driver for Intel GPUs - 32-bit
            "umu-launcher",  # The Unified Launcher for Windows Games on Linux, to run Proton with fixes outside of Steam
            "steam", # Valve's digital software delivery system
            "vulkan-intel",  # Open-source Vulkan driver for Intel GPUs
        ]
