# Template for the Read the Docs tutorial

This GitHub template includes fictional Python library
with some basic Sphinx docs.

## Online doc are available in readthedoc

https://yu-readthedocs-tutorial.readthedocs.io/en/devel/

## Tools

documentation is built with three tools

- [doxygen](http://www.doxygen.org)
- [sphinx](http://www.sphinx-doc.org)
- [breathe](https://breathe.readthedocs.io)

## Locally build

1. install tools in #tools section.
2. build
   ```
   cd docs
   make --always-make html
   ```
3. Open following in your browser.
   - Sphinx at `file:///<path to cloned repo>/docs/source/_build/html/index.html`
   - Original doxygen output at `file:///<path to cloned repo>/docs/source/_build/html/doxygen_generated/html/index.html`
