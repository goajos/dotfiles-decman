from decman import File, Module

from config import USER


class Nvim(Module):
    def __init__(self):
        super().__init__(name="nvim", enabled=True, version="1")

    def files(self) -> dict[str, File]:
        return {
            f"/home/{USER}/.config/nvim/init.lua": File(source_file="nvim/init.lua"),
        }

    def pacman_packages(self) -> list[str]:
        return [
            "neovim",  # Fork of Vim aiming to improve user experience, plugins, and GUIs
        ]
