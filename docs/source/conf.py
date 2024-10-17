# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from nglcobdai_utils import __author__, __copyright__, __version__

project = __name__
copyright = __copyright__
author = __author__
release = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # Include documentation from docstrings
    "sphinx.ext.napoleon",  # Support for NumPy and Google style docstrings
    "sphinx.ext.viewcode",  # Add links to highlighted source code
    "sphinx.ext.todo",  # Support for todo items
    "sphinx.ext.autosummary",  # Generate autodoc summaries
    "sphinx.ext.coverage",  # Collect doc coverage stats
    "sphinx.ext.intersphinx",  # Link to other projects' documentation
    "myst_parser",  # Support for MyST markdown
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# -- Options for autodoc -----------------------------------------------------
add_module_names = False
autodoc_member_order = "bysource"
autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "private-members": False,
    "special-members": False,
    "inherited-members": False,
    "show-inheritance": True,
}

# -- Options for Napoleon Extension ------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# -- Options for Intersphinx Extension ---------------------------------------
highlight_language = "python"

# -- Options for HTML output -------------------------------------------------
html_show_sourcelink = True
html_show_copyright = True
html_show_sphinx = False
