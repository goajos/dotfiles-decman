#!/usr/bin/env python
from decman import Module


class Zig(Module):
    def __init__(self):
        super().__init__(name="zig", enabled=True, version="1")

    def pacman_packages(self) -> list[str]:
        return [
            "zig" # a general-purpose programming language and toolchain for maintaining robust, optimal, and reusable software
        ]

