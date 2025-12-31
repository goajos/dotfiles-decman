#!/usr/bin/env python
from decman import Directory, Module

from config import USER

class Raylib(Module):
    def __init__(self):
        super().__init__(name="raylib", enabled=True, version="1")

    def aur_packages(self) -> list[str]:
        return [
        ]

    def pacman_packages(self) -> list[str]:
        return [
            # libglvnd,
            # libx11,
            "raylib", # Simple and easy-to-use game programming library
        ]
