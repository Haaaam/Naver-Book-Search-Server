from flask_wtf import FlaskForm
from wtforms import StringField,DateField
from wtforms.validators import DataRequired

class Search_Title(FlaskForm):
    title=StringField('도서명을 입력하세요',validators=[DataRequired()])

class Search_Author(FlaskForm):
    title = StringField('저자명을 입력하세요', validators=[DataRequired()])

class Search_Movie(FlaskForm):
    title=StringField('영화명을 입력하세요',validators=[DataRequired()])

class Search_Rank(FlaskForm):
        keyword = StringField()
        date = DateField()