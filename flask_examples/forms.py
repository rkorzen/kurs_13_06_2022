f"""
    >>> print(10)
    10

"""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField


class AuthorForm(FlaskForm):
    # """
    #     Docstring
    # """
    name = StringField('name')
    last_name = StringField()


