from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

CATEGORIES = [('технології', 'Технології'), ('наука', 'Наука'), ('спосіб життя', 'Спосіб життя')]

class PostForm(FlaskForm):
    title = StringField("Назва", validators=[DataRequired(), Length(min=2)])
    content = TextAreaField("Зміст", render_kw={"rows": 5, "cols": 40}, validators=[DataRequired()])
    is_active = BooleanField('Активний пост')
    publish_date = DateField('Дата публікації', format='%Y-%m-%d', validators=[DataRequired()])
    category = SelectField('Категорія', choices=CATEGORIES, validators=[DataRequired()])
    submit = SubmitField("Додати пост")