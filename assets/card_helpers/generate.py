from pathlib import Path, PurePath
import sys
import click
import imgkit
import markdown
from jinja2 import Template

# Twitter card suggested size
HEIGHT = 418
WIDTH = 800
assets = PurePath(Path.cwd(), "assets")
cards_folder = PurePath(assets, "cards")
helper_folder = PurePath(assets, "card_helpers")
templates = PurePath(helper_folder, "templates")
static = PurePath(helper_folder, "static")

def generate_fn(post, output_folder):
    stub = "-".join(PurePath(post).stem.split("-")[3:])
    fn = PurePath(output_folder,stub  + ".png")
    return fn

with open(f"{templates}/card.html") as f:
    t = Template(f.read())

def process(post, png):
    print(f"Generating card: {post}")
    md = markdown.Markdown(extensions=['meta'])
    with open(post) as f:
        _ = md.convert(f.read())
        title = md.Meta["title"][0]
        
    render = t.render(
        title=title,
        #background=f"{static}/background.png",
        height=HEIGHT, 
        width=WIDTH, 
    )
    img = imgkit.from_string(render, png, options={"width": WIDTH, "quiet": ""})
    return (f"Generated {png}")

@click.command()
@click.option('-i', '--input-folder', default="_posts", help='Output folder')
@click.option('-o', '--output-folder', default=cards_folder, help='Output folder')
@click.option('-r', '--refresh', is_flag=True, default=False, help="Force refresh")
@click.option('-q', '--quiet', is_flag=True, default=False, help="quiet")
def main(input_folder, output_folder, refresh, quiet):
    changes = False
    for post in Path(input_folder).glob("*.md"):
        png = generate_fn(post, output_folder)
        if refresh:
            resp = process(post, png)
            if not quiet:
                print(resp)
        else:
            if Path(png).exists():
                if not quiet: 
                    print(f"Skipping {png}; exists.")
            else:
                resp = process(post, png)
                changes = True
                if not quiet:
                    print(resp)
    if changes:
        print("New card made. Make sure you commit it! TODO(glasnt): make this script do that for you")
        sys.exit(1)
    
if __name__ == '__main__':
    main()

