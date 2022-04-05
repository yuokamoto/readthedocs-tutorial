# Template for the Read the Docs tutorial

This GitHub template includes fictional Python library
with some basic Sphinx docs.

Read the tutorial here:

https://yu-readthedocs-tutorial.readthedocs.io/en/stable/

## locally test

### doxygen

```
cd cpp
doxygen
```

open file:///<path to cloned repo>/cpp/html/index.html

### Sphinx

```
sphinx-build -a docs/source sphinx_output
```

open file:///<path to cloned repo>/sphinx_output/index.html
