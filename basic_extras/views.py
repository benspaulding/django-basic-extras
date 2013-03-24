# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views.generic.base import TemplateView


class PlainTextTemplateView(TemplateView):
    """ A plain text generic template view. """

    def render_to_response(self, context, **kwargs):
        return super(PlainTextTemplateView, self).render_to_response(
            context, content_type='text/plain', **kwargs
            )
