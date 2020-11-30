from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length

class RegistrationForm(FlaskForm):
    nama = StringField('Nama Lengkap', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class Esport(FlaskForm):
    namaTeam = StringField('Nama Team', validators=[DataRequired(message='Nama Team Wajib'), Length(min=1, max=100)])
    kapten = StringField('Nama Kapten', validators=[DataRequired(message='Nama Kapten Wajib'), Length(min=1, max=100)])
    nickname = StringField('Nickname', validators=[DataRequired(message='Nickname Wajib'), Length(min=1, max=100)])
    idAccount = IntegerField('Id Account', validators=[DataRequired(message='Harus Angka')])
    jumlahPemain = IntegerField('Jumlah Pemain', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(message='Email Wajib'), Length(min=1, max=100)])
    whatsapp = StringField('Whatsapp', validators=[DataRequired(message='Harus Angka'), Length(min=1, max=16)])