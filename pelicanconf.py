#This is for SEO
AUTHOR = 'Affan Yunas'
SITENAME = 'Blogsite'
SITEURL = "http://127.0.0.1:8000"
FAVICON = 'theme/images/pelican.png'
SITESUBTITLE = 'Writte every parts'

# Change Header Area in here
SITESLOGAN = 'Blog'
SITE_INTRO = 'Blogging all the ways down'

#Configuration yor site
TIMEZONE = 'Asia/Jakarta'
DEFAULT_LANG = 'en'
THEME = 'themes/minim'
PATH = "content"
PAGE_PATHS = ['pages']


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

MENUITEMS = (
    ('Home', f'{SITEURL}/index.html'),
    ('All Post', f'{SITEURL}/pages/posts.html'),
    ('About', f'{SITEURL}/pages/about.html'),
    ('Tags', f'{SITEURL}/pages/tags.html'),
    # Tambahkan item lainnya di sini
)
