# Blank Tavern Project for Panoptest

## Where to add the Tavern test files ?

You must **delete** the sample files **[test_file1/2.tavern].yml** in the diretory **/tavern**

After that you can **add** your yaml files to the directory **/tavern**

## Where to configure the variables ?

The variable file is in the directory **/tavern/template/var.yaml.tmpl**

And you have to configure the templater in the **run.sh** file

## How to test on your pc ?

**To install the python dependencies**, you can run the command `make install`

Run the command `./run.sh`

## Useful links

- [Documention Tavern](https://taverntesting.github.io/)
- [Documentation Pytest](https://docs.pytest.org/en/latest/contents.html)
- [Documentation Bash-Templater](https://github.com/johanhaleby/bash-templater)
- [Example : sanity-check data-compliance](https://gitlab.adeo.com/sirius/data-compliance/sanity-check)
- [Example : bash-templater](http://code.haleby.se/2015/11/20/simple-templating-engine-in-bash/)