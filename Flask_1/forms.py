from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from Flask_1.Models import User,Post
from wtforms import StringField,PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError

class RegistrationForm(FlaskForm):
        username = StringField('Username', validators=[DataRequired(), Length(min=2,max=20)])
        email = StringField('email',validators=[DataRequired(), Email()])
        password=PasswordField('password',validators=[DataRequired()])
        password_confirm = PasswordField('confirm password',validators=[DataRequired(), EqualTo('password')])
        submit = SubmitField('Sign Up')
        
        def validate_username(self,username):
                user = User.query.filter_by(username=username.data).first()
                if user:
                        raise ValidationError('Username taken. Choose another one')
        def validate_email(self,email):
                email = User.query.filter_by(email=email.data).first()
                if email:
                        raise ValidationError('Email is in use.')
                
class LoginForm(FlaskForm):
        email = StringField('email',validators=[DataRequired(), Email()])
        password=PasswordField('password',validators=[DataRequired()])
        remember = BooleanField('remember me')
        submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
        username = StringField('Username', validators=[DataRequired(), Length(min=2,max=20)])
        
        email = StringField('email',validators=[DataRequired(), Email()])
        
        picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
        
        submit = SubmitField('Update')
        
        def validate_username(self,username):
                if username.data != current_user.username:
                        user = User.query.filter_by(username=username.data).first()
                        if user:
                                raise ValidationError('Username taken. Choose another one')
        
        def validate_email(self,email):
                if email.data != current_user.email:
                        email = User.query.filter_by(email=email.data).first()
                        if email:
                                raise ValidationError('Email is in use.')

class PostForm(FlaskForm):
        title=StringField('Title', validators=[DataRequired()])
        content = TextAreaField('Content',validators=[DataRequired()])
        submit = SubmitField('Post')