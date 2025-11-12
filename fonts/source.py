from decman import File, Module


class Fonts(Module):
    def __init__(self):
        super().__init__(name="fonts", enabled=True, version="1")

    # TODO: what to do with installing the fonts?
    def files(self) -> dict[str, File]:
        return {
            "/home/jappe/.config/fontconfig/fonts.conf": File(
                source_file="fonts/fonts.conf"
            ),
        }
