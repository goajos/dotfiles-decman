from decman import File, Module

from config import USER


class Misc(Module):
    def __init__(self):
        super().__init__(name="misc", enabled=True, version="1")

    def files(self) -> dict[str, File]:
        return {
            f"/home/{USER}/.config/Code/User/keybindings.json": File(
                source_file="misc/code/keybindings.json"
            ),
            f"/home/{USER}/.config/Code/User/settings.json": File(
                source_file="misc/code/settings.json"
            ),
            f"/home/{USER}/.config/discord/settings.json": File(
                source_file="misc/discord/settings.json"
            ),
            # minimal ruff pyproject.toml
            f"/home/{USER}/.config/ruff/pyproject.toml": File(
                source_file="misc/code/pyproject.toml"
            ),
        }

    def aur_packages(self) -> list[str]:
        return [
            "visual-studio-code-bin",  # Visual Studio Code (vscode) official binary version
        ]

    def pacman_packages(self) -> list[str]:
        return [
            "bitwarden",  # A secure and free password manager for all of your devices
            "discord",  # All-in-one voice and text chat for gamers
            "firefox",  # Fast, Private & Safe Web Browser
            "thunderbird",  # Standalone mail and news reader from mozilla.org
        ]
