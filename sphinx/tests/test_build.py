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
    # define some content which should be in a given page
    cases = {
        'index.html': "HOMEPAGECONTENT",
        'page.html': "SECONDARYPAGECONTENT",
        'category/index.html': "CATEGORYHOMEPAGECONTENT",
        'category/subpage.html': "CATEGORYPAGECONTENT"
    }

    # define source and output dir
    source_dir = root / "src"
    dest_dir = root / "artefacts"
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
    # check for errors
    errors = []
    for err_line in stderr.read_text().split("\n"):
        # ignore blank lines
        if not err_line:
            continue
        # ignore non-fatal warnings
        if " WARNING" in err_line.split(":"):
            continue
        # append anything else in stderr
        errors.append(err_line)

    assert not errors, "\n".join(errors)
    # parse relevant pages...
    for page, phrase in cases.items():
        # read page
        content = (root / "artefacts" / "html" / page).read_text()
        # check that content is present
        assert phrase in content

