#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Júnior Carvalho'
SITENAME = 'Blog Júnior Carvalho'
SITESUBTITLE = 'Programador, pensador e pai da princesa Rebeca...'
SITEDESCRIPTION = 'Códigos e mais...'
SITEURL = ''
SITELOGO = 'image/foto.jpg'

COPYRIGHT_YEAR='2016'

MAIN_MENU = True

BROWSER_COLOR = '#333'


PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

DEFAULT_DATE_FORMAT = '%d/%m/%Y'

STATIC_PATHS = ['image/']


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('ConBits', 'http://conbits.com.br/'),
#)

# Social widget
SOCIAL = (('linkedin', 'https://br.linkedin.com/in/juniorcarvalhorj'),
          ('github', 'https://github.com/juniorcarvalho'),
          ('twitter', 'https://twitter.com/joseadolfojr'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/home/junior/projetos/blog.juniorcarvalho/src/pelican-themes/Flex"