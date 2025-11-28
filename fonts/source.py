from decman import Directory, File, Module

from config import USER


# TODO: run fc-cache command?
class Fonts(Module):
    def __init__(self):
        super().__init__(name="fonts", enabled=True, version="1")

    def files(self) -> dict[str, File]:
        return {
            f"/home/{USER}/.config/fontconfig/fonts.conf": File(
                source_file="fonts/fonts.conf"
            ),
            f"/home/{USER}/.local/bin/dconf.sh": File(
                source_file="fonts/dconf.sh", permissions=0o755
            ),
        }

    def directories(self) -> dict[str, Directory]:
        return {
            "/usr/local/share/fonts/ttf/JetBrainsMono": Directory(
                source_directory="fonts/JetBrainsMono"
            ),
            "/usr/local/share/fonts/ttf/Noto": Directory(source_directory="fonts/Noto"),
        }
