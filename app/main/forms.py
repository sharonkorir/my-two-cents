from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [Required()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):

    title = StringField('Blog post title',validators=[Required()])
    content = TextAreaField('Your post', validators=[Required()])
    slug = StringField('Slug', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    comment = TextAreaField('comment', validators=[Required()])
    submit = SubmitField('Submit')