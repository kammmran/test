# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'My Sphinx demo project!'
copyright = '2026, Kamran Heydarov'
author = 'Kamran Heydarov'
version = '4.2'
release = '4.2.1b0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

# Autodoc configuration
autodoc_member_order = 'bysource'
autodoc_typehints = 'description'
autosummary_generate = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_title = "Lumache Documentation"
html_logo = None

# -- Options for LaTeX output ------------------------------------------------
latex_documents = [
    ('index', 'lumache.tex', 'Lumache Documentation', author, 'manual'),
]

# -- Options for manual page output ------------------------------------------
man_pages = [
    ('index', 'lumache', 'Lumache Documentation', [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------
texinfo_documents = [
    ('index', 'lumache', 'Lumache Documentation', author, 'lumache', 
     'A delicious pasta recipe library', 'Miscellaneous'),
]

# -- Options for intersphinx extension ----------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}
