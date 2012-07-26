# -*- coding: utf-8 -*-

"""Settings for running app tests when not part of another project."""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = (
    'basic_extras',
)

# Required for Django >= 1.4.
SECRET_KEY = 'super-secret!'
