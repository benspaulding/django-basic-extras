# -*- coding: utf-8 -*-

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
        self.assertTrue(hasattr(MonkeyPatchTestClass, 'get_foo'))

        @monkeypatch_method(MonkeyPatchTestClass)
        def get_foo(self):
            return u'oof'

        obj = MonkeyPatchTestClass()
        self.assertEqual(obj.get_foo(), u'oof')
