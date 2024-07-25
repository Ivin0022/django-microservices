from config.settings import * # NOQA
from config.settings import INSTALLED_APPS


INSTALLED_APPS = [
    *INSTALLED_APPS,

    'app1',
]

ROOT_URLCONF = 'app1.urls'
