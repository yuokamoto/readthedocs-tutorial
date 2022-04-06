# Configuration file for the Sphinx documentation builder.

import sys
import os
import subprocess

print('test\n\n')

read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'
if read_the_docs_build:

    subprocess.call('cd ..; doxygen', shell=True)

else :
    sys.path.append( "/usr/local/lib/python3.9/site-packages/breathe/" )

sys.path.insert(0, os.path.abspath("../../py"))

# -- Project information

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.imgmath', 
    'sphinx.ext.todo', 
    'breathe', 
    "sphinx.ext.graphviz"
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

breathe_projects = { "myproject": "../xml" }
breathe_default_project = "myproject"

html_extra_path = ['../html']