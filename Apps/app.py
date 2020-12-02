from flask import (Flask, render_template, request, redirect, url_for, flash, abort)
from flask_mysql_connector import MySQL
from werkzeug.utils import secure_filename
from flask_wtf.csrf import CSRFProtect, CSRFError
from static.TOKEN import Esport_Mobile_Legend
import os
import datetime

csrf = CSRFProtect()
app = Flask(__name__)
app.secret_key = os.urandom(24)
csrf.init_app(app)
'''
CSRF CUSTOM ERROR
'''
@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return 'Token Expaired!', 400
'''
PROSES UPLOAD GAMBAR
'''
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
UPLOAD_FOLDER_BUKTI = 'static/bukti_transfer'
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
    form = Esport_Mobile_Legend()
    return render_template('user/daftar.html', form=form)

@app.route('/admin')
def index_admin():
    conn = mysql.connection
    cur = conn.cursor()
    cur.execute('SELECT * FROM daftar_ml')
    result = cur.fetchall()
    return render_template('admin/player.html', daftar=result)

'''
MOBILE LEGEND - BACKEND
'''
@app.route('/upload_ML', methods=['POST'])
def uploadML():
    form = Esport_Mobile_Legend()
    if form.validate_on_submit():
        if request.method == 'POST':
            get_Team            = request.form['Team']
            get_Email           = request.form['Email']
            get_Whatsapp        = request.form['Whatsapp']

            get_Nama_Kapten     = request.form['NamaKapten']
            get_IGN_Kapten      = request.form['IGN_Kapten']
            get_Id_Kapten       = request.form['IdKapten']

            get_Nama_Player_2   = request.form['NamaPlayer2']
            get_IGN_Player_2    = request.form['IGN_Player2']
            get_Id_Player_2     = request.form['IdPlayer2']
            
            get_Nama_Player_3   = request.form['NamaPlayer3']
            get_IGN_Player_3    = request.form['IGN_Player3']
            get_Id_Player_3     = request.form['IdPlayer3']

            get_Nama_Player_4   = request.form['NamaPlayer4']
            get_IGN_Player_4    = request.form['IGN_Player4']
            get_Id_Player_4     = request.form['IdPlayer4']

            get_Nama_Player_5   = request.form['NamaPlayer5']
            get_IGN_Player_5    = request.form['IGN_Player5']
            get_Id_Player_5     = request.form['IdPlayer5']

            get_waktu           = datetime.datetime.now()
            get_BuktiPembayaran = request.files['bukti-tf']

            if get_BuktiPembayaran and allowed_file(get_BuktiPembayaran.filename):
                try:
                    filename = get_BuktiPembayaran.filename
                    get_BuktiPembayaran.save(os.path.join(app.config['UPLOAD_FOLDER_BUKTI'], get_Team + '.jpg'))
                except:
                    abort(403)
                '''
                Myqsl Configuration
                '''
                conn = mysql.connection
                cur = conn.cursor()
                cur.execute("INSERT INTO daftar_ml (Team, NamaKapten, IGN_Kapten, ID_Kapten,\
                                                    NamaPlayer2, IGN_Player2, ID_Player2,\
                                                    NamaPlayer3, IGN_Player3, ID_Player3,\
                                                    NamaPlayer4, IGN_Player4, ID_Player4,\
                                                    NamaPlayer5, IGN_Player5, ID_Player5,\
                                                    Email, Whatsapp, BuktiPembayaran, Waktu)\
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
                                    (get_Team, get_Nama_Kapten, get_IGN_Kapten, get_Id_Kapten,
                                    get_Nama_Player_2, get_IGN_Player_2, get_Id_Player_2,
                                    get_Nama_Player_3, get_IGN_Player_3, get_Id_Player_3,
                                    get_Nama_Player_4, get_IGN_Player_4, get_Id_Player_4,
                                    get_Nama_Player_5, get_IGN_Player_5, get_Id_Player_5,
                                    get_Email, get_Whatsapp, get_Team + '.jpg', get_waktu))
                conn.commit()
                flash('Berhasil Terdaftar', 'Success')
                return redirect(url_for('index'))
            else:
                flash('Upload Gagal!', 'Failed')
                return redirect(url_for('index'))
        else:
            abort(405)
    else:
        return render_template('user/daftar.html', form=form)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')