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

