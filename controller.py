import subprocess
import os

def run_cpp_routing(source, destination):
    exe_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "cpp_backend",
            "routing.exe"
        )
    )

    result = subprocess.run(
        [exe_path, str(source), str(destination)],
        capture_output=True,
        text=True
    )

    return result.stdout
