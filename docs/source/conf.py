# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import acces_memoire
acces_memoire.path.insert(0, os.path.abspath("."))

project = 'sae15-proc'
copyright = '2023, Ewen GADONNAUD Theo BRUNEAU'
author = 'Ewen GADONNAUD Theo BRUNEAU'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
 'sphinx.ext.todo',
 'sphinx.ext.mathjax',
 'sphinx.ext.ifconfig',
 'sphinx.ext.autodoc',
 'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
