#!/usr/bin/env python3

def fetch_and_stash(id:str):
    """
    TK do this last; don't need to automate downloads when i can do it by hand
    TK pseudo-code

    slug = 'chicago-environmental-inspections'

    source_url = sources['download']
    dest_dir = Path('data', slug)

    mkdir -p dest_dir
    dest_url = get_default_stash_filename
    # curl -o dest_dir/get_default_stash_filename  dest_url
    """

def build_feeds() -> NoReturnType:
    pass

def build_index() -> str:
    # gather metas
    # use jinja2
    pass

def validate_dataset(id:str):
    pass

def main():
    pass


if __name__ == '__main__':
    print('this is where some cli stuff might go')
    main()


