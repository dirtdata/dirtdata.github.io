# TODOS

## priority

- work on meta.yaml format
    -   call `downloads` the `collection`?
    - change `status.notes` to `status` and `notes`
    - ca-homicides has ad-hoc edits that need to be added to the template
    - all older projects need to be fixed
    - get meta.yaml into minimal viable form
    - [x] move original.csv to main.csv in all repos
    - [x] datastash needs a name (it's now `downloads`)

- hack together index.html-making script
    - simple one pager with a data table
    - no need to implement publish.json yet
    - minimal fields:
        - title
        - main url
        - description
        - source landing page
        - publisher
        - hack row/column counter

- write a DataPackage/DataPot class

## renaming stuff

- data/ be renamed d/ or x/?
    - allows us to put default dataset file path as data.csv


**meta.yaml schema**

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


# cli/makefile

- collect
    - when main file is a result of processing the raw download, i.e. a zip file, need
        some logic to deal with that
        - it shouldn't have a url, but it should refer to a original source link
        - maybe have a tempurl attribute, which triggers the manual collection scripting

- feeds/index/publish
    - collects and analyzes all the metas
    - produces a atom-compatible xml feed
    - produces flat CSVs:
        - main.csv: important attributes, and URLs for original and sample csv
        - subs.csv enumerates all URLs and is meant to be joined by slug with main.csv
    - produces JSON
-  publish
    - uses meta.yaml to create a publish.json, which is meant for public API access and NOT meant to be human edited
    - given a dataset id, read its meta.yaml, and produce stats.json/publish.json
        - stats
            - row and column count
            - bytes count
            - last fetched
        - urls
            - main data
                - via Github pages
                - via Github web repo
            - sample
                - Github Pages download
                - web repo
                - gsheets
            - single
                - Github pages URL
                - some kind of interactive view
        - docs
        - links

