#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'DLR'
SITENAME = u't8code'
SITEURL = ''
SITE_SUMMARY = 't8code - Parallel algorithms and data structures for tree-based AMR with arbitrary element shapes.'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
LOCALE = "C"
DEFAULT_DATE_FORMAT = '%a %d %B %Y'


THEME = 'themes/polar'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Simulation and Software Technology', 'http://www.dlr.de/sc'),
         ('Imprint', '%s/pages/imprint.html' % SITEURL),
         ('Privacy', '%s/pages/privacy.html' % SITEURL),
         ('Terms of use', '%s/pages/terms_of_use.html' % SITEURL),
         ('Accessibility', '%s/pages/accessibility.html' % SITEURL),)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

SITEMAP = {
    'exclude': ['author/'],
    'format': 'xml',
    'changefreqs': {
        'articles': 'weekly',
        'pages': 'monthly',
        'indexes': 'yearly'
    }
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Static paths
STATIC_PATHS = ['images', 'pages/images', 'extra/CNAME', 'doc']
ARTICLE_EXCLUDES = ['doc']

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ['pelican-page-hierarchy.page_hierarchy', 'sitemap', 'pelican-open_graph']

# Github pages domain name
# EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}