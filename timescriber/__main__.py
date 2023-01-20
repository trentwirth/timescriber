import sys
from pathlib import Path

base_package_path = Path(__file__).parent.parent
print(f"adding base_package_path: {base_package_path} : to sys.path")
sys.path.insert(0, str(base_package_path)) # add parent directory to sys.path

from timescriber.timescriber import TimeScriberApp

if __name__ == "__main__":
    app = TimeScriberApp()
    app.run()