import subprocess
import sys
import time
from pathlib import Path

def main():
    python = sys.executable
    base = Path(__file__).parent

    # 1) Start the login/launch script
    launch_proc = subprocess.Popen([python, str(base / "launch.py")])

    # 2) Give it a moment to spin up Chrome on 9222
    time.sleep(5)

    # 3) Kick off your main automation against that existing Chrome
    main_proc = subprocess.Popen([python, str(base / "main.py")])

    # 4) Optionally wait for both to finish
    launch_proc.wait()
    main_proc.wait()

if __name__ == "__main__":
    main()