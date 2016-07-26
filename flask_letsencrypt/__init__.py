# -*- coding: utf-8 -*-
"""
    flask_letsencrypt
    ~~~~~~~~~~~~~~~~~

    A library for a flask route for Google App Engine to allow easy creation of
    /.well_known/acme-challenge routes.

    :copyright: (c) 2016 Will Shackleton
    :license: Artistic 2.0
"""

from .auth import admin_login_required
from .models import AcmeChallenge
from .editor import editor

__all__ = ['letsencrypt']


def letsencrypt(app,
        template_name,
        config_url="/letsencrypt/",
        admin_decorator_func=admin_login_required):

    @app.route(config_url, methods=['GET', 'POST'])
    @admin_decorator_func()
    def letsencrypt_editor():
        return editor(template_name)

    @app.route('/.well-known/acme-challenge/<key>')
    def challenge(key):
        challenge = AcmeChallenge.find(key)
        if challenge is None:
            abort(404)
        return challenge.key + "." + challenge.value
