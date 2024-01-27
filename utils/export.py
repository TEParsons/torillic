"""
Basic script to generate necessary binaries for a release.
"""

from pathlib import Path
import shutil
import zipfile

# root folder
root = Path(__file__).parent.parent
# folder to put files in
target = root / ".export"
# make sure target folder exists
if not target.is_dir():
    target.mkdir(parents=True)

# read gitignore to use for junk filter
ignore_list = (root / ".gitignore").read_text().split("\n")

# write a zip file for each backend
for backend in ("sphinx", "typora"):
    # make zip
    with zipfile.ZipFile(target / (backend + ".zip"), "w") as zip:
        # get all files
        all_files = (root / backend).glob("**/*")
        include_files = set(all_files)
        # remove files matching gitignore patterns
        for ignore in ignore_list:
            ignore_files = (root / backend).glob(f"**/{ignore}")
            include_files -= set(ignore_files)
        # add each to the zip
        for file in include_files:
            zip.write(
                filename=file,
                arcname=file.relative_to(root / backend)
            )
