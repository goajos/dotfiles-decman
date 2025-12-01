from decman import Module, sh

from config import USER


class Docker(Module):
    def __init__(self):
        super().__init__(name="docker", enabled=True, version="1")

    def pacman_packages(self) -> list[str]:
        return [
            "docker",  # Pack, ship and run any application as a lightweight container
        ]

    def on_enable(self) -> None:
        sh("groupadd -r docker")
        sh(f"usermod -a -G docker {USER}")

    def systemd_units(self) -> list[str]:
        return ["docker.service", "docker.socket"]
