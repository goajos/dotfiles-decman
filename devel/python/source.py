#!/usr/bin/env python
from decman import Module, sh


class Python(Module):
    def __init__(self):
        super().__init__(name="python", enabled=True, version="1")

    def pacman_packages(self) -> list[str]:
        return [
            "python",  # The Python programming language
            "uv",  # An extremely fast Python package installer and resolver written in Rust
        ]

    def on_enable(self) -> None:
        sh("uv tool install --editable /home/jappe/Repositories/bt-auto-connect")
        sh("uv tool install --editable /home/jappe/Repositories/idle-inhibitor")
