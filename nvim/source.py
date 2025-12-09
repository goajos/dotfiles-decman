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
            "ty",  # An extremely fast Python type checker and language server, written in Rust.
        ]

    def pacman_packages(self) -> list[str]:
        return [
            "fd",  # Simple, fast and user-friendly alternative to find
            "fzf",  # Command-line fuzzy finder
            "lua-language-server",  # Lua Language Server coded by Lua
            # "neovim",  # Fork of Vim aiming to improve user experience, plugins, and GUIs
            "ripgrep",  # A search tool that combines the usability of ag with the raw speed of grep
            "ruff",  # An extremely fast Python linter, written in Rust
            "rust-analyzer",  # Rust compiler front-end for IDEs
            "typescript-language-server",  # Language Server Protocol (LSP) implementation for TypeScript using tsserver
        ]
