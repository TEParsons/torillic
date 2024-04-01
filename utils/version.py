"""
For managing version
"""

from pathlib import Path
import re


__all__ = [
    "folder",
    "version_file",
    "get_version",
    "set_version",
]


# ref to this folder
folder = Path(__file__).parent
# ref to root folder
root = folder.parent
# ref to version file
version_file = root / "version"


def get_version():
    """
    Get the current version from the version file at this repo's root
    """
    return version_file.read_text(encoding="utf-8")


def set_version(version, populate=True):
    """
    Set the current version in the version file at this repo's root, and optionally populate it across to other references to it (e.g. in pyproject.toml files)

    Parameters
    ----------
    version : str
        Version to set (should be in semantic versioning format, e.g. 1.2.3)
    populate : bool
        If True (default), then apply version to other references (e.g. pyproject.toml files) 
    """
    # write to version file
    version_file.write_text(version, encoding="utf-8")
    # update other refs
    if populate:
        # find all pyproject.toml files...
        for proj in root.glob("**/pyproject.toml"):
            # read file
            content = proj.read_text(encoding="utf-8")
            # update version
            content = re.sub(
                pattern=r"^version *= *[\"'].*[\"']$",
                repl=f"version = \"{version}\"",
                string=content,
                flags=re.MULTILINE
            )
            # write file
            proj.write_text(content)

if __name__ == "__main__":
    # if run as a script, populate version from current value
    version = get_version()
    set_version(version, populate=True)
