import click
import jinja2
from pathlib import Path

from cli_helpers import *



@click.command()
def publish():
    """
    make an index.html file
    """
    projdirs = [d for d in DATA_DIR.iterdir() if d.is_dir()]
    projects = []

    for pdir in sorted(projdirs):
        pname = pdir.name
        print(pname)
        meta = proj_meta(pname)

        murl = f"https://dirtdata.github.io/data/{pname}/{meta['downloads']['main']['path']}"
        proj = {
            'title': meta['title'],
            'description': meta['description'],
            'main_download_url': murl,
        }
        projects.append(proj)
        # print(meta)


    with open(PUBLISH_PATH, 'w') as w:
        template = jinja2.Template(TEMPLATES['index'].read_text())
        w.write(template.render(projects=projects))




if __name__ == '__main__':
    print('oops')

