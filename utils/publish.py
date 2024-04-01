""" 
Script to publish to PyPi (or TestPyPi). Requires git actiosn environment variables, so can't be run from regular terminal.
"""

from os import environ
import version

# get version from tag
tag_version_full = environ["GITHUB_REF"]
# extract version itself
tag_version = tag_version_full.split("/")[-1]
# get version from file
file_version = version.get_version()

if tag_version == "release":
    # if tag version ends with release, this was run from a button - redirect to testpypi
    with open(environ["GITHUB_OUTPUT"], "a") as f:
        print("target=testpypi", file=f)
else:
    # anything else, this was run from a release - target pypi proper
    with open(environ["GITHUB_OUTPUT"], "a") as f:
        print("target=pypi", file=f)
    # make sure repo version matches
    version.set_version(tag_version, populate=True)