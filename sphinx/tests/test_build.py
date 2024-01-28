from pathlib import Path
import subprocess


# define root folder
root = Path(__file__).parent
# define std files
stdout = root / "artefacts" / "stdout.txt"
stderr = root / "artefacts" / "stderr.txt"
# make sure std files exist
for std_file in (stdout, stderr):
    if not std_file.is_file():
        with std_file.open("w") as f:
            f.write("")


def test_build():
    # define source and output dir
    source_dir = root / "src"
    dest_dir = root / "artefacts"
    # make sure destination exists
    if not dest_dir.is_dir():
        dest_dir.mkdir(parents=True)
    # define subprocess call to build
    cmd = ["sphinx-build", "-M", "html", source_dir.absolute(), dest_dir.absolute()]
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
    # check for errors
    err = stderr.read_text()
    assert not err, err
