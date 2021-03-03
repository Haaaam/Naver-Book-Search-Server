from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class Search_Title(FlaskForm):
    title=StringField('도서명을 입력하세요',validators=[DataRequired()])

class Search_Author(FlaskForm):
    title = StringField('저자명을 입력하세요', validators=[DataRequired()])

