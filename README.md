# datatexts.github.io

https://datatexts.github.io

Real world data files for examples, i.e. yet another repo where I stash datasets that I want to link to online. Because I keep forgetting the past repos I've stashed data in.

## Features

- Plain text data: all datasets are stored as either CSV or JSON
- Data straight from the official public sources, uncleaned and ready for you to struggle with!
- All data is licensed for public use
- Detailed metadata that describes the provenance of each dataset
- Multiple formats and samples and variations

## TK description stuff

### How things are organized (TK)

Each dataset has a slug, e.g. `us-congress-legislators-current`.

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

Which means the data file paths are:

- [data/us-congress-legislators-current/original.csv](data/us-congress-legislators-current/original.csv)
- [data/us-congress-legislators-current/sample.csv](data/us-congress-legislators-current/sample.csv)

And these data files are hosted online at these Github pages URLs:

- [https://datatexts.github.io/data/us-congress-legislators-current/original.csv](https://datatexts.github.io/data/us-congress-legislators-current/original.csv)
- [https://datatexts.github.io/data/us-congress-legislators-current/sample.csv](https://datatexts.github.io/data/us-congress-legislators-current/sample.csv)




## Other data stashes as a service repos

This repo takes inspiration and ideas from:


- https://github.com/datasets
- https://github.com/vega/vega-datasets
- https://github.com/altair-viz/vega_datasets
- https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/00Index.html
- https://github.com/vincentarelbundock/Rdatasets
