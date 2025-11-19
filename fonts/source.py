from decman import Directory, File, Module


# TODO: set the gnome fonts here or in Gnome module?
class Fonts(Module):
    def __init__(self):
        super().__init__(name="fonts", enabled=True, version="1")

    def files(self) -> dict[str, File]:
        return {
            "/home/jappe/.config/fontconfig/fonts.conf": File(
                source_file="fonts/fonts.conf"
            ),
        }

    def directories(self) -> dict[str, Directory]:
        return {
            "/usr/local/share/fonts/ttf/JetBrainsMono": Directory(
                source_directory="fonts/JetBrainsMono"
            ),
            "/usr/local/share/fonts/ttf/Noto": Directory(source_directory="fonts/Noto"),
        }
