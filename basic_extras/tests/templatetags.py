# -*- coding: utf-8 -*-

from django.test import TestCase
from django.test.utils import override_settings
from django.core.paginator import Paginator
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpRequest, QueryDict
from django.template import Context, RequestContext

from ..templatetags.pagination_extras import (start_index_reversed,
                                              page_querystring)


class StartIndexReversedFilterTestCase(TestCase):

    def test_passed_not_a_page(self):
        self.assertEqual(start_index_reversed('foo'), 0)

    def test_paginator_has_zero_items(self):
        paginator = Paginator([], 3, allow_empty_first_page=True)
        self.assertEqual(start_index_reversed(paginator.page(1)), 0)

    def test_the_maths(self):
        object_list = [x for x in range(13)]
        paginator = Paginator(object_list, 3)
        self.assertEqual(start_index_reversed(paginator.page(1)), 13)
        self.assertEqual(start_index_reversed(paginator.page(2)), 10)
        self.assertEqual(start_index_reversed(paginator.page(3)), 7)
        self.assertEqual(start_index_reversed(paginator.page(4)), 4)
        self.assertEqual(start_index_reversed(paginator.page(5)), 1)

    def test_the_maths_with_orphans(self):
        object_list = [x for x in range(13)]
        paginator = Paginator(object_list, 3, orphans=4)
        self.assertEqual(start_index_reversed(paginator.page(1)), 13)
        self.assertEqual(start_index_reversed(paginator.page(2)), 10)
        self.assertEqual(start_index_reversed(paginator.page(3)), 7)


# Ensure that the request context processor is installed.
TCP = ['django.core.context_processors.request']


@override_settings(TEMPLATE_CONTEXT_PROCESSORS=TCP)
class PageQuerystringTagTestCase(TestCase):

    def setUp(self):
        request1 = HttpRequest()
        request1.GET = QueryDict('')
        self.context1 = RequestContext(request1)
        request2 = HttpRequest()
        request2.GET = QueryDict('foo=bar')
        self.context2 = RequestContext(request2)

    def test_no_request_in_context(self):
        self.assertRaises(ImproperlyConfigured, page_querystring, Context(), 1)

    def test_page_1(self):
        # No ``?`` should be returned in this case.
        self.assertEqual(page_querystring(self.context1, 1), '')

    def test_page_1_with_other_params(self):
        self.assertEqual(page_querystring(self.context2, 1), '?foo=bar')

    def test_page_2(self):
        self.assertEqual(page_querystring(self.context1, 2), '?page=2')

    def test_page_2_with_other_params(self):
        self.assertEqual(page_querystring(self.context2, 2), '?foo=bar&page=2')
