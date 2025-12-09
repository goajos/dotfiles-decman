#!/usr/bin/env python
from decman import File, Module

from config import USER


class Mako(Module):
    def __init__(self):
        super().__init__(name="mako", enabled=True, version="1")

    def files(self) -> dict[str, File]:
        return {
            f"/home/{USER}/.config/mako/config": File(source_file="mako/config"),
            f"/home/{USER}/.config/systemd/user/mako.service": File(
                source_file="systemd/user/mako.service"
            ),
        }

    def pacman_packages(self) -> list[str]:
        return [
            "mako",  # Lightweight notification daemon for Wayland
        ]

    def systemd_user_units(self) -> dict[str, list[str]]:
        return {
            f"{USER}": [
                "mako.service",
            ]
        }
