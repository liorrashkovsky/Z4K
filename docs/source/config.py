# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Zerto for Kubernetes'
copyright = '2022, Zerto a Hewlett Packard Enterprise company'
author = 'Yuri Kretingen'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'myst_parser',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {    
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
