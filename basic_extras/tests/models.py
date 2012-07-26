# -*- coding: utf-8 -*-

from django.test import TestCase

from basic_extras.models import MetaBase


class MetaBaseTestModel(MetaBase):
    """A concrete class solely for testing the MetaBase abstract model."""
    class Meta:
        # Must supply app_label so this gets added to the db correctly.
        app_label = MetaBase._meta.app_label


class MetaBaseTestCase(TestCase):

    def setUp(self):
        self.mbase = MetaBaseTestModel.objects.create()

    def test_dates_get_set(self):
        # TODO: Mock the date instead of just checking for a value.
        # When moving to mocking, we could simply check that created and
        # modified are equal, rather than using the possibly fragile delta/
        # assertAlmostEqual check.
        import datetime
        delta = datetime.timedelta(seconds=1)
        self.assertTrue(self.mbase.created)
        self.assertTrue(self.mbase.modified)
        self.assertAlmostEqual(self.mbase.created, self.mbase.modified,
                delta=delta)

    def test_created_unchanged_on_save(self):
        created_date = self.mbase.created
        self.mbase.save()
        self.assertEqual(self.mbase.created, created_date)

    def test_modified_updated_on_save(self):
        # TODO: Mock date to be sure the datetime is updated correctly.
        modified_date = self.mbase.modified
        self.mbase.save()
        self.assertGreater(self.mbase.modified, modified_date)

