#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# groundwork tutorial documentation build configuration file, created by
# sphinx-quickstart on Wed Jan 11 08:06:47 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import os
import sys

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.todo',
              'sphinx.ext.viewcode',
              'sphinxcontrib.plantuml'
              ]

this_dir = os.path.dirname(__file__)
plantuml = 'java -jar %s' % os.path.join(this_dir, "tools/plantuml.jar")

# If we are running on windows, we need to manipulate the path,
# otherwise plantuml will have problems.
if os.name == "nt":
    plantuml = plantuml.replace("/", "\\")
    plantuml = plantuml.replace("\\", "\\\\")

# plantuml_output_format = 'svg'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'groundwork tutorial'
copyright = '2017, team useblocks'
author = 'team useblocks'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.1'
# The full version, including alpha/beta/rc tags.
release = '0.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme_path = ["_themes"]
html_theme = 'gw'
if html_theme == 'gw':
    # The gw theme can be found under: https://github.com/useblocks/gw-sphinx-themes
    # The following code tries to fetch the latest version before the build starts.
    git_url = "https://github.com/useblocks/gw-sphinx-themes"
    repo_dir = os.path.join(os.path.dirname(__file__), os.path.abspath("_themes"))
    print("Getting latest version of groundwork sphinx theme")
    try:
        print("  Checking for gitpython library... ", end="")
        from git import Repo
        print("done")
        print("  Checking for working internet connection... ", end="")
        from urllib.request import urlopen
        urlopen("http://google.com")
        print("done")
    except Exception:
        if not os.path.exists(repo_dir) or os.listdir(repo_dir) == []:
            print("Please install 'gitpython' to use the latest version of the groundwork"
                  "sphinx theme or save it by your own under '_themes' by executing "
                  "'git clone https://github.com/useblocks/gw-sphinx-themes")
            sys.exit(1)
        else:
            print("gitpython is not installed, but _themes is no empty. So maybe there is"
                  "a working copy of the groundwork sphinx themes. Lets go one.")

    print("  Getting latest theme updates... ", end="")

    if not os.path.exists(repo_dir):
        Repo.clone_from(git_url, repo_dir)
    else:
        repo = Repo(repo_dir)
        origin = repo.remotes.origin
        origin.pull()
    print("done")

html_logo = "/_static/gw_logo.png"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
html_theme_options = {
    "contribute": False,
    "github_fork": "useblocks/groundwork-tutorial",
    "github_ribbon_color": "white_ffffff",
    "github_user": "useblocks"
}

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'groundworktutorialdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'groundworktutorial.tex', 'groundwork tutorial Documentation',
     'team useblocks', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'groundworktutorial', 'groundwork tutorial Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'groundworktutorial', 'groundwork tutorial Documentation',
     author, 'groundworktutorial', 'One line description of project.',
     'Miscellaneous'),
]

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']
