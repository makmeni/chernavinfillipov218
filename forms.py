from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class ResumeForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    description = TextAreaField('Описание', validators=[DataRequired()])
    image_url = StringField('URL изображения', validators=[DataRequired()])
    category = SelectField('Категория', choices=[('Дизайн', 'Дизайн'), ('Разработка', 'Разработка'), ('Маркетинг', 'Маркетинг')], validators=[DataRequired()])
    submit = SubmitField('Добавить')
