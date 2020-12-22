from pathlib import Path
import requests
from ruamel.yaml import YAML
yaml = YAML()

DATA_DIR = Path('data')
TEMPLATES = {'meta': Path('assets/templates/meta.template.yaml'),
            'index': Path('assets/templates/index.template.html')}
PUBLISH_PATH = Path('./index.html')


def fetch_file(url:str) -> bytes:
    resp = requests.get(url)
    if resp.status_code != 200:
        raise ValueError(f"Got unexpected status code of {resp.status_code}")
    else:
        return resp.content

# proj should probably be a class

def proj_dir(id:str) -> Path:
    return DATA_DIR.joinpath(id)

def proj_meta_path(id:str) -> Path:
    return proj_dir(id).joinpath('meta.yaml')

def proj_meta(id:str) -> dict:
    txt = proj_meta_path(id).read_text()
    return yaml.load(txt)



def proj_file_inventory(id:str) -> dict:
    d = {}
    stash = proj_meta(id)['downloads']

    if stash.get('main'):
        d['main'] = stash['main']

    extras = proj_meta(id)['extra_downloads']

    for o in extras:
        d[o['path']] = o

    return d
