# meta.yaml TODOS


(main stuff)
- move sources.landing_page to a top level attribute
- datastash/downloads
    - the object that contains collected files that were downloaded and are now made available
    - need a name: files, stash, catalog, resources
    - has main attribute for main/default file
    - has other: object
    - has samples: object

- [x] references should be links

- [...] `files` (didn't get to it last night)
    - should be like `sources`, with canonical keys like:
        - original/default
        - preview/sample
        - record (a preview of a single representative record)

- optionally, there should be variations/samples, with `path,url,title,description` attrs
    - maybe a `record-samples/examples` object to be able to spotlight outlier records


- dataset specific scripts
    - `scripts` an object that has canonical keys: `download/fetch`, e.g.
    ```yaml
    scripts:
        collect:
            - path: collect.sh # expects scripts/fetch.sh
              description: 'because unzipping is involved'
    ```

- dataset specific docs
    - optional docs subfolder
    - spec has a `docs` list, pointing to objects with `title,path,url,description`
    - automate the downloading of docs into data/dataset-id/docs/PATH.FILE
    - see example in us-census-surnames

(file.template.yaml)

optional:
- `links` a list of objects, each which have keys `{title,url,description}`
- `wrangling` is now an object, with keys `description,cmd`



(other stuff)
- should files.original be files.main?
- should :files: be changed to :stashes/stash:
- looking forward, should there be timestamp versioning? 
- maybe a versions list, with each num corresponding to a sub/subdir

    ```yaml
    versions:
        - num: 1
          description: whatever
          updated_at: 2020-10-12
    ```
    results in files at data/dataset-slug/v/1/original.csv

- ideas from datapackage spec: https://specs.frictionlessdata.io/data-package/#metadata
    - `keywords`
    - `license` is an object, with name and url keys
    - `resources` for multi-file packages, if I ever have them? Or maybe in place of `files`?
