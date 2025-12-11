#!/usr/bin/env python
from decman import Directory, Module

from config import USER


class Nvim(Module):
    def __init__(self):
        super().__init__(name="nvim", enabled=True, version="1")

    def directories(self) -> dict[str, Directory]:
        return {
            f"/home/{USER}/.config/nvim/": Directory(
                source_directory="nvim/nvim", permissions=0o755, owner=USER
            )
        }

    def aur_packages(self) -> list[str]:
        return [
            "neovim-nightly-bin",  # NeoVim nightly build
        ]

    def pacman_packages(self) -> list[str]:
        return [
            "ripgrep", # A search tool that combines the usability of ag with the raw speed of grep
        ]
