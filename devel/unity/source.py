#!/usr/bin/env python
from decman import Module, Directory

from config import USER

class Unity(Module):
    def __init__(self):
        super().__init__(name="unity", enabled=True, version="1")

    def aur_packages(self) -> list[str]:
        return [
            "unityhub" # The Unity Hub is a standalone application that streamlines the way you find, download, and manage your Unity Projects and installations.
        ]
