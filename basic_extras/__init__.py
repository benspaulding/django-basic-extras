# -*- coding: utf-8 -*-

"""
Django Basic Extras

A very small collection of some things I find myself frequently using in Django
projects. Hopefully you find it useful. At the moment it only includes an
abstract model for collecting object metadata, and some context processors.
More will likely be added with time, but the idea of this is to stay small
and low-key, including only things that I use on almost all projects.

In fact, some of these bits may seem so small that it is silly to not just
write them in with the project. But I don’t want to have to copy and paste
tests as well, so I figure it is worth it. And putting things together in cute
little packages like this is fun. :)

"""

__version__ = '1.0'

# Mark the app_label for translation. This is wrapped in a try/except block to
# prevent errors when the app is being installed and Django has not yet been
# installed.
try:
    from django.utils.translation import ugettext_noop as _
    # Translators: This is the application label.
    _(u'basic_extras')
except ImportError:
    pass
