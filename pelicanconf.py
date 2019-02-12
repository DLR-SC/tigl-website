#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'DLR'
SITENAME = u'TiGL'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

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
         ('Imprint', '/pages/imprint.html'),
		 ('Privacy', '/pages/privacy.html'),)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Static paths
STATIC_PATHS = ['images', 'pages/images', 'extra/CNAME']

# Plugins
PLUGIN_PATHS = ["plugins", "d:\\rce\\plugins"]
PLUGINS = ['pelican-page-hierarchy.page_hierarchy',]

# Github pages domain name
# EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}