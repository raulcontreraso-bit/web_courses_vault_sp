import datetime

project = 'Web Courses Vault'
copyright = f'{datetime.date.today().year}, Raul Contreras'
author = 'Raul Contreras'

# Core Extensions
extensions = [
    'sphinx_lesson',
    'sphinx_rtd_theme_ext_color_contrast',
    'sphinx.ext.mathjax',
    'sphinx_thebe',
    'myst_parser',  # Myst parser for Markdown support
]

# Prevent suffix conflict between MyST and Sphinx 8+
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

html_theme = 'sphinx_rtd_theme'

# Configure live code execution via MyBinder
thebe_config = {
   "selector": "div.highlight",
   "repository_url": "https://github.com/raulcontreraso-bit/web_courses_vault_sp",
   "repository_branch": "main",
}

exclude_patterns = ['_build', 'venv', 'Thumbs.db', '.DS_Store']