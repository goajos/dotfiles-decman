from decman import File, Module

from config import USER


class Sound(Module):
    def __init__(self):
        super().__init__(name="sound", enabled=True, version="1")

    def files(self) -> dict[str, File]:
        return {
            f"/home/{USER}/.local/bin/wp-vol": File(
                source_file="sound/wp-vol", permissions=0o755
            )
        }

    def pacman_packages(self) -> list[str]:
        return [
            "pavucontrol",  # PulseAudio Volume Control
            "pipewire",  # Low-latency audio/video router and processor
            "pipewire-alsa",  # - ASLA configuration
            "pipewire-audio",  # - Audio support
            "pipewire-pulse",  # - PulseAudio replacement
            "wireplumber",  # Session / policy manager implementation for PipeWire
        ]
