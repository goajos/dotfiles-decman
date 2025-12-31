#!/usr/bin/env python
from decman import Directory, Module

from config import USER

class CSharp(Module):
    def __init__(self):
        super().__init__(name="csharp", enabled=True, version="1")

    # TODO: copy the .dll to the local bin folder with decman?
    def pacman_packages(self) -> list[str]:
        return [
            "dotnet-sdk", # The .NET Core SDK
        ]
