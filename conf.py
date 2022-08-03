# *************************************************************
# |docname| - Sphinx configuration file for a Runestone project
# *************************************************************
#
# Problem Solving with Algorithms and Data Structures documentation build configuration file, created by
# sphinx-quickstart on Thu Oct 27 08:17:45 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('../modules'))

from runestone import runestone_static_dirs, runestone_extensions, setup
import pkg_resources

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.mathjax'] + runestone_extensions()

#,'runestone.video','runestone.reveal','runestone.poll','runestone.tabbedStuff','runestone.disqus','runestone.codelens','runestone.activecode', 'runestone.assess', 'runestone.animation','runestone.meta', 'runestone.parsons', 'runestone.blockly', 'runestone.livecode','runestone.accessibility']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'COMP1000:Think Like a Computer'
copyright = '2022 clatulip'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.0.1'
# The full version, including alpha/beta/rc tags.
release = '0.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages. https://www.sphinx-doc.org/en/master/usage/configuration.html
language = "en"

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# `keep_warnings <http://www.sphinx-doc.org/en/stable/config.html#confval-keep_warnings>`_:
# If true, keep warnings as “system message” paragraphs in the built documents.
# Regardless of this setting, warnings are always written to the standard error
# stream when sphinx-build is run.
keep_warnings = True

# `rst_prolog <http://www.sphinx-doc.org/en/stable/config.html#confval-rst_prolog>`_:
# A string of reStructuredText that will be included at the beginning of every
# source file that is read.
rst_prolog = (
# For fill-in-the-blank questions, provide a convenient means to indicate a blank.
"""

.. |blank| replace:: :blank:`x`
"""

# For literate programming files, provide a convenient way to refer to a source file's name. See `runestone.lp.lp._docname_role`.
""".. |docname| replace:: :docname:`name`
"""
)

# Select whether to use server-side grading where possible. Server-side grading
# requires **all** the following:
#
# - The use of Runestone services (``eBookConfig.useRunestoneServices === true``)
# - Logging enabled (``eBookConfig.logLevel > 0``)
#
# The first two conditions cause the ``RunestoneBase.logBookEvent`` in ``runestonebase.js`` to post a student response to the server. The last conditions ensures that ``hsblog`` in ``ajax.py`` on the server will return a response containing grading information.
runestone_server_side_grading = False
generate_component_labels = False

# Extensions
# ==========
# CodeChat
# --------
# **CodeChat note:** A dict of {glob_, lexer_alias}, which uses lexer_alias
# (e.g. a lexer's `short name <http://pygments.org/docs/lexers/>`_) to analyze
# any file wihch matches the given `glob
# <https://docs.python.org/2/library/glob.html>`_.
CodeChat_lexer_for_glob = {
    # Otherwise, Pygments picks the wrong lexer for CSS...
    '*.css': 'CSS',
    # ... and for JavaScript.
    '*.js': 'JavaScript',
}
#
# **CodeChat note::** This is a list of exclude_patterns_ which applies only to
# source documents; exclude_patterns_ will exclude the given files from all of
# Sphinx (for example, files here won't be included even if they're mentioned in
# html_static_path_.
CodeChat_excludes = []
#
# Inline syntax highlight
# -----------------------
# `inline_highlight_respect_highlight <https://sphinxcontrib-inlinesyntaxhighlight.readthedocs.io/en/latest/#confval-inline_highlight_respect_highlight>`_:
# Use the language specified by the ``highlight`` directive to syntax highlight ``code`` role contents.
inline_highlight_respect_highlight = True
inline_highlight_literals = False

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages. sphinx_bootstrap is provided with
# Runestone. Other themes are built into sphinx:
# https://www.sphinx-doc.org/en/master/usage/theming.html?highlight=html_theme_path#using-a-theme
html_theme = 'sphinx_bootstrap'

# If using a non-sphinx theme, the path to the theme folder must be in this list
html_theme_path = [pkg_resources.resource_filename('runestone', 'common/project_template/_templates/plugin_layouts')]

# To override individual templates from the theme, you can make a directory and add its path
# relative to this file to the templates_path list. In it, place copies of any template files
# you wish to override - your template file(s) will be used instead of the default ones from the theme
#templates_path = ['_templates']

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    # Navigation bar title. (Default: ``project`` value)
    'navbar_title': "COMP1000UofM",

    # Tab name for entire site. (Default: "Site")
    'navbar_site_name': "Chapters",

    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    'globaltoc_depth': 1,

    # Include hidden TOCs in Site navbar?
    #
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    #
    # Values: "true" (default) or "false"
    'globaltoc_includehidden': "true",

    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': "navbar",

    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "true",

    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    'source_link_position': "nav",

    # Bootswatch (http://bootswatch.com/) theme.
    #
    # Options are nothing with "" (default) or the name of a valid theme
    # such as "amelia" or "cosmo".
    #
    # Note that this is served off CDN, so won't be available offline.
    #'bootswatch_theme': "slate",
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# https://www.sphinx-doc.org/en/master/usage/configuration.html?highlight=html_sidebars#confval-html_additional_pages
#html_additional_pages = {}

# A list of paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# Example: html_static_path =  runestone_static_dirs() + ['_static', 'other']
html_static_path = runestone_static_dirs()

# List of extra stylesheets that should be added to all html pages
# Files must be on a path contained in html_static_path
#setup.custom_css_files = ["sample.css", "sample2.css"]

# List of extra js files that should be added to all html pages
# Items may be a file name or a dict with properties {"file":FILENAME, "key1", "value1", "key2, "value2"...}
#   in which case file should have the file name and other key/value pairs are used as attrs
#   on the script tag. The sample below will set sample2.js's script tag to have the defer attr
# Files must be on a path contained in html_static_path
#setup.custom_js_files = ["sample.css", {"file": "sample2.js", "defer": ""}]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'COMP 1000: Think Like a Computer'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title ='COMP 1000'

# Logo is included at the top of the page
#html_logo = "../source/_static/logo_small.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# It True, sets js files from Sphinx & Runestone to be loaded with defer attr
# substantially speeding up page rendering. May cause issues with books that
# have custom directives or raw html that assume jquery or another library
# is loaded before body is parsed. 
html_defer_js = True

# Output file base name for HTML help builder.
htmlhelp_basename = 'PythonCoursewareProjectdoc'

# .. _accessibility_style:
#
# accessibility_style
# -------------------
# This config value is defined in the `../../accessibility/accessibility.py` extension.
# By this config value you can select what accessibility stylesheet
# you want to add (``normal``, ``light``, ``darkest`` or ``none``).
#accessibility_style = 'normal'

# Config values for specific Runestone components
#
#activecode_div_class = 'runestone explainer ac_section alert alert-warning'
#activecode_hide_load_history = False
#mchoice_div_class = 'runestone alert alert-warning'
#clickable_div_class = 'runestone alert alert-warning'
#codelens_div_class = 'alert alert-warning cd_section'
#dragndrop_div_class = 'runestone'
#fitb_div_class = 'runestone'
#parsons_div_class = 'runestone'
#poll_div_class = 'alert alert-warning'
#shortanswer_div_class = 'journal alert alert-warning'
#shortanswer_optional_div_class = 'journal alert alert-success'
#showeval_div_class = 'runestone explainer alert alert-warning'
#tabbed_div_class = 'alert alert-warning'
