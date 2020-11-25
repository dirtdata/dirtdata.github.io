.PHONY: help manifest clean
.DEFAULT_GOAL := help

clean:
	echo cleaning
	# should clean out all TMPWORK dirs

help:
	echo 'Read the README at README.md!'

manifest:
	@echo This command should recursively read data/**/meta.yaml and generate a current inventory of data
