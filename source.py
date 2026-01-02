#!/usr/bin/env python
import os

import decman
import decman.config

from alacritty.source import Alacritty
from bluetooth.source import Bluetooth
from config import USER
from devel.c.source import C
from devel.csharp.source import CSharp
from devel.docker.source import Docker
from devel.python.source import Python
from devel.raylib.source import Raylib
from devel.rust.source import Rust
from devel.typescript.source import TypeScript
from devel.unity.source import Unity
from devel.zig.source import Zig
from fonts.source import Fonts
from fuzzel.source import Fuzzel
from gaming.source import Gaming
from mako.source import Mako
from misc.source import Misc
from niri.source import Niri, NiriIdle
from nvim.source import Nvim
from openrgb.source import OpenRGB
from pacman.source import Pacman
from shell.source import Shell
from sound.source import Sound
from waybar.source import Perf, Waybar

# TODO: git module with agent + token setup?
# TODO: remove the 'jappe' dependencies in some of the service and config files (paths)?

os.environ["GNUPGHOME"] = f"/home/{USER}/.gnupug/"
decman.config.makepkg_user = f"{USER}"
decman.config.enable_flatpak = False

# AUR packages (self-maintained with paru)
decman.config.enable_fpm = False
decman.aur_packages += [
    "decman",  # Declarative package & configuration manager for Arch Linux.
    "paru",  # Feature packed AUR helper
    "yay"  # Yet another yogurt. Pacman wrapper and AUR helper written in go. (paru backup)
]

base_system_packages = [
    "base",  # Minimal package set to define a basic Arch Linux installation
    "base-devel",  # Basic tools to build Arch Linux packages
    "btrfs-progs",  # Btrfs filesystem utilities
    "intel-ucode",  # Microcode update files for Intel CPUs
    "less",  # A terminal based program for viewing text files
    "linux",  # The Linux kernel and modules
    "linux-firmware",  # Firmware files for Linux - Default set
    "man-db",  # A utility for reading man pages
    "man-pages",  # Linux man pages
    "networkmanager",  # Network connection manager and user applications
]

base_util_packages = [
    "git",  # The fast distributed version control system
    "sudo",  # Give certain users the ability to run some commands as root
]

decman.packages += base_system_packages + base_util_packages

decman.modules += [
    Alacritty(),
    Bluetooth(),
    C(),
    CSharp(),
    Docker(),
    Fonts(),
    Fuzzel(),
    Gaming(),
    Mako(),
    Misc(),
    Niri(),
    NiriIdle(),
    Nvim(),
    OpenRGB(),
    Pacman(),
    Perf(),
    Python(),
    Raylib(),
    Rust(),
    Shell(),
    Sound(),
    TypeScript(),
    Unity(),
    Waybar(),
    Zig(),
]

decman.enabled_systemd_units += ["NetworkManager.service"]

class NoConfirmCommands(decman.config.Commands):
    def install_pkgs(self, pkgs: list[str]) -> list[str]:
        return ["pacman", "-S", "--color=always", "--needed", "--noconfirm"] + pkgs

    def install_files(self, pkg_files: list[str]) -> list[str]:
        return ["pacman", "-U", "--color=always", "--asdeps", "--noconfirm"] + pkg_files

    def install_deps(self, deps: list[str]) -> list[str]:
        return ["pacman", "-S", "--color=always", "--needed", "--asdeps", "--noconfirm"] + deps

    def upgrade(self) -> list[str]:
        return ["pacman", "-Syu", "--color=always", "--noconfirm"]

    def remove(self, pkgs: list[str]) -> list[str]:
        return ["pacman", "-Rs", "--color=always", "--noconfirm"] + pkgs

decman.config.commands = NoConfirmCommands()
