# TODOS


**meta.yaml schema**

(main stuff)
- slug is now id
    - [x] change it in existing yaml
    - [ ] change it in docs
- references should be links

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
        fetch:
            - path: fetch.sh # expects scripts/fetch.sh
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
- should sources.download be changed to sources.original?
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
- feed process: gathers and validates metas
    - produces a atom-compatible xml feed
    - produces flat CSVs:
        - main.csv: important attributes, and URLs for original and sample csv
        - subs.csv enumerates all URLs and is meant to be joined by slug with main.csv
    - produces JSON


## datasets

General issues
- include datasets that exclude commercial usage?

Things to get
- census surnames 2010
- census housing estimates
- federal judges
- covid-19 us deaths: 
    - https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv
    - https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series
- usgs earthquakes
- airport planings
- airplane registrations
- bird impact data
- fatal encounters
- official S&P listings: https://github.com/datasets/s-and-p-500-companies-financials
