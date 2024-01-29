from pathlib import Path
import subprocess


# define root folder
root = Path(__file__).parent
# define std files
stdout = root / "stdout.txt"
stderr = root / "stderr.txt"
# make sure std files exist
for std_file in (stdout, stderr):
    if not std_file.is_file():
        with std_file.open("w") as f:
            f.write("")

# define source and output dir
source_dir = root / "src"
dest_dir = root / "docs"
# make sure destination exists
if not dest_dir.is_dir():
    dest_dir.mkdir(parents=True)
# define subprocess call to build
cmd = ["sphinx-build", "-M", "html", source_dir.absolute(), dest_dir.absolute(), "-a"]
# open std files
_stdout = stdout.open("w")
_stderr = stderr.open("w")
# call
subprocess.call(
    args=cmd,
    stdout=_stdout,
    stderr=_stderr
)
# close std files
_stdout.close()
_stderr.close()
