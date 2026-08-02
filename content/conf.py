import datetime

# Project details
project = 'Web Courses Vault'
copyright = f'{datetime.date.today().year}, Raul Contreras'
author = 'Raul Contreras'

# Core Extensions
# Note: sphinx_lesson automatically manages myst_parser internally
extensions = [
    'sphinx_lesson',
    'sphinx_rtd_theme_ext_color_contrast',
    'sphinx.ext.mathjax',
    'sphinx_thebe',
    'nbsphinx',  # Enables rendering Jupyter Notebooks
]

# Theme & GitHub Pages URL Configuration
html_theme = 'sphinx_rtd_theme'

html_baseurl = 'https://raulcontreraso-bit.github.io/web_courses_vault_sp/'
html_context = {
    'display_github': True,
    'github_user': 'raulcontreraso-bit',
    'github_repo': 'web_courses_vault_sp',
    'github_version': 'main/content/',
}

# Configure live code execution via MyBinder
thebe_config = {
   "selector": "div.highlight",
   "repository_url": "https://github.com/raulcontreraso-bit/web_courses_vault_sp",
   "repository_branch": "main",
}

# Files and directories to ignore during build
exclude_patterns = ['_build', 'venv', 'Thumbs.db', '.DS_Store']