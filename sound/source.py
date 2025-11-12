import decman

from config import USER

decman.packages += [
    "pavucontrol",  # PulseAudio Volume Control
    "pipewire",  # Low-latency audio/video router and processor
    "pipewire-alsa",  # - ASLA configuration
    "pipewire-audio",  # - Audio support
    "pipewire-pulse",  # - PulseAudio replacement
    "wireplumber",  # Session / policy manager implementation for PipeWire
]
