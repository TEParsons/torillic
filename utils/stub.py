import shutil
from pathlib import Path

# get root folder
root = Path(__file__).parent.parent.parent
# get path of base torillic folder
base = Path(__file__).parent.parent / "torillic"
# iterate through all torillic.stub files
for target in root.glob("**/*/torillic.stub"):
    # delete stub
    target.unlink()
    # remove extension
    target = target.parent / target.stem
    # copy folder in its place
    shutil.copytree(
        src=base,
        dst=target
    )
