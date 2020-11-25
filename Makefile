.PHONY: help  clean
.DEFAULT_GOAL := help

DATASET_DIR = ./data

clean:
	echo cleaning
	# should clean out all TMPWORK dirs

help:
	@echo 'Read the README at README.md!'

	@echo 'Run ./cli --help'

