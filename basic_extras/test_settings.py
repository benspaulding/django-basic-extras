# -*- coding: utf-8 -*-

"""
Settings for running app tests when not part of another project.

"""

from __future__ import unicode_literals


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = (
    'basic_extras',
)

SECRET_KEY = 'super-secret!'
