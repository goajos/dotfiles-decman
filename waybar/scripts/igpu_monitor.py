#!/usr/bin/env python
import json
import subprocess


def main():
    process = subprocess.Popen(
        ["intel_gpu_top", "-J", "-s", "1000", "-o", "-"],
        stdout=subprocess.PIPE,
        text=True,
    )

    try:
        if process.stdout is None:
            return

        buffer = ""
        brace_count = 0

        power = 0.0
        engines: dict[str, float] = {
            "Render": 0.0,
            "Blitter": 0.0,
            "Video": 0.0,
            "VideoEnhance": 0.0,
            "Compute": 0.0,
        }

        for line in process.stdout:
            buffer += line.strip()
            for char in line:
                if char == "{":
                    brace_count += 1
                elif char == "}":
                    brace_count -= 1

                    if brace_count == 0:
                        # first buffer holds the opening bracket
                        if buffer[0] == "[":
                            data = json.loads(buffer[1:-1])  # cut of the trailing comma
                        else:
                            data = json.loads(buffer[0:-1])  # cut of the trailing comma

                        power = data.get("power", {}).get("GPU", 0)
                        engines_data = data.get("engines", {})
                        engines["Render"] = engines_data.get("Render/3D", {}).get(
                            "busy", 0
                        )
                        engines["Blitter"] = engines_data.get("Blitter", {}).get(
                            "busy", 0
                        )
                        engines["Video"] = engines_data.get("Video", {}).get("busy", 0)
                        engines["VideoEnhance"] = engines_data.get(
                            "VideoEnhance", {}
                        ).get("busy", 0)
                        engines["Compute"] = engines_data.get("Compute", {}).get(
                            "busy", 0
                        )

                        output = {
                            "text": "iGPU ",
                            "tooltip": f"iGPU Power: {power:.2f}W\nRender: {engines['Render']:.2f}%\nBlitter: {engines['Blitter']:.2f}%\nVideo: {engines['Video']:.2f}%\nVideoEnhance: {engines['VideoEnhance']:.2f}%\nCompute: {engines['Compute']:.2f}%",
                        }
                        print(json.dumps(output), flush=True)

                        buffer = ""
    except (ValueError, IndexError, json.JSONDecodeError):
        buffer = ""
        brace_count = 0
        pass

    # except KeyboardInterrupt:
    #     process.terminate()
    #     sys.exit()


if __name__ == "__main__":
    main()
