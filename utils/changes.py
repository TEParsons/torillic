"""
Build a nicely formatted changelog from git commits since the last release
"""

import git 
import re
import argparse
from pathlib import Path
from packaging.version import Version

def parse_commits(repo_dir, version):
    """
    Get commits between a given release and its previous release, sorted by their tags.

    Parameters
    ----------
    repo_dir : pathlib.Path
        Path to the repo whose commit log to parse
    version : packaging.version.Version
        Version to build a changelog for
    
    Returns
    -------
    dict[str: list[tuple[str, git.Commit]]]
        Commit messages (stripped of their tags) and the corresponding commit object, sorted by tag.
    """
    # create repo object
    repo = git.Repo(repo_dir.absolute())
    # get the commits for each version
    tag_commits = {Version(tag.name): tag.commit for tag in repo.tags}
    # get last version from order of repo tags
    all_versions = sorted(list(tag_commits))
    last_version = all_versions[all_versions.index(version) - 1]
    # dict to store messages in by tag
    messages = {}
    # iterate commits between this and last version
    for commit in repo.iter_commits(rev=f"{tag_commits[last_version]}..{tag_commits[version]}"):
        # split into message and tag
        tag, msg = re.match(f"(\w*): (.*)", commit.message).groups()
        # lowercase tag
        tag = tag.lower()
        # alias tags
        if tag in ("bf", ):
            tag = "fix"
        if tag in ("nf", ):
            tag = "feat"
        if tag in ("docs", ):
            tag = "doc"
        if tag in ("tests", ):
            tag = "test"
        # make sure tag has a key in dict
        if tag not in messages:
            messages[tag] = []
        # store message and commit object against tag
        messages[tag].append(
            (msg, commit)
        )
    
    return messages

def construct_changelog(messages):
    """_summary_

    Parameters
    ----------
    messages : [str: list[tuple[str, git.Commit]]]
        Commit messages (stripped of their tags) and the corresponding commit object, sorted by tag.

    Returns
    -------
    str
        Markdown-formatted changelog
    """
    changelog = ""

    # add new features
    if "feat" in messages:
        changelog += (
            "## Features\n"
        )
        for msg, commit in messages['feat']:
            changelog += (
                f"- {msg}\n"
            )
        changelog += (
            "\n"
        )
    # add enhancements
    if "enh" in messages:
        changelog += (
            "## Improvements\n"
        )
        for msg, commit in messages['enh']:
            changelog += (
                f"- {msg}\n"
            )
        changelog += (
            "\n"
        )
    # add fixes
    if "fix" in messages:
        changelog += (
            "## Fixes\n"
        )
        for msg, commit in messages['fix']:
            changelog += (
                f"- {msg}\n"
            )
        changelog += (
            "\n"
        )
    # if anything has been written, add a heading
    if changelog:
        changelog = (
        "# Changes\n"
        "\n"
        + changelog
        )
    
    return changelog

if __name__ == "__main__":
    # get repo and version from arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", help="Specify the location of the repo to build a changelog for.", type=Path)
    parser.add_argument("version", help="Specify the version to build a changelog for.", type=Version)
    args = parser.parse_args()
    # parse commits
    messages = parse_commits(args.repo, args.version)
    # write changelog
    changelog = construct_changelog(messages)

    print(f'::set-output name=changelog::{changelog}')

