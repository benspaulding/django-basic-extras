# -*- coding: utf-8 -*-

import os

from distutils.core import setup


version = __import__('basic_extras').__version__

setup(
    name = 'django-basic-extras',
    version = version,
    description = 'A small collection of some oft-used Django bits.',
    url = 'https://github.com/benspaulding/django-basic-extras/',
    author = 'Ben Spaulding',
    author_email = 'ben@benspaulding.us',
    license = 'BSD',
    long_description = open('README.rst').read(),
    requires = ['Django (>=1.3.1)'],
    packages = [
        'basic_extras',
        'basic_extras.tests',
    ],
    package_data = {
        'basic_extras': [
            'locale/*/LC_MESSAGES/*',
        ],
    },
    platforms = ['Any'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
)
