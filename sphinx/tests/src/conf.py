import sys, os

sys.path.append(os.path.abspath('sphinxext'))

extensions = ["myst_parser"]

source_suffix = {
    '.txt': 'markdown',
    '.md': 'markdown',
}

source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser'
}

html_theme = "torillic"