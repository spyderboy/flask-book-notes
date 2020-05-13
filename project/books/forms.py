from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import DateField

class BooksForm(FlaskForm):
    title = TextField('Title', validators=[DataRequired(),
                                         Length(min=1, max=254)])
    author = TextField('Author')
    read_date = DateField('Read on Date', format='%Y-%m-%d')
    notes = TextField('Notes')


class EditBooksForm(FlaskForm):
    title = TextField('Title', validators=[DataRequired(),
                                         Length(min=1, max=254)])
    author = TextField('Author')
    read_date = DateField('Read on Date', format='%Y-%m-%d')
    notes = TextField('Notes')
