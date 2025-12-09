#!/usr/bin/env python
from decman import Directory, File, Module, sh

from config import USER


# TODO: clickable waybar module to run decman?
class Waybar(Module):
    def __init__(self):
        super().__init__(name="waybar", enabled=True, version="1")

    def files(self) -> dict[str, File]:
        return {
            f"/home/{USER}/.config/waybar/config.jsonc": File(
                source_file="waybar/config.jsonc"
            ),
            f"/home/{USER}/.config/waybar/style.css": File(
                source_file="waybar/style.css"
            ),
            f"/home/{USER}/.config/systemd/user/waybar.service": File(
                source_file="systemd/user/waybar.service"
            ),
        }

    def directories(self) -> dict[str, Directory]:
        return {
            f"/home/{USER}/.config/waybar/scripts": Directory(
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

    def systemd_user_units(self) -> dict[str, list[str]]:
        return {
            f"{USER}": [
                "waybar.service",
            ]
        }


class Perf(Module):
    def __init__(self):
        super().__init__(name="perf", enabled=False, version="1")

    def files(self) -> dict[str, File]:
        return {
            "/etc/udev/rules.d/99-turbostat.rules": File(
                source_file="waybar/perf/99-turbostat.rules"
            ),
        }

    def on_enable(self) -> None:
        sh("groupadd -r msr")
        sh(f"usermod -a -G msr {USER}")
        sh("setcap cap_perfmon=+ep /usr/bin/intel_gpu_top")
        sh("setcap cap_sys_admin,cap_sys_rawio,cap_sys_nice=+ep /usr/bin/turbostat")
        sh("udevadm control -R")
