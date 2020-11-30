
# datasets TODOs

TODOs of finding and collecting them

## existing

- remove us-congress-legislators-current and just have historical be legislators?
    - data schema is exactly the same
    - this could be one example in which the main.csv data is not the pure raw data, but a combination of historical and current
    - add a congressmembers.terms repo, that consists of the flattening of yaml


## in progress

- [x] census surnames 2010
- [?] federal judges
- [?] dot gov domains
- [?] denver pot sales
- [o] chicago lobbyist activity
- CA DOJ data: 
    - https://openjustice.doj.ca.gov/data
    - [o] e warrants
        - https://data-openjustice.doj.ca.gov/sites/default/files/dataset/2019-12/electronic-search-warrant-notifications.csv
    - [o] homicides:
        - actual: https://data-openjustice.doj.ca.gov/sites/default/files/dataset/2020-07/Homicide%20_Actuals_1987-2019.csv
    - [o] deaths in custody

- [?] ct pre trial inmates: https://data.ct.gov/Public-Safety/Accused-Pre-Trial-Inmates-in-Correctional-Faciliti/b674-jy6w
- [o] chicago lobbying https://data.cityofchicago.org/Ethics/Lobbyist-Data-Lobbying-Activity/pahz-egmi

- [o] vermont public records requests
    - (not updated since 2019) https://data.vermont.gov/dataset/Public-Records-Requests/fwxs-ckd2
        - 25 cols and 27K rows
    - newer https://data.vermont.gov/dataset/Public-Records-Requests/476u-uxxa
        - just 11 cols and 9000 rows

- [o] HHS data breaches
    - https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf 

- [o] NHTSA 
    - landing: http://www-odi.nhtsa.dot.gov/downloads/index.cfm
    - defects investigations
        - needs to be pruned
    - recalls
        - needs to be pruned

- [ ] restaurant inspections


## maybe

- leso data

- [ ] pet licenses from muckrock/Charlotte, NC Pet Licensing
    - https://www.muckrock.com/foi/charlotte-161/charlotte-nc-pet-licensing-39645/
    - https://cdn.muckrock.com/foia_files/2017/08/14/CHR_PetOwner_170804.xlsx

- Congress House expenditures
- 311 data

- census housing estimates
- covid-19 us deaths: 
    - https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv
    - https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series


## no for now

- CA DOJ data
    - arrests
    - crimes and clearances
    - domestic violence
        - https://data-openjustice.doj.ca.gov/sites/default/files/dataset/2020-07/Domestic%20Violence%20Related%20Calls%20for%20Service%20Context_062419.pdf
- CT police stops
- white house salary data
- twitter potus tweets
- usgs earthquakes
- airport planings
- airplane registrations
- bird impact data
- fatal encounters
- official S&P listings: https://github.com/datasets/s-and-p-500-companies-financials
