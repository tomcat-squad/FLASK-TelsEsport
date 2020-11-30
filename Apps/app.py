from flask import (Flask, render_template, request, redirect, url_for, flash)
from flask_mysql_connector import MySQL
from werkzeug.utils import secure_filename
from flask_wtf.csrf import CSRFProtect
from static.mchevro import Esport
import os
import datetime

csrf = CSRFProtect()
app = Flask(__name__)
app.secret_key = os.urandom(24)
csrf.init_app(app)
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024

UPLOAD_FOLDER_BUKTI = 'static/bukti'
ALLOWED_EXTENSIONS = set(['png', 'jpeg', 'jpg'])
app.config['UPLOAD_FOLDER_BUKTI'] = UPLOAD_FOLDER_BUKTI

'''
ALLOWED EXTENSION
'''
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

'''
DATABASE MYSQL
'''
app.config['MYSQL_HOST']        = 'localhost'
app.config['MYSQL_USER']        = 'root'
app.config['MYSQL_PASSWORD']    = ''
app.config['MYSQL_DATABASE']    = 'tomcat_esport'
mysql = MySQL(app)

@app.route('/')
def index():
    form = Esport()
    return render_template('user/daftar.html', form=form)

@app.route('/admin')
def index_admin():
    conn = mysql.connection
    cur = conn.cursor()
    cur.execute('SELECT * FROM daftar_ml')
    result = cur.fetchall()
    return render_template('admin/player.html', daftar=result)

@app.route('/upload', methods=['POST'])
def uploadML():
    form = Esport()
    if form.validate_on_submit():
        if request.method == 'POST':
            file = request.files['bukti-tf']
            namaTeam = request.form['namaTeam']
            kapten = request.form['kapten']
            nickname = request.form['nickname']
            idAccount = request.form['idAccount']
            jumlahPemain = request.form['jumlahPemain']
            email = request.form['email']
            whatsapp = request.form['whatsapp']
            waktu = datetime.datetime.now()
            '''
            Myqsl Configuration
            '''
            conn = mysql.connection
            cur = conn.cursor()
            cur.execute("INSERT INTO daftar_ml (namaTeam, kapten, nickname, idAccount, jumlahPemain, email, whatsapp, bukti, waktu) \
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (namaTeam, kapten, nickname, idAccount, jumlahPemain, email, whatsapp, namaTeam+'.jpg', waktu))
            conn.commit()
            if file and allowed_file(file.filename):
                filename = file.filename
                file.save(os.path.join(app.config['UPLOAD_FOLDER_BUKTI'], namaTeam + '.jpg'))
                return redirect(url_for('index'))
            else:
                flash('Upload Gagal!')
                return "Upload Gagal"
    else:
        return render_template('user/daftar.html', form=form)       
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')