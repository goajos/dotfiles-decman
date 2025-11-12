from decman import Directory, File, Module


class Niri(Module):
    def __init__(self):
        super().__init__(name="niri", enabled=True, version="1")

    def files(self) -> dict[str, File]:
        return {
            "home/jappe/.config/niri/config.kdl": File(source_file="niri/config.kdl"),
        }

    def directories(self) -> dict[str, Directory]:
        return {
            "/home/jappe/.config/niri/scripts": Directory(
                source_directory="niri/scripts"
            ),
            "/home/jappe/Backgrounds": Directory(source_directory="niri/backgrounds"),
        }

    def pacman_packages(self) -> list[str]:
        return [
            "gnome-keyring",  # Stores passwords and encryption keys
            "nautilus",  # Default file manager for GNOME
            "niri",  # A scrollable-tiling Wayland compositor
            "polkit-kde-agent",  # Daemon providing a polkit authentication UI for KDE
            "socat",  # Multipurpose relay
            # TODO: swww deprecated => switch to awww aur package?
            "swww",  # A Solution to your Wayland Wallpaper Woes
            "wl-clipboard",  # Command-line copy/paste utilities for Wayland
            "xclip",  # Command line interface to the X11 clipboard
            "xdg-desktop-portal-gnome",  # Backend implementation for xdg-desktop-portal for the GNOME desktop environment
            "xdg-desktop-portal-gtk",  # A backend implementation for xdg-desktop-portal using GTK
            "xwayland-satellite",  # Xwayland outside your Wayland
        ]

    def systemd_units(self) -> list[str]:
        return [
            "dynamic-window-rules.service",
            "polkit-agent.service",
            "swww-background.service",
            "swww-overview.service",
        ]


class NiriIdle(Module):
    def __init__(self):
        super().__init__(name="niri_idle", enabled=True, version="1")

    def files(self) -> dict[str, File]:
        return {
            "home/jappe/.config/niri/scripts/idle_inhibitor": File(
                source_file="niri/scripts/idle_inhibitor.py"
            ),
            "home/jappe/.config/gtklock/style.css": File(
                source_file="niri/gtklock/style.css"
            ),
        }

    def pacman_packages(self) -> list[str]:
        return [
            "gtklock",  # GTK-based lockscreen for Wayland
            "swayidle",  # Idle management daemon for Wayland
        ]

    def systemd_units(self) -> list[str]:
        return [
            "idle-inhibitor.service",
            "swayidle.service",
        ]
