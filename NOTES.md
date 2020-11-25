# NOTES

just journaling my thought and design process

## random ideas

- in meta.yaml, have a `schema` attribute
- check out datapackage.json schema from github/datasets: 
    - https://github.com/datasets/country-codes/blob/master/datapackage.json

- design philosophy
    - each DataPot should have one canonical main data file
    - each DataPot should be CSV or JSON
    - the main canonical data file should be as unaltered as possible from the original source, including the keeping of unneeded columns.

## Observations of other data repos

Git cloning other data repos and studying their organization

#### Datahub.io Core Data
- repo: https://github.com/datasets
- homepage: https://datahub.io/docs/core-data
- data index: https://datahub.io/core
- Data Package v1 spec:
    - https://datahub.io/blog/upgrade-to-data-package-specs-v1

- individual data packages
    - very cool generated pages for showing metadata and viz previews
    - each package is its own repo
    - each repo has its own data and scripts subfolders, and github/workflows
    - https://datahub.io/core/geo-admin1-us
        - All data is licensed under the Open Data Commons Public Domain Dedication and License.
        - shows the geojson map
        - datapackage.json: https://pkgstore.datahub.io/core/geo-admin1-us/7/datapackage.json
    - https://github.com/datasets/airport-codes
        - just one data csv...full path is [airport-codes/data/airport-codes.csv](https://github.com/datasets/airport-codes/blob/master/data/airport-codes.csv)
        - has archive/data.csv: https://github.com/datasets/airport-codes/tree/master/archive
        - just one script: https://github.com/datasets/airport-codes/blob/master/scripts/process.py

- inventory schema:
    - file is called `datapackage.json`
    - spec: https://specs.frictionlessdata.io/data-package/
    - datapackage.json examples
        - single csv, i.e. one `resources`: https://github.com/datasets/airport-codes/blob/master/datapackage.json
        - geojson with several resources: https://github.com/datasets/geo-admin1-us/blob/master/datapackage.json

    - datapackage spec: https://specs.frictionlessdata.io/data-package/
        - json-schema: https://specs.frictionlessdata.io/schemas/data-package.json
    - datapackage: tabular data package spec
        - introduction and features: https://specs.frictionlessdata.io/tabular-data-package/#introduction
            - CSV format, single datapackage.json
        - Why CSV: https://specs.frictionlessdata.io/tabular-data-package/#why-csv
        - Specification:


    - datapackage schema details
        - `readme` is raw Markdown, e.g. headers and structure up to author
        - `name` instead of our `slug`
        - `stats` has attrs `bytes` and `rowcount`
        - `licenses` is a list, with each dict having `type` and `url` keys
        - `resources` a list of files in a given data package
            - some packages, like geo shape files, necessarily have several files
            - is required, and must always have at least one item: https://specs.frictionlessdata.io/data-package/#resource-information
            - resources object has
                - `dialect` object, which specifies `delimiter`, `lineTerminator`, and other keys that are similar to python csv.reader args
                - `encoding`
                - `profile`, e.g. `tabular-data-resource`
                - `missingValues` list, e.g. `[""]`
        - has a `sources` list, with each dict specifying title, path and name
        - has `version`

            - 

#### fivethirtyeight/data

- https://github.com/fivethirtyeight/data

- features:
    - designed index page listing: https://data.fivethirtyeight.com/
    - broad CC 4.0 license
- issues:
    - a crapton of subdirs in the root level

- inventory:
    - index.csv is a simple table with fields: `dataset_url,article_url,live`

- individual data packages
    - https://github.com/fivethirtyeight/data/tree/master/trump-lawsuits
        - just a README.md and the CSV
        - README has nice markdown table for data dictionary
    - https://github.com/fivethirtyeight/data/tree/master/subreddit-algebra
        - no data, but has scripts
        - readme describes each script

    - https://github.com/fivethirtyeight/data/tree/master/scrabble-games
        - just csv and readme
        - CSV is 164 MB!
            - Download GUI url is: https://github.com/fivethirtyeight/data/raw/master/scrabble-games/scrabble_games.csv
            - it redirects to: https://media.githubusercontent.com/media/fivethirtyeight/data/master/scrabble-games/scrabble_games.csv
            - seems to use LFS: `scrabble-games/scrabble_games.csv filter=lfs diff=lfs merge=lfs -text`
    
    - https://github.com/fivethirtyeight/data/tree/master/classic-rock
        - scripts and code
        - README is mostly an unordered list of tips
        - scraper script: https://github.com/fivethirtyeight/data/blob/master/classic-rock/compiling_radio.py 


#### Rdatasets

- https://github.com/vincentarelbundock/Rdatasets
- key features
    - generated HTML index with link to CSV, HTML documentation, package, item/slug, title, and rows/cols
    - lots and lots of datasets, distributed across 50 subdirs, with each subdir representing a package/library, e.g. csv/ggplot2 has diamonds.csv and (census) midwest.csv
    - naming convention in which every CSV file has a corresponding RST (and produced HTML) file in csv/ and doc/ subdirs

- key issues
    - No Makefile
    - seems to only work with data that is already included in (and documented by) an R package, like ggplot2 and [datasets](https://stat.ethz.ch/R-manual/R-patched/library/datasets/html/00Index.html)
- inventory
    - to add a new package to collect/scrape, add the name to Imports in [DESCRIPTION](https://github.com/vincentarelbundock/Rdatasets/blob/master/DESCRIPTION) 
    - then run [scrape.R](https://github.com/vincentarelbundock/Rdatasets/blob/master/scrape.R)

- project structure
    - seems to have all data as CSVs, hence a [csv](https://github.com/vincentarelbundock/Rdatasets/tree/master/csv) subdirectory
    - for every csv/subdir, there's a corresponding [doc](https://github.com/vincentarelbundock/Rdatasets/tree/master/csv) subdirectory
    - the csv subdirs
        + each csv subdirectory can contain a wide variety of things
            
            + [csv/carData](https://github.com/vincentarelbundock/Rdatasets/tree/master/csv/carData) contains many CSVs, irregularly capitalized.
            
            + [csv/ggplot2](https://github.com/vincentarelbundock/Rdatasets/tree/master/csv/ggplot2) contains data that comes built into ggplot2

    - the doc subdirs
        - [doc/carData](https://github.com/vincentarelbundock/Rdatasets/tree/master/doc/carData) contains generated HTML, one for each corresponding csv/CarData csv file
            - e.g. [Cowles.html](https://github.com/vincentarelbundock/Rdatasets/tree/master/doc/carData)
            - but there is also a RST subdir: [Cowles.rst](https://github.com/vincentarelbundock/Rdatasets/blob/master/doc/carData/rst/Cowles.rst)
            - ggplot2 docs is cool: https://github.com/vincentarelbundock/Rdatasets/blob/master/doc/ggplot2/rst/midwest.rst
            - RST format in the files are pretty similar, but vaguely enforced. 
                - Not everything has a Sources or Examples section: https://github.com/vincentarelbundock/Rdatasets/blob/master/doc/ggplot2/rst/midwest.rst
                - Not everything has a data dictionary: https://github.com/vincentarelbundock/Rdatasets/blob/master/doc/datasets/rst/AirPassengers.rst


#### Vega datasets

- https://github.com/vega/vega-datasets
- no structured meta, just an inconsistent [SOURCES.md](https://github.com/vega/vega-datasets/blob/master/SOURCES.md) file
- has a flat data directory, with each file as is
- list of file names to CDN URLs  is configured in [src/urls.ts](https://github.com/vega/vega-datasets/blob/master/src/urls.ts)
- has a `scripts` directory
    - [make-url-index.sh](https://github.com/vega/vega-datasets/blob/master/scripts/make-url-index.sh) creates a simple dict with "filename": "cdnurl"
    - [weather.py](https://github.com/vega/vega-datasets/blob/master/scripts/weather.py) does some light wrangling. According to SOURCES.md:

        > ## `seattle-weather.csv`
        > Data from [NOAA](https://www.ncdc.noaa.gov/cdo-web/datatools/records). Daily weather records with metric units. Transformed using `/scripts/weather.py`. We synthesized the categorical "weather" field from multiple fields in the original dataset. This data is intended for instructional purposes.

