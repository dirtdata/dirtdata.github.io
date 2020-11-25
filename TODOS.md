# TODOS

## priority

- work on meta.yaml format
    - ca-homicides has ad-hoc edits that need to be added to the template
    - all older projects need to be fixed
    - datastash needs a name
    - original.csv is now main:main.csv
- write a DataProject class
- move data/ to d/?

## overall

- data/ be renamed d/ or x/?
    - allows us to put default dataset file path as data.csv


**meta.yaml schema**

(main stuff)
- slug is now id
    - [x] change it in existing yaml
    - [ ] change it in docs
- datastash
    - the object that contains collected files that were downloaded and are now made available
    - need a name: files, stash, catalog, resources
    - has main attribute for main/default file
    - has other: object
    - has samples: object

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

- [x] census surnames 2010
- [?] federal judges
- [?] dot gov domains
- [?] denver pot sales
- leso data
- [ ] ct pre trial inmates
    - https://data.ct.gov/Public-Safety/Accused-Pre-Trial-Inmates-in-Correctional-Faciliti/b674-jy6w
- berkeley police stops
    - https://data.cityofberkeley.info/Public-Safety/Berkeley-PD-Stop-Data-Jan-26-2015-to-Sep-30-2020-/4tbf-3yt8
- ct police stops
- [ ] ca doj open data: https://openjustice.doj.ca.gov/data
    - e warrants
        - https://data-openjustice.doj.ca.gov/sites/default/files/dataset/2019-12/electronic-search-warrant-notifications.csv
    - homicides:
        - https://data-openjustice.doj.ca.gov/sites/default/files/dataset/2020-07/Homicide%20Context_062419.pdf
        - actual: https://data-openjustice.doj.ca.gov/sites/default/files/dataset/2020-07/Homicide%20_Actuals_1987-2019.csv
        - justifiable: https://data-openjustice.doj.ca.gov/sites/default/files/dataset/2020-07/Homicide_Justifiable_1987-2019.csv
        - does actual include justifiable?
    - arrests
    - crimes and clearances
    - deaths in custody
    - domestic violence
        - https://data-openjustice.doj.ca.gov/sites/default/files/dataset/2020-07/Domestic%20Violence%20Related%20Calls%20for%20Service%20Context_062419.pdf

- [ ] pet licenses from muckrock
    - Charlotte, NC Pet Licensing

    - https://www.muckrock.com/foi/charlotte-161/charlotte-nc-pet-licensing-39645/
    - https://cdn.muckrock.com/foia_files/2017/08/14/CHR_PetOwner_170804.xlsx
- [ ] chicago lobbyist activity
    - https://data.cityofchicago.org/Ethics/Lobbyist-Data-Lobbying-Activity/pahz-egmi
    - kind of simple, but messy enough?
- [ ] sf lobbyists
    - public contacts: https://data.sfgov.org/City-Management-and-Ethics/-Known-Issue-Lobbyist-Activity-Contacts-of-Public-/hr5m-xnxc
- public records requests
    - vermont 
        - (not updated since 2019) https://data.vermont.gov/dataset/Public-Records-Requests/fwxs-ckd2
            - 25 cols and 27K rows
        - newer https://data.vermont.gov/dataset/Public-Records-Requests/476u-uxxa
            - just 11 cols and 9000 rows
    - NOLA: has narrative field: https://data.nola.gov/City-Administration/Public-Records-Requests/jsrk-e98x
- house expenditures
- 311 data
- restaurant inspections
- white house salary data
- twitter potus tweets
- NHTSA complaints
    - KILL IT...it's too big...do recalls and investigations instead
    - download: http://www-odi.nhtsa.dot.gov/downloads/folders/Complaints/FLAT_CMPL.zip
        - script
        ```
        mkdir -p TMPWORK/
        curl -Lo TMPWORK/FLAT_CMPL.zip 'http://www-odi.nhtsa.dot.gov/downloads/folders/Complaints/FLAT_CMPL.zip'
        unzip -o TMPWORK/FLAT_CMPL.zip -d TMPWORK/
        ```
    - landing: http://www-odi.nhtsa.dot.gov/downloads/index.cfm
    - metadata page: https://one.nhtsa.gov/webapi/Default.aspx?Complaints/Metadata/81
    - data dictionary: http://www-odi.nhtsa.dot.gov/downloads/folders/Complaints/CMPL.txt
    - http://www-odi.nhtsa.dot.gov/downloads/folders/Complaints/Import_Instructions.pdf
    - http://www-odi.nhtsa.dot.gov/help/complaint.html

- census housing estimates
- covid-19 us deaths: 
    - https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv
    - https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series
- usgs earthquakes
- airport planings
- airplane registrations
- bird impact data
- fatal encounters
- official S&P listings: https://github.com/datasets/s-and-p-500-companies-financials
