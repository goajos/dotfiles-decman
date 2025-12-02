from decman import Directory, File, Module

from config import USER


class Niri(Module):
    def __init__(self):
        super().__init__(name="niri", enabled=True, version="1")

    def files(self) -> dict[str, File]:
        return {
            f"/home/{USER}/.config/niri/config.kdl": File(
                source_file="niri/config.kdl"
            ),
            f"/home/{USER}/.config/systemd/user/dynamic-window-rules.service": File(
                source_file="systemd/user/dynamic-window-rules.service"
            ),
            f"/home/{USER}/.config/systemd/user/polkit-agent.service": File(
                source_file="systemd/user/polkit-agent.service"
            ),
            f"/home/{USER}/.config/systemd/user/swww-background.service": File(
                source_file="systemd/user/swww-background.service"
            ),
            f"/home/{USER}/.config/systemd/user/swww-overview.service": File(
                source_file="systemd/user/swww-overview.service"
            ),
        }

    def directories(self) -> dict[str, Directory]:
        return {
            f"/home/{USER}/.config/niri/scripts": Directory(
                source_directory="niri/scripts",
                permissions=0o755,
            ),
            f"/home/{USER}/Pictures/Backgrounds": Directory(
                source_directory="niri/backgrounds"
            ),
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

    def systemd_user_units(self) -> dict[str, list[str]]:
        return {
            f"{USER}": [
                "niri.service",
                "dynamic-window-rules.service",
                "polkit-agent.service",
                "swww-background.service",
                "swww-overview.service",
            ]
        }


# TODO: how to auto set up the idle-inhibitor script?
class NiriIdle(Module):
    def __init__(self):
        super().__init__(name="niri_idle", enabled=True, version="1")

    def files(self) -> dict[str, File]:
        return {
            f"/home/{USER}/.config/gtklock/style.css": File(
                source_file="niri/gtklock/style.css"
            ),
            f"/home/{USER}/.config/systemd/user/idle-inhibitor.service": File(
                source_file="systemd/user/idle-inhibitor.service"
            ),
            f"/home/{USER}/.config/systemd/user/swayidle.service": File(
                source_file="systemd/user/swayidle.service"
            ),
        }

    def pacman_packages(self) -> list[str]:
        return [
            "gtklock",  # GTK-based lockscreen for Wayland
            "swayidle",  # Idle management daemon for Wayland
        ]

    def systemd_user_units(self) -> dict[str, list[str]]:
        return {
            f"{USER}": [
                "idle-inhibitor.service",
                "swayidle.service",
            ]
        }
