from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, Regexp

class RegistrationForm(FlaskForm):
    nama = StringField('Nama Lengkap', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class Esport_Mobile_Legend(FlaskForm):
    Team        = StringField('Team', validators=[DataRequired(message='*Wajib Isi'), Length(min=1, max=100),
                                                    Regexp(regex=r'^[0-9A-Za-z]',flags=1 ,message='*Dilarang Menggunakan Simbol')])
    Whatsapp    = IntegerField('Whatsapp', validators=[DataRequired(message='*Wajib Isi')])
    Email       = StringField('Email', validators=[DataRequired(message='*Alamat Email'), Length(min=1, max=100),
                                                    Regexp(regex=r'^[@0-9a-z]',flags=1 ,message='*Huruf Kecil')])
    NamaKapten  = StringField('Team', validators=[DataRequired(message='*Wajib Isi'), Length(min=1, max=100),
                                                    Regexp(regex=r'^[0-9A-Za-z]',flags=1 ,message='*Dilarang Menggunakan Simbol')])
    IGN_Kapten  = StringField('Team', validators=[DataRequired(message='*Wajib Isi'), Length(min=1, max=100),
                                                    Regexp(regex=r'^[0-9A-Za-z]',flags=1 ,message='*Dilarang Menggunakan Simbol')])
    IdKapten    = IntegerField('Whatsapp', validators=[DataRequired(message='*Wajib Isi')])     
    NamaPlayer2 = StringField('Team', validators=[DataRequired(message='*Wajib Isi'), Length(min=1, max=100),
                                                    Regexp(regex=r'^[0-9A-Za-z]',flags=1 ,message='*Dilarang Menggunakan Simbol')])
    IGN_Player2 = StringField('Team', validators=[DataRequired(message='*Wajib Isi'), Length(min=1, max=100),
                                                    Regexp(regex=r'^[0-9A-Za-z]',flags=1 ,message='*Dilarang Menggunakan Simbol')])
    IdPlayer2   = IntegerField('Whatsapp', validators=[DataRequired(message='*Wajib Isi')])  
    NamaPlayer3 = StringField('Team', validators=[DataRequired(message='*Wajib Isi'), Length(min=1, max=100),
                                                    Regexp(regex=r'^[0-9A-Za-z]',flags=1 ,message='*Dilarang Menggunakan Simbol')])
    IGN_Player3 = StringField('Team', validators=[DataRequired(message='*Wajib Isi'), Length(min=1, max=100),
                                                    Regexp(regex=r'^[0-9A-Za-z]',flags=1 ,message='*Dilarang Menggunakan Simbol')])
    IdPlayer3   = IntegerField('Whatsapp', validators=[DataRequired(message='*Wajib Isi')])  
    NamaPlayer4 = StringField('Team', validators=[DataRequired(message='*Wajib Isi'), Length(min=1, max=100),
                                                    Regexp(regex=r'^[0-9A-Za-z]',flags=1 ,message='*Dilarang Menggunakan Simbol')])
    IGN_Player4 = StringField('Team', validators=[DataRequired(message='*Wajib Isi'), Length(min=1, max=100),
                                                    Regexp(regex=r'^[0-9A-Za-z]',flags=1 ,message='*Dilarang Menggunakan Simbol')])
    IdPlayer4   = IntegerField('Whatsapp', validators=[DataRequired(message='*Wajib Isi')])  
    NamaPlayer5 = StringField('Team', validators=[DataRequired(message='*Wajib Isi'), Length(min=1, max=100),
                                                    Regexp(regex=r'^[0-9A-Za-z]',flags=1 ,message='*Dilarang Menggunakan Simbol')])
    IGN_Player5 = StringField('Team', validators=[DataRequired(message='*Wajib Isi'), Length(min=1, max=100),
                                                    Regexp(regex=r'^[0-9A-Za-z]',flags=1 ,message='*Dilarang Menggunakan Simbol')])
    IdPlayer5   = IntegerField('Whatsapp', validators=[DataRequired(message='*Wajib Isi')])  
    NamaPlayer6 = StringField('Team', validators=[DataRequired(message='*Wajib Isi'), Length(min=1, max=100),
                                                    Regexp(regex=r'^[0-9A-Za-z]',flags=1 ,message='*Dilarang Menggunakan Simbol')])
    IGN_Player6 = StringField('Team', validators=[DataRequired(message='*Wajib Isi'), Length(min=1, max=100),
                                                    Regexp(regex=r'^[0-9A-Za-z]',flags=1 ,message='*Dilarang Menggunakan Simbol')])
    IdPlayer6   = IntegerField('Whatsapp', validators=[DataRequired(message='*Wajib Isi')]) 