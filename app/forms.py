from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class SearchForm(FlaskForm):
    search_term = StringField(
        "Type a keyword to search",
        validators=[
            DataRequired(message="Please enter a search term."),
            Length(min=2, max=50, message="Search term must be between 2 and 50 characters.")
        ]
    )
    submit = SubmitField("Search")
