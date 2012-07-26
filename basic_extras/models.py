# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from basic_extras.utils import now


class MetaBase(models.Model):
    """Abstract base model class that holds some commone metadata fields."""

    created = models.DateTimeField(_(u'date created'))
    modified = models.DateTimeField(_(u'date modified'))

    class Meta:
        abstract = True
        get_latest_by = 'created'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = now()
        self.modified = now()
        return super(MetaBase, self).save(*args, **kwargs)
