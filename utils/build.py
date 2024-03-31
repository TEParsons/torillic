"""
Copy the files from base Torillic into the various locations where there's a stub file for it.
"""

import shutil
from pathlib import Path

# ref to this folder
folder = Path(__file__).parent
# ref to root folder
root = folder.parent

# --- Inject base code in place of stub files ---

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

# --- Update version for sub-packages ---

# ref to version file
version_file = root / "version"
# get version
version = version_file.read_text(encoding="utf-8")
# find all pyproject.toml files...
for proj in root.glob("**/pyproject.toml"):
    # read file
    content = proj.read_text(encoding="utf-8")
    # update version
    content = content.replace("{{VERSION}}", version)
    # write file
    proj.write_text(content)
