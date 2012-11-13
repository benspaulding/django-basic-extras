# -*- coding: utf-8 -*-

def monkeypatch_method(cls):
    """
    Add a new method to a given class.

    Usage::

        from foo import Bar

        @monkeypatch_method(Bar)
        def new_method(self, args):
            # Write your method just like any other.
            # ...

    Credit for this decorator goes to Guido van Rossum. See
    http://mail.python.org/pipermail/python-dev/2008-January/076194.html
    """
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator
