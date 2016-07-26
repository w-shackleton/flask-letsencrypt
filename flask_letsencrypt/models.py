# -*- coding: utf-8 -*-
"""
    flask_letsencrypt.models
    ~~~~~~~~~~~~~~~~~

    Google App Engine database models

    :copyright: (c) 2016 Will Shackleton
    :license: Artistic 2.0
"""

from google.appengine.ext import ndb


class AcmeChallenge(ndb.Model):
    key = ndb.StringProperty(required=True)
    value = ndb.StringProperty(required=True)

    """
    Returns the AcmeChallenge for the given key.
    """
    @classmethod
    def find(cls, key):
        return cls.query(cls.key == key).get()
