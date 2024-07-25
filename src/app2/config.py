from config.settings import * # NOQA
from config.settings import INSTALLED_APPS


INSTALLED_APPS = [
    *INSTALLED_APPS,

    'app2',
]

ROOT_URLCONF = 'app2.urls'
