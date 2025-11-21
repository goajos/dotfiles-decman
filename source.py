import os

import decman
import decman.config

from alacritty.source import Alacritty
from bluetooth.source import Bluetooth
from config import USER
from devel.python.source import Python

# TODO: add angular source?
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

# TODO: remove the 'jappe' dependencies in some of the service and config files?

os.environ["GNUPGHOME"] = f"/home/{USER}/.gnupug/"
decman.config.makepkg_user = f"{USER}"

# AUR packages (self-maintained with paru)
decman.config.enable_fpm = False
decman.aur_packages += [
    "decman",  # Declarative package & configuration manager for Arch Linux.
    "paru",  # Feature packed AUR helper
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
    Shell(),
    Sound(),
    Waybar(),
]

decman.enabled_systemd_units += ["NetworkManager.service"]
