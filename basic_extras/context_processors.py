# -*- coding: utf-8 -*-

"""
Useful context processors.

These are to be referenced from the setting TEMPLATE_CONTEXT_PROCESSORS and
used by RequestContext.

"""

from __future__ import unicode_literals


def now(request):
    """Provides the current datetime to the context."""
    from django.utils import timezone
    return {'now': timezone.now()}


def site(request):
    """Provides the current site to the context."""
    from django.contrib.sites.models import Site
    return {'site': Site.objects.get_current()}
