# -*- coding: utf-8 -*-
"""
    flask_letsencrypt.auth
    ~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 Will Shackleton
    :license: Artistic 2.0
"""

from functools import wraps
from google.appengine.api import users
from flask import redirect, request


def admin_login_required():
    def decorator(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not users.get_current_user():
                return redirect(users.create_login_url(request.url))
            elif not users.is_current_user_admin():
                return redirect(users.create_login_url(request.url))
            return func(*args, **kwargs)
        return decorated_view
    return decorator
