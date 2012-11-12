# -*- coding: utf-8 -*-

from django import template
from django.core.paginator import Page
from django.core.exceptions import ImproperlyConfigured


register = template.Library()


@register.filter(is_safe=True)
def start_index_reversed(page):
    """
    Returns the reversed 1-based index of the first object on this page,
    relative to total objects in the paginator.

    This is useful for reversed, paginated lists::

        <ol reversed start="{{ page_obj|start_index_reversed }}">
            <li>...
        </ol>
    """

    # Return zero if there are no items, or if we were passed something other
    # than a ``Page`` object.
    if not isinstance(page, Page) or page.paginator.count == 0:
        return 0
    return page.paginator.count - (page.paginator.per_page * (page.number - 1))


@register.simple_tag(takes_context=True)
def page_querystring(context, page_num):
    """
    Output a querystring for the given page number. (Includes preceding ``?``)

    This makes it simple to create links to other pages while preserving
    other ``GET`` arguments. It also keeps things tidy by removing the ``page``
    parameter if its value is ``1``.

    Usage::

        {% page_querystring [page_num] %}

    Examples::

        <a href="./{% page_querystring 1 %}">Page 1</a>
        <a href="./{% page_querystring paginator.page_count %}">Last page</a>
        <a href="./{% page_querystring page_obj.next_page_number %}">Next</a>

    As with all pagination bits, you will need to avoid errors by wrapping
    these like so::

        {% if page_obj.has_next %}
            <a href="./{% page_querystring page_obj.next_page_number %}">...
        {% endif %}

    Note: This tag requires that the ``HttpRequest`` object be available in the
    context as ``request``. The simplest way to achive this is by listing
    ``django.core.context_processors.request`` in your settings'
    ``TEMPLATE_CONTEXT_PROCESSORS``.
    """
    # Originally I created a tag that also took keywords like ``next``,
    # ``last``, ``previous``, etc., but that required making assumptions about
    # a paginator and page being in context with a certain names, and for
    # handling a bunch of different code paths. It was nice to use in the
    # template, but I did not feel the code complexity was worth it. So while
    # usage in the template may feel verbose, it allows for simpler, more
    # stable code.

    # Ensure request object is accessible in context.
    try:
        querydict = context['request'].GET.copy()
    except KeyError:
        raise ImproperlyConfigured(u'``request`` is not available in the '
            'context. Is ``django.core.context_processors.request`` listed in '
            '``TEMPLATE_CONTEXT_PROCESSORS``. (And you must be using a '
            'RequestContext, of course.)')

    if type(page_num) is not int:
        raise template.TemplateSyntaxError(u'You must pass an integer or a '
                                           'variable which returns one.')

    # NOTE: Below we hard code in the expected name of the page parameter
    # (``page``). At some point this may be made configurable.
    querydict['page'] = page_num

    # Be tidy and remove the page parameter if referencing the first page.
    if page_num == 1:
        del querydict['page']

    return '?%s' % querydict.urlencode() if querydict else ''
