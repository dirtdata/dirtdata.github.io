.PHONY: help manifest
.DEFAULT_GOAL := help

help:
	echo 'Read the README at README.md!'

manifest:
	@echo This command should recursively read data/**/meta.yaml and generate a current inventory of data
