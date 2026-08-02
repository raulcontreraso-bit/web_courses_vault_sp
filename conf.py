import datetime

# Project details
project = 'Python Interactive Courses'
copyright = f'{datetime.date.today().year}, Course Team'
author = 'Course Team'

# Extensions required for interactive execution & themes
extensions = [
    'sphinx_lesson',
    'sphinx_rtd_theme_ext_color_contrast',
    'sphinx.ext.mathjax',
    'sphinx_thebe',  # Enables the live execution button
    'myst_parser',   # Allows writing content in Markdown (.md) in addition to .rst
]

# Theme setup
html_theme = 'sphinx_rtd_theme'

# Configure Thebe for interactive code cells
thebe_config = {
   "selector": "div.highlight",
   "repository_url": "https://github.com/YOUR-USERNAME/interactive-python-courses",
   "repository_branch": "main",
}

exclude_patterns = ['_build', 'venv', 'Thumbs.db', '.DS_Store']