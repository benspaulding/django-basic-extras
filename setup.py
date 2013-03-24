# -*- coding: utf-8 -*-

import os

from distutils.core import setup


here = os.path.dirname(__file__)


def get_long_desc():
    return open(os.path.join(here, 'README.rst')).read()


# Function borrowed from carljm.
def get_version():
    fh = open(os.path.join(here, 'basic_extras', '__init__.py'))
    try:
        for line in fh.readlines():
            if line.startswith('__version__ ='):
                return line.split('=')[1].strip().strip("'")
    finally:
        fh.close()


setup(
    name='django-basic-extras',
    version=get_version(),
    description='A small collection of some oft-used Django bits.',
    url='https://github.com/benspaulding/django-basic-extras/',
    author='Ben Spaulding',
    author_email='ben@benspaulding.us',
    license='BSD',
    long_description=open('README.rst').read(),
    packages=[
        'basic_extras',
        'basic_extras.templatetags',
        'basic_extras.tests',
    ],
    package_data={
        'basic_extras': [
            'locale/*/LC_MESSAGES/*',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
)
