from pathlib import Path

def setup(app):
    app.add_html_theme('torillic', Path(__file__).parent.absolute())