import os

import decman
import decman.config

import bluetooth.source
import sound.source
from devel.python.source import Python
from fonts.source import Fonts
from gaming.source import Gaming
from mako.source import Mako
from misc.source import Misc
from niri.source import Niri, NiriIdle
from nvim.source import Nvim
from openrgb.source import OpenRGB
from waybar.source import Waybar

os.environ["GNUPGHOME"] = "/home/jappe/.gnupug/"
decman.config.makepkg_user = "jappe"

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
    Fonts(),
    Gaming(),
    Mako(),
    Misc(),
    Niri(),
    NiriIdle(),
    Nvim(),
    OpenRGB(),
    Python(),
    Waybar(),
]

decman.enabled_systemd_units += ["NetworkManager.service"]
