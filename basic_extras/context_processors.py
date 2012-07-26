# -*- coding: utf-8 -*-

"""
Useful context processors.

These are to be referenced from the setting TEMPLATE_CONTEXT_PROCESSORS and
used by RequestContext.

"""


def now(request):
    """Provides the current datetime to the context."""
    from basic_extras.utils import now
    return {'now': now()}


def site(request):
    """Provides the current site to the context."""
    from django.contrib.sites.models import Site
    return {'site': Site.objects.get_current()}
