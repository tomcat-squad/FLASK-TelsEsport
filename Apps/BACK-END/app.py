from flask import (Flask, render_template, request, 
                    redirect, url_for, flash, abort,
                    session)
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
CUSTOM ERROR PAGE
'''
@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    code_error = '400'
    pesan_error = 'TOKEN EXPAIRED, REFRESH PAGE'
    return render_template('error_page/error.html', code=code_error, pesan=pesan_error), 400

@app.errorhandler(404)
def page_not_found(e):
    code_error = '404'
    pesan_error = 'PAGE NOT FOUND'
    return render_template('error_page/error.html', code=code_error, pesan=pesan_error), 404

@app.errorhandler(405)
def page_methods_allowed(e):
    code_error = '405'
    pesan_error = 'METHOD NOT ALLOWED'
    return render_template('error_page/error.html', code=code_error, pesan=pesan_error), 405

@app.errorhandler(403)
def page_forbiden(e):
    code_error = '403'
    pesan_error = 'FORBIDEN :)'
    return render_template('error_page/error.html', code=code_error, pesan=pesan_error), 403

@app.errorhandler(500)
def page_server_error(e):
    code_error = '500'
    pesan_error = 'SERVER ERROR :('
    return render_template('error_page/error.html', code=code_error, pesan=pesan_error), 500

'''
PROSES UPLOAD GAMBAR
'''
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
UPLOAD_FOLDER_BUKTI = 'static/assets/bukti_transfer'
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

'''
VIEW ADMIN START
'''
@app.route('/admin')
def index_admin():
    get_ip  = request.environ['REMOTE_ADDR']
    form    = Esport_Mobile_Legend()
    return render_template('admin/index.html', form=form, get_ip=get_ip)

@app.route('/login_admin', methods=['POST'])
def login_admin():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        '''
        Logger & Blokir Ip START
        '''
        #Get IP & Waktu
        get_ip  = request.environ['REMOTE_ADDR']
        get_waktu = datetime.datetime.now()
        logger = open('static/logger_admin.txt', 'a')
        logger.write(f'{get_ip}\n')
        logger.close()

        #Baca File Logger
        logger = open('static/logger_admin.txt', 'r')
        logger_read = logger.readlines()
        logger.close()

        #Blacklist Ip Di Htaccess
        if len(logger_read) == 5:
            htaccess = open('static/.htaccess', 'a')
            htaccess.write(f'deny from {logger_read[0]}allow from all\n')
            htaccess.close()
            os.remove('static/logger_admin.txt')
        '''
        Logger & Blokir Ip END
        '''
        get_username = request.form['username']
        get_password = request.form['password']
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT * FROM admin WHERE username=%s AND password=%s", (get_username, get_password))
        account = cur.fetchone()
        if account:
            session['admin'] = True
            session['username'] = account['username']
            os.remove('static/logger_admin.txt')
            return redirect(url_for('index_dashboard'))
        else:
            flash('Username Atau Password Salah', 'Failed')
            return redirect(url_for('index_admin'))
    else:
        abort(405)

@app.route('/logout_admin', methods=['GET'])
def logout_admin():
    session.pop('admin', None)
    session.pop('username', None)
    flash('Anda Telah Keluar', 'Logout')
    return redirect(url_for('index_admin'))

@app.route('/dashboard')
def index_dashboard():
    if 'admin' in session:
        return render_template('admin/BerhasilLogin/dashboard.html')
    else:
        flash('Login Terlebih Dahulu', 'Failed')
        return redirect(url_for('index_admin'))

'''
ADMIN MOBILE LEGEND - START
'''
@app.route('/MobileLegend')
def dashboardML():
    if 'admin' in session:
        form    = Esport_Mobile_Legend()
        '''
        Myqsl Configuration
        '''
        conn    = mysql.connection
        cur     = conn.cursor()
        cur.execute('SELECT * FROM daftar_ml')
        result = cur.fetchall()
        return render_template('admin/BerhasilLogin/Dashboard_MobileLegend.html', form=form, daftar=result, )
    else:
        flash('Login Terlebih Dahulu', 'Failed')
        return redirect(url_for('index_admin'))

@app.route('/edit_ML', methods=['POST'])
def editML():
    if 'admin' in session:
        if request.method == 'POST':
            get_id              = request.form['id']
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
            '''
            Myqsl Configuration
            '''
            conn = mysql.connection
            cur = conn.cursor()
            cur.execute("UPDATE daftar_ml SET Team=%s, NamaKapten=%s, IGN_Kapten=%s, ID_Kapten=%s,\
                                            NamaPlayer2=%s, IGN_Player2=%s, ID_Player2=%s,\
                                            NamaPlayer3=%s, IGN_Player3=%s, ID_Player3=%s,\
                                            NamaPlayer4=%s, IGN_Player4=%s, ID_Player4=%s,\
                                            NamaPlayer5=%s, IGN_Player5=%s, ID_Player5=%s,\
                                            Email=%s, Whatsapp=%s, Waktu=%s\
                                            WHERE id=%s", 
                                            (get_Team, get_Nama_Kapten, get_IGN_Kapten, get_Id_Kapten,\
                                            get_Nama_Player_2, get_IGN_Player_2, get_Id_Player_2,\
                                            get_Nama_Player_3, get_IGN_Player_3, get_Id_Player_3,\
                                            get_Nama_Player_4, get_IGN_Player_4, get_Id_Player_4,\
                                            get_Nama_Player_5, get_IGN_Player_5, get_Id_Player_5,\
                                            get_Email, get_Whatsapp, get_waktu, get_id))
            conn.commit()
            flash('Berhasil Edit', 'Success')
            return redirect(url_for('dashboardML'))
        else:
            abort(405)
    else:
        flash('Login Terlebih Dahulu', 'Failed')
        return redirect(url_for('index_admin'))

@app.route('/delete_ML/<int:get_id>', methods=['GET'])
def deleteML(get_id):
    if 'admin' in session:
        conn = mysql.connection
        cur = conn.cursor()
        cur.execute("DELETE FROM daftar_ml WHERE id=%s" %(get_id))
        conn.commit()
        flash('Berhasil Hapus Team', 'Success')
        return redirect(url_for('dashboardML'))
    else:
        flash('Login Terlebih Dahulu', 'Failed')
        return redirect(url_for('index_admin'))
'''
ADMIN MOBILE LEGEND - END
'''

'''
VIEW ADMIN END
'''

'''
VIEW USER START
'''

'''
A J A X START
'''
@app.route('/get_turnament/<int:turnament>', methods=['GET'])
def getTurnament(turnament):
    conn    = mysql.connection
    cur     = conn.cursor()
    cur.execute("SELECT * FROM turnament WHERE Status=%s;" %(turnament))
    result_turnament = cur.fetchall()
    return render_template('user/ajax_turnament.html', ajax_turnament=result_turnament)

@app.route('/get_team/MLBB', methods=['GET'])
def getTeamML():
    conn = mysql.connection
    cur  = conn.cursor()
    cur.execute("SELECT Team,NamaKapten FROM daftar_ml;")
    result_team_ML = cur.fetchall()
    if len(result_team_ML) > 0:
        return render_template('user/ajax_team.html', ajax_team=result_team_ML)
    else:
        return 'Cooming Soon'

@app.route('/get_team/PUBG', methods=['GET'])
def getTeamPubg():
    conn = mysql.connection
    cur  = conn.cursor()
    cur.execute("SELECT Team,NamaKapten FROM daftar_pubg;")
    result_team_PUBG = cur.fetchall()
    if len(result_team_PUBG) > 0:
        return render_template('user/ajax_team.html', ajax_team=result_team_PUBG)
    else:
        return 'Cooming Soon'

'''
A J A X END
'''

'''
INDEX START
'''
@app.route('/')
def index():
    conn            = mysql.connection
    #GET Data Table Turnament
    cur_turnament   = conn.cursor()
    cur_turnament.execute("SELECT * FROM turnament WHERE Status=1;")
    result_turnament = cur_turnament.fetchall()
    return render_template('user/home.html', turnament=result_turnament)

@app.route('/team')
def index_team():
    return render_template('user/team.html')
'''
INDEX END
'''

'''
USER MOBILE LEGEND - START
'''
@app.route('/register_MLBB')
def register_ML():
    form = Esport_Mobile_Legend()
    return render_template('user/register.html', form=form)

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
                    get_BuktiPembayaran.save(os.path.join(app.config['UPLOAD_FOLDER_BUKTI'], get_Team + str(get_waktu.strftime("-%f")) + '.jpg'))
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
                                    get_Email, get_Whatsapp, get_Team + str(get_waktu.strftime("-%f")) + '.jpg', get_waktu))
                conn.commit()
                flash('Berhasil Terdaftar', 'Success')
                return redirect(url_for('index'))
            else:
                flash('Upload Gagal!', 'Failed')
                return redirect(url_for('index'))
        else:
            abort(405)
    else:
        return render_template('user/register.html', form=form)
'''
VIEW USER END
'''





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')