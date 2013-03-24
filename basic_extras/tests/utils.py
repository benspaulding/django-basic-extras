# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.test import TestCase

from ..utils import monkeypatch_method


class MonkeyPatchTestClass(object):
    """ A class solely for testing the ``monkeypatch_method`` decorator. """

    def get_foo(self):
        return u'foo'


class MonkeyPatchMethodTestCase(TestCase):

    def test_method_added(self):
        self.assertFalse(hasattr(MonkeyPatchTestClass, 'get_bar'))

        @monkeypatch_method(MonkeyPatchTestClass)
        def get_bar(self):
            return u'bar'

        self.assertTrue(hasattr(MonkeyPatchTestClass, 'get_bar'))
        obj = MonkeyPatchTestClass()
        self.assertEqual(obj.get_bar(), u'bar')

    def test_method_overridden(self):
        obj = MonkeyPatchTestClass()
        self.assertEqual(obj.get_foo(), u'foo')

        @monkeypatch_method(MonkeyPatchTestClass)
        def get_foo(self):
            return u'oof'

        self.assertEqual(obj.get_foo(), u'oof')
