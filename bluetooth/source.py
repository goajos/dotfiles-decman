import decman

decman.packages += [
    "bluez",  # Daemons for the bluetooth protocol stack
    "bluez-utils",  # Development and debugging utilities for the bluetooth protocol stack
]

decman.enabled_systemd_units += ["bluetooth.service"]
