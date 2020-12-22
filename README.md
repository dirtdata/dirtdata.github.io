# dirtdata.github.io

[https://dirtdata.github.io](https://dirtdata.github.io) (work in progress)

Real world data files for examples, i.e. yet another repo where I stash datasets that I want to link to online. Because I keep forgetting the past repos I've stashed data in.

## Features

- Plain text data: all datasets are stored as either CSV or JSON
- Data straight from the official public sources, uncleaned and ready for you to struggle with!
- All data is licensed for public use
- Detailed metadata that describes the provenance of each dataset
- Multiple formats and samples and variations

This repo is mostly focused on data storing and example documentation, and to be used by other repos.

## Issues/Flaws/Limitations

- Unlike [Datahub.io's core data service](https://datahub.io/docs/core-data), DirtData doesn't provide much beyond data and documentation. No wrangling, no standardization.
- Most of this data is most definitely not just ready to use or visualize


## TK description stuff

### How things are organized (TK)

Each dataset has an `id` , e.g. `us-congress-legislators-current`.

Each dataset has a subfolder in [data/](data/) corresponding to its slug, e.g. [data/us-congress-legislators-current](data/us-congress-legislators-current).

Each dataset subfolder has a `meta.yaml` file which describes the dataset's provenance and also its file paths, e.g. [data/us-congress-legislators-current/meta.yaml](data/us-congress-legislators-current/meta.yaml).

The `files` schema looks something like:

```yaml
files:
  - path: orignal.csv
    default: true

  - path: sample.csv
    description: |
      Just a little more than a dozen rows
```

Which means the local data file paths are:

- [data/us-congress-legislators-current/original.csv](data/us-congress-legislators-current/original.csv)
- [data/us-congress-legislators-current/sample.csv](data/us-congress-legislators-current/sample.csv)

And these data files are hosted online at these Github pages URLs:

- [https://dirtdata.github.io/data/us-congress-legislators-current/original.csv](https://dirtdata.github.io/data/us-congress-legislators-current/original.csv)
- [https://dirtdata.github.io/data/us-congress-legislators-current/sample.csv](https://dirtdata.github.io/data/us-congress-legislators-current/sample.csv)


And they can also be found in the Github repo:

- https://github.com/dirtdata/dirtdata.github.io/blob/main/data/us-congress-legislators-current/original.csv
- https://github.com/dirtdata/dirtdata.github.io/blob/main/data/us-congress-legislators-current/sample.csv



## Other data stashes as a service repos

This repo takes inspiration and ideas from:

- https://github.com/fivethirtyeight/data
- Datahub.io Core Data: https://github.com/datasets: a Github organization that hosts many dataset repos that follow a spec
- https://github.com/datasets/awesome-data: a collection of Markdown files by topic that describe a curated list of possible data sources. No data is hosted on this repo
- https://github.com/vega/vega-datasets
- https://github.com/altair-viz/vega_datasets
- https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/00Index.html
- https://github.com/vincentarelbundock/Rdatasets
- R `datasets` package: https://stat.ethz.ch/R-manual/R-patched/library/datasets/html/00Index.html
- https://github.com/curran/data
https://github.com/awesomedata/awesome-public-datasets
