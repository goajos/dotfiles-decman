#!/usr/bin/env python
from decman import Module, sh


class JavaScript(Module):
    def __init__(self):
        super().__init__(name="javascript", enabled=True, version="1")

    def pacman_packages(self) -> list[str]:
        return [
            "npm",  # JavaScript package manager
        ]

    def on_enable(self) -> None:
        sh("npm install -g @angular/cli")
