#!/usr/bin/env python
import json
import subprocess


def print_output(
    system: dict[str, float | int], cores: dict[str, dict[str, int | float]]
):
    try:
        tooltip = f"System:\nAvg {system['Avg_MHz']} MHz\nBusy {system['Busy%']}%\nBusy {system['Bzy_MHz']} MHz\nTemp {system['PkgTmp']}°C\nPackage {system['PkgWatt']} W"
        cores_tooltip = ""
        sorted_cores = sorted(cores.items(), key=lambda x: int(x[0]))
        columns = [sorted_cores[i : i + 5] for i in range(0, len(sorted_cores), 5)]
        for column in columns:
            for core_id, core_data in column:
                cores_tooltip += (
                    f"Core {core_id}: Avg {core_data['Avg_MHz']} MHz | "
                    f"Busy {core_data['Busy%']}% | "
                    f"Busy {core_data['Bzy_MHz']} MHz | "
                    f"Temp {core_data['CoreTmp']}°C\n"
                )
            cores_tooltip += "\n"
        tooltip += f"\n\nCores:\n{cores_tooltip}"
        output = {"text": "CPU ", "tooltip": tooltip}
        print(json.dumps(output), flush=True)
    except json.JSONDecodeError:
        pass


def main():
    process = subprocess.Popen(
        [
            "turbostat",
            "--interval",
            "1",
            "--quiet",
            "--show",
            "CPU,Busy%,Bzy_MHz,CoreTmp,Avg_MHz,PkgTmp,PkgWatt",
        ],
        stdout=subprocess.PIPE,
        text=True,
    )

    try:
        if process.stdout is None:
            return

        system: dict[str, float | int] = {
            "Avg_MHz": 0,
            "Busy%": 0.0,
            "Bzy_MHz": 0,
            "CoreTmp": 0,
            "PkgTmp": 0,
            "PkgWatt": 0.0,
        }
        cores: dict[str, dict[str, int | float]] = {}

        for line in process.stdout:
            line = line.strip()
            if not line:
                continue
            split = line.split()
            if not split:
                continue
            if split[0] == "CPU":
                continue  # skip header line

            cpu_id = split[0]
            if cpu_id == "-":  # summary line indicates start of new block
                if cores:
                    print_output(system, cores)
                    cores = {}

                system["Avg_MHz"] = int(split[1])
                system["Busy%"] = float(split[2])
                system["Bzy_MHz"] = int(split[3])
                system["PkgTmp"] = int(split[5])
                system["PkgWatt"] = float(split[6])
            else:
                cores.setdefault(cpu_id, {})
                cores[cpu_id]["Avg_MHz"] = int(split[1])
                cores[cpu_id]["Busy%"] = float(split[2])
                cores[cpu_id]["Bzy_MHz"] = int(split[3])
                cores[cpu_id]["CoreTmp"] = int(split[4])
    except (IndexError, ValueError):
        pass


if __name__ == "__main__":
    main()
