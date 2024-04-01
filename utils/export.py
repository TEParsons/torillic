"""
Generate necessary binaries for a release.
"""


from pathlib import Path
import zipfile

__all__ = [
    "folder",
    "target",
    "version",
    "set_version",
    "get_version"
]


# ref to this folder
folder = Path(__file__).parent
# ref to root folder
root = folder.parent
# ref to binaries folder
export_target = root / ".export"


def make_binaries():
    """
    Create binaries (zip files) for release, and save them in the `.export` folder.
    """
    # make sure target folder exists
    if not export_target.is_dir():
        export_target.mkdir(parents=True)

    # read gitignore to use for junk filter
    ignore_list = (root / ".gitignore").read_text().split("\n")

    # write a zip file for each backend
    for backend in ("base", "sphinx", "typora", "mkdocs"):
        # make zip
        with zipfile.ZipFile(export_target / (backend + ".zip"), "w") as zip:
            # get all files
            all_files = (root / backend).glob("**/*")
            include_files = set(all_files)
            # remove files matching gitignore patterns
            for ignore in ignore_list:
                ignore_files = (root / backend).glob(f"**/{ignore}")
                include_files -= set(ignore_files)
            # remove any errant stub files
            stub_files = (root / backend).glob("**/*.stub")
            include_files -= set(stub_files)
            # add each to the zip
            for file in include_files:
                zip.write(
                    filename=file,
                    arcname=file.relative_to(root / backend)
                )

if __name__ == "__main__":
    # if run as a script, just call binaries function
    make_binaries()
