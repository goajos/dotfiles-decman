from decman import Directory, File, Module

from config import USER


class Nvim(Module):
    def __init__(self):
        super().__init__(name="nvim", enabled=True, version="1")

    def files(self) -> dict[str, File]:
        return {
            f"/home/{USER}/.config/nvim/init.lua": File(source_file="nvim/init.lua"),
        }

    def directories(self) -> dict[str, Directory]:
        return {
            f"/home/{USER}/.config/nvim/lsp": Directory(source_directory="nvim/lsp")
        }

    def aur_packages(self) -> list[str]:
        return [
            "ty",  # An extremely fast Python type checker and language server, written in Rust.
        ]

    def pacman_packages(self) -> list[str]:
        return [
            "lua-language-server",  # Lua Language Server coded by Lua
            "neovim",  # Fork of Vim aiming to improve user experience, plugins, and GUIs
            "ripgrep",  # A search tool that combines the usability of ag with the raw speed of grep
            "ruff",  # An extremely fast Python linter, written in Rust
            "rust-analyzer",  # Rust compiler front-end for IDEs
            "typescript-language-server",  # Language Server Protocol (LSP) implementation for TypeScript using tsserver
        ]
