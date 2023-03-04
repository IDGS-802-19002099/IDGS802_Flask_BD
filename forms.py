from wtforms import Form
from wtforms import StringField, IntegerField 
from wtforms import EmailField 
from wtforms import validators 


class UseForm(Form):
    id=IntegerField('id')
    nombre=StringField('nombre')
    apellidos=StringField('apellidos')
    email=EmailField('correo')
    