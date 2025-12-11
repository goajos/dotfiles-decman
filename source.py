#!/usr/bin/env python
import os

import decman
import decman.config

from alacritty.source import Alacritty
from bluetooth.source import Bluetooth
from config import USER
from devel.docker.source import Docker
from devel.javascript.source import JavaScript
from devel.python.source import Python
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
# TODO: how to properly set up the uv executables for user services?
# TODO: remove the 'jappe' dependencies in some of the service and config files?
# TODO: properly set up a global theme with this as guideline:
# https://github.com/projekt0n/github-nvim-theme/blob/main/lua/github-theme/palette/github_dark_default.lua

os.environ["GNUPGHOME"] = f"/home/{USER}/.gnupug/"
decman.config.makepkg_user = f"{USER}"

# AUR packages (self-maintained with paru)
decman.config.enable_fpm = False
decman.aur_packages += [
    "decman",  # Declarative package & configuration manager for Arch Linux.
    "paru",  # Feature packed AUR helper
    # "ty",  # An extremely fast Python type checker and language server, written in Rust.
    # "visual-studio-code-bin",  # Visual Studio Code (vscode) official binary version
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
    Docker(),
    Fonts(),
    Fuzzel(),
    Gaming(),
    JavaScript(),
    Mako(),
    Misc(),
    Niri(),
    NiriIdle(),
    Nvim(),
    OpenRGB(),
    Pacman(),
    Perf(),
    Python(),
    Shell(),
    Sound(),
    Waybar(),
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
