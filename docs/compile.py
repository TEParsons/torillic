from pathlib import Path
import shutil
import markdown

__folder__ = Path(__file__).parent

# copy theme to docs folder
theme_source = __folder__.parent / "typora"
shutil.copytree(str(theme_source), str(__folder__), dirs_exist_ok=True)

# point to template file
template_file = __folder__ / "_template.html"
# point to content file
content_file = __folder__ / "index.md"
# point to output file
output_file = __folder__ / "index.html"

# read template
template = template_file.read_text(encoding="utf-8")
# read markdown content
content_md = content_file.read_text(encoding="utf-8")

# setup markdown parser
md = markdown.Markdown(extensions=["extra", "nl2br"])

# parse markdown content
content_html = md.convert(content_md)
# insert into template
page = template.replace("<!-- content -->", content_html)

# save
output_file.write_text(page, encoding="utf-8")