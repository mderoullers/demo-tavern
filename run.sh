#!/bin/bash

generate_config() {
  if [[ "$1" =~ ^(dev|qualif|uat|prep)$ ]]; then
    ENV=$1. ./tools/templater.sh tavern/template/var.yaml.tmpl > tavern/var.yaml
  else
    ENV= ./tools/templater.sh tavern/template/var.yaml.tmpl > tavern/var.yaml
  fi
}

generate_config $1

### To run tavern tests ###
cd tavern
python -m pytest
cd ..

### Delete colorlog encodage of junit report xml ###
sed -i 's/\#x1B\[[0-9]*m//g' target/test-results.xml
