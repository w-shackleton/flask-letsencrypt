# -*- coding: utf-8 -*-
"""
    flask_letsencrypt.editor
    ~~~~~~~~~~~~~~~~~

    The editor page to add new let's encrypt challenges.

    :copyright: (c) 2016 Will Shackleton
    :license: Artistic 2.0
"""

from flask import render_template, flash, redirect, url_for
from flask.ext import wtf
from wtforms import Form, TextField, validators
from .models import AcmeChallenge


class AddForm(wtf.Form):
    combined = TextField('Token (key.value)',
                         validators=[validators.Required()])


def editor(template_name):
    form = AddForm()
    if form.validate_on_submit():
        parts = form.combined.data.split(".")
        if len(parts) != 2:
            flash('Invalid token')
            return redirect(url_for('letsencrypt_editor'))
        [key, value] = parts
        challenge = AcmeChallenge(key=key, value=value)
        challenge.put()
        flash('Key added')
        return redirect(url_for('letsencrypt_editor'))
    return render_template(template_name, form=form,
                           challenges=AcmeChallenge.query())
