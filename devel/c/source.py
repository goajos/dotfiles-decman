#!/usr/bin/env python
from decman import Module


class C(Module):
    def __init__(self):
        super().__init__(name="c", enabled=True, version="1")

    def pacman_packages(self) -> list[str]:
        return [
            "clang" # C language family frontend for LLVM
        ]
