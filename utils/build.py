"""
Copy the files from base Torillic into the various locations where there's a stub file for it.
"""

import shutil
from pathlib import Path


# ref to this folder
folder = Path(__file__).parent
# ref to root folder
root = folder.parent


def replace_stubs():
    """
    Replace all .stub files with the base torillic folder.
    """
    # ref to base folder
    base = root / "base"
    # find all .stub files...
    for stub in root.glob("**/*.stub"):
        # convert the stub to a folder
        target = stub.parent / stub.stem
        # delete the stub file
        stub.unlink()
        # copy the base files to the new folder
        shutil.copytree(base, target)
        # log
        print(
            f"Copied {base} to {target}."
        )


if __name__ == "__main__":
    # if run as a script, just replace stubs
    replace_stubs()