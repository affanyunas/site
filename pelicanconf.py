#This is for SEO
AUTHOR = 'Affan Yunas'
SITENAME = 'Blogsite'
SITEURL = "https://affanyunas.github.io/me"
FAVICON = '/static/images/favicon.png'
SITESUBTITLE = 'This site is for blogging for me'

# Change Header Area in here - themes by creativitas https://fiverr.com/creativitas
SITESLOGAN = 'Minimals'
SITE_INTRO = 'Clean Minimalist and SEO themes for Pelician Project'

#Configuration yor site
TIMEZONE = 'Asia/Jakarta'
DEFAULT_LANG = 'en'
THEME = 'themes/minim'
PATH = "content"
PAGE_PATHS = ['pages']

# For your static assets folder
STATIC_PATHS = [
    'static',
    'static/images',
    'static/robots.txt',
    ]
EXTRA_PATH_METADATA = {
    "static/robots.txt": {"path": "robots.txt"},
    }

#For change Pagination List Posts
DEFAULT_PAGINATION = 4

# Setup bro
USE_FOLDER_AS_CATEGORY = True
DELETE_OUTPUT_DIRECTORY = False
OUTPUT_RETENTION = [".articles"]
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    }
}
