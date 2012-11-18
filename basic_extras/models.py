# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


# Translators: This is the application label.
_(u'basic extras')


class MetaBase(models.Model):
    """Abstract base model class that holds some common metadata fields."""

    created = models.DateTimeField(_(u'date created'))
    modified = models.DateTimeField(_(u'date modified'))

    class Meta:
        abstract = True
        get_latest_by = 'created'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(MetaBase, self).save(*args, **kwargs)
