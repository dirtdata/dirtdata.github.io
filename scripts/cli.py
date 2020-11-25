#!/usr/bin/env python3

import click
from pathlib import Path
import sys
from typing import NoReturn as NoReturnType

from cli_helpers import *


def myecho(*messages, **kwargs) -> NoReturnType:
    msgtxt = ' '.join(str(m) for m in messages)
    kwargs['message'] = msgtxt
    click.echo(**kwargs)

def myerr(*messages, **kwargs) -> NoReturnType:
    kwargs['err'] = True
    myecho(*messages, **kwargs)


@click.group()
def main():
    pass



@main.command()
@click.argument('id', nargs=1)
@click.option('-n', '--dry-run', is_flag=True, help="Just print the URLs that would be downloaded and the paths saved to")
def collect(id, dry_run):
    """
    Download the original raw files as specified in the project meta, and save to canonical paths

    Status: just a rickety script -- need to make a project class, write tests, and make a more robust downlaoder...
    """
    destdir = proj_dir(id)
    if not destdir.exists():
        raise ValueError(f'Could not find data project with {id=}')

    files = proj_file_inventory(id)
    for k, f in files.items():
        myerr(click.style(f'\n{k}', fg='bright_blue'))

        url = f['url']
        myerr(click.style('Downloading from URL:\n', fg='green'), click.style(url, fg='white',))

        if not dry_run:
            content = fetch_file(url)
            myerr('\tDownloaded', click.style(f'{len(content)} bytes', fg='cyan'))

        destpath = destdir.joinpath(f["path"])
        myerr(click.style('Saving to:\n', fg='green'), click.style(str(destpath) , fg='white'))
        if not dry_run:
            with open(destpath, 'wb') as dest:
                dest.write(content)



@main.command()
@click.argument('id', nargs=1)
@click.option('-n', '--dry-run', is_flag=True, help="Just print what would be created, etc.")
def init(id, dry_run):
    """
    Initiate a new dataset scaffold project in ${DATA_DIR}/[ID]
    """
    destdir = proj_dir(id)

    if destdir.exists():
        raise ValueError(f'{destdir} already exists!')
    else:
        click.echo(f"Creating project directory: {destdir}", err=True)

        if not dry_run:
            destdir.mkdir()

        metapath = proj_meta_path(id)
        click.echo(f"Creating meta file: {metapath}", err=True)

        if not dry_run:
            metapath.write_text(TEMPLATES['meta'].read_text())


if __name__ == '__main__':
    sys.exit(main())




# def fetch_and_stash(id:str):
#     """
#     TK do this last; don't need to automate downloads when i can do it by hand
#     TK pseudo-code

#     slug = 'chicago-environmental-inspections'

#     source_url = sources['download']
#     dest_dir = Path('data', slug)

#     mkdir -p dest_dir
#     dest_url = get_default_stash_filename
#     # curl -o dest_dir/get_default_stash_filename  dest_url
#     """

# def build_feeds() -> NoReturnType:
#     pass

# def build_index() -> str:
#     # gather metas
#     # use jinja2
#     pass

# def validate_dataset(id:str):
#     pass

# def main():
#     pass
