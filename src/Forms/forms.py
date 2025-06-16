from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,EmailField
from wtforms.validators import DataRequired,Length,Email,EqualTo




class RegisterForm(FlaskForm):
    name=StringField("introduce un nombre",validators=[DataRequired(),Length(min=4,max=12)])
    email=EmailField("Introduce un correo electronico",validators=[DataRequired(),Email()])
    password=PasswordField("Introduce una contraseña",validators=[DataRequired(),Length(min=12,max=300),EqualTo("confirmar")])
    confirmar=PasswordField("Repite la contraseña ",validators=[DataRequired(),Length(min=12,max=300)])
    submit=SubmitField("Registrarse")
    



class LoginForm(FlaskForm):
    
    email=EmailField("Introduce tu correo electronico",validators=[DataRequired(),Email()])
    password=PasswordField("Introduce tu  contraseña",validators=[DataRequired(),Length(min=12,max=300)])
    submit=SubmitField("Iniciar Sesion")
    