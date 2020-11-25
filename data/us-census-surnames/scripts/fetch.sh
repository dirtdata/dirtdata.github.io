#!/bin/sh

# OPTIONAL TODO: fetch scripts should assume download.url is being passed in
# i.e. dry this up
SRC_URL='https://www2.census.gov/topics/genealogy/2010surnames/names.zip'

mkdir -p TMPWORK

curl -o TMPWORK/surnames-2010.zip "${SRC_URL}"
unzip -o TMPWORK/surnames-2010.zip  -d TMPWORK

cp TMPWORK/Names_2010Census.csv original.csv

cp TMPWORK/Names_2010Census.xlsx original.xlsx
