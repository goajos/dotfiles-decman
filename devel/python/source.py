from decman import Module


class Python(Module):
    def __init__(self):
        super().__init__(name="python", enabled=True, version="1")

    # TODO: check the python .local/bin script?
    def pacman_packages(self) -> list[str]:
        return [
            "python",  # The Python programming language
            "uv",  # An extremely fast Python package installer and resolver written in Rust
        ]
