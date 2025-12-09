#!/usr/bin/env python
from decman import File, Module

from config import USER


# TODO: setup bash shell properly
class Shell(Module):
    def __init__(self):
        super().__init__(name="shell", enabled=True, version="1")

    def files(self) -> dict[str, File]:
        return {
            f"/home/{USER}/.bashrc": File(source_file="shell/.bashrc"),
        }
