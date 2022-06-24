#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

OUTPUT_PATH = 'published/'

SITEURL = 'https://github.com/holke/t8code'
RELATIVE_URLS = False

#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = False

LINKS = (('Simulation and Software Technology', 'http://www.dlr.de/sc'),
         ('Imprint', '%s/pages/imprint.html' % SITEURL),
         ('Privacy', '%s/pages/privacy.html' % SITEURL),)


# Following items are often useful when publishing

# DISQUS_SITENAME = "..."
GOOGLE_ANALYTICS = "UA-134418253-1"
