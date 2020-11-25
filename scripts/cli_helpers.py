import pyaml
from pathlib import Path
import requests
from ruamel.yaml import YAML
yaml = YAML()

DATA_DIR = Path('data')
TEMPLATES = {'meta': Path('assets/schemas/meta.template.yaml')}


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
    meta = proj_meta(id)
    stash = meta['datastash']

    d = {}
    if stash.get('main'):
        d['main'] = stash['main']

    if stash.get('extra'):
        for o in stash['extra']:
            d[o['path']] = o

    return d
