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

UPLOAD_FOLDER_THUMBNAIL = 'static/assets/thumbnail'
ALLOWED_EXTENSIONS = set(['png', 'jpeg', 'jpg'])
app.config['UPLOAD_FOLDER_THUMBNAIL'] = UPLOAD_FOLDER_THUMBNAIL

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

@app.route('/admin/dashboard')
def index_dashboard():
    if 'admin' in session:
        return render_template('admin/BerhasilLogin/dashboard.html')
    else:
        flash('Login Terlebih Dahulu', 'Failed')
        return redirect(url_for('index_admin'))

#==============================
# DASHBOARD MOBILE LEGEND START
#==============================
@app.route('/admin/dashboard_MobileLegend')
def dashboardML():
    if 'admin' in session:
        form    = Esport_Mobile_Legend()
        '''
        Myqsl Configuration
        '''
        #INNER JOIN 2 Table
        conn    = mysql.connection
        cur     = conn.cursor()
        cur.execute("SELECT * FROM daftar_ml INNER JOIN bukti_pembayaran ON daftar_ml.Team=bukti_pembayaran.Team WHERE Genre='MLBB';")
        result_online = cur.fetchall()
        #SELECT ALL 1 TABLE
        cur_cod = conn.cursor()
        cur_cod.execute("SELECT * FROM daftar_ml;")
        result_cod = cur_cod.fetchall()
        return render_template('admin/BerhasilLogin/dashboard_MobileLegend.html', form=form, daftar_online=result_online, daftar_cod=result_cod)
    else:
        flash('Login Terlebih Dahulu', 'Failed')
        return redirect(url_for('index_admin'))

@app.route('/edit_ML', methods=['POST'])
def editML():
    if 'admin' in session:
        if request.method == 'POST':
            get_id              = request.form['id']
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
            cur.execute("UPDATE daftar_ml SET NamaKapten=%s, IGN_Kapten=%s, ID_Kapten=%s,\
                                            NamaPlayer2=%s, IGN_Player2=%s, ID_Player2=%s,\
                                            NamaPlayer3=%s, IGN_Player3=%s, ID_Player3=%s,\
                                            NamaPlayer4=%s, IGN_Player4=%s, ID_Player4=%s,\
                                            NamaPlayer5=%s, IGN_Player5=%s, ID_Player5=%s,\
                                            Email=%s, Whatsapp=%s, Waktu=%s\
                                            WHERE id=%s", 
                                            (get_Nama_Kapten, get_IGN_Kapten, get_Id_Kapten,\
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
#==============================
# DASHBOARD MOBILE LEGEND END
#==============================

#===========================
# DASHBOARD TURNAMENT START
#===========================
@app.route('/admin/dashboard_Turnament')
def dashboardTurnament():
    if 'admin' in session:
        form = Esport_Mobile_Legend()
        conn    = mysql.connection
        cur     = conn.cursor()
        cur.execute("SELECT * FROM turnament;")
        result_turnament = cur.fetchall()
        return render_template('admin/BerhasilLogin/dashboard_turnament.html', turnament=result_turnament, form=form)
    else:
        flash('Login Terlebih Dahulu', 'Failed')
        return redirect(url_for('index_admin'))

@app.route('/uploadTurnament', methods=['POST'])
def uploadTurnament():
    if 'admin' in session:
        if request.method == 'POST':
            get_thumbnail   = request.files['thumbnail']
            get_judul       = request.form['judul']
            get_genre       = request.form['genre']
            get_biaya       = request.form['biaya']
            get_slot        = request.form['slot']
            get_hadiah      = request.form['hadiah']
            get_tanggal     = request.form['waktu']
            date_time       = datetime.datetime.now()
            get_status      = 1
            if get_thumbnail and allowed_file(get_thumbnail.filename):
                try:
                    filename = get_thumbnail.filename
                    get_thumbnail.save(os.path.join(app.config['UPLOAD_FOLDER_THUMBNAIL'], get_genre + str(date_time.strftime("-%d-%B-%Y")) +'.jpg'))
                except:
                    abort(403)
            '''
            Myqsl Configuration
            '''
            conn = mysql.connection
            cur = conn.cursor()
            cur.execute("INSERT INTO turnament (Thumbnail, Judul, Genre, Biaya, Slot, \
                                                Hadiah, Waktu, Status) \
                                                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", 
                                                (get_genre + str(date_time.strftime("-%d-%B-%Y")) +'.jpg', get_judul, 
                                                get_genre, get_biaya, get_slot, get_hadiah, get_tanggal, get_status))
            conn.commit()
            flash('Berhasil Buat Turnament', 'Success')
            return redirect(url_for('dashboardTurnament'))
        else:
            abort(405)
    else:
        flash('Login Terlebih Dahulu', 'Failed')
        return redirect(url_for('index_admin'))
        
@app.route('/edit_Turnament', methods=['POST'])
def editTurnament():
    if 'admin' in session:
        if request.method == 'POST':
            get_id          = request.form['id']
            get_thumbnail   = request.files['thumbnail']
            get_judul       = request.form['judul']
            get_genre       = request.form['genre']
            get_biaya       = request.form['biaya']
            get_slot        = request.form['slot']
            get_hadiah      = request.form['hadiah']
            get_tanggal     = request.form['waktu']
            get_status      = request.form['status']
            date_time       = datetime.datetime.now()
            if get_thumbnail and allowed_file(get_thumbnail.filename):
                try:
                    filename = get_thumbnail.filename
                    get_thumbnail.save(os.path.join(app.config['UPLOAD_FOLDER_THUMBNAIL'], get_genre + str(date_time.strftime("-%d-%B-%Y")) +'.jpg'))
                except:
                    abort(403)
            '''
            Myqsl Configuration
            '''
            conn = mysql.connection
            cur = conn.cursor()
            cur.execute("UPDATE turnament SET Thumbnail=%s, Judul=%s, Genre=%s, Biaya=%s, Slot=%s, \
                                                Hadiah=%s, Waktu=%s, Status=%s WHERE id=%s",
                                                (get_genre + str(date_time.strftime("-%d-%B-%Y")) +'.jpg', get_judul, get_genre, \
                                                get_biaya, get_slot, get_hadiah, get_tanggal, get_status, get_id))
            conn.commit()
            flash('Berhasil Edit', 'Success')
            return redirect(url_for('dashboardTurnament'))  
        else:
            abort(405)                             
    else:
        flash('Login Terlebih Dahulu', 'Failed')
        return redirect(url_for('index_admin'))

@app.route('/delete_Turnament/<int:get_id>', methods=['GET'])
def deleteTurnament(get_id):
    if 'admin' in session:
        conn = mysql.connection
        cur = conn.cursor()
        cur.execute("DELETE FROM turnament WHERE id=%s" %(get_id))
        conn.commit()
        flash('Berhasil Hapus Team', 'Success')
        return redirect(url_for('dashboardTurnament'))
    else:
        flash('Login Terlebih Dahulu', 'Failed')
        return redirect(url_for('index_admin'))   
        
#===========================
# DASHBOARD TURNAMENT END
#===========================

#===========================
# DASHBOARD JADWAL START
#===========================
@app.route('/admin/Jadwal')
def dashboardJadwal():
    if 'admin' in session:
        conn = mysql.connection

        #GET Data Table Jadwal MLBB
        cur_jadwal_MLBB   = conn.cursor()
        cur_jadwal_MLBB.execute("SELECT * FROM turnament_jadwal WHERE Genre='MLBB';")
        result_jadwal_MLBB = cur_jadwal_MLBB.fetchall()

        #GET Data Table Jadwal PUBG
        cur_jadwal_PUBG   = conn.cursor()
        cur_jadwal_PUBG.execute("SELECT * FROM turnament_jadwal WHERE Genre='PUBG';")
        result_jadwal_PUBG = cur_jadwal_PUBG.fetchall()

        #GET Data Table Jadwal PB
        cur_jadwal_PB   = conn.cursor()
        cur_jadwal_PB.execute("SELECT * FROM turnament_jadwal WHERE Genre='PB';")
        result_jadwal_PB = cur_jadwal_PB.fetchall()

        return render_template('/admin/BerhasilLogin/dashboard_jadwal.html',
        jadwal_mlbb=result_jadwal_MLBB,
        jadwal_pubg=result_jadwal_PUBG,
        jadwal_pb=result_jadwal_PB)
    else:
        flash('Login Terlebih Dahulu', 'Failed')
        return redirect(url_for('index_admin'))  

#===========================
# DASHBOARD JADWAL END
#===========================

'''
VIEW ADMIN END
'''

'''
VIEW USER START
'''

#===================
#URL FOR AJAX START
#===================
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
#===================
#URL FOR AJAX END
#===================

#===================
#SECTION HOME START
#===================
@app.route('/')
def index():
    conn            = mysql.connection

    #GET Data Table Turnament MLBB Aktif
    cur_turnament_MLBB_Aktif   = conn.cursor()
    cur_turnament_MLBB_Aktif.execute("SELECT * FROM turnament WHERE Genre='MLBB'AND Status=1;")
    result_turnament_MLBB_Aktif = cur_turnament_MLBB_Aktif.fetchall()

    #GET Data Table Turnament MLBB Selesai
    cur_turnament_MLBB_Selesai   = conn.cursor()
    cur_turnament_MLBB_Selesai.execute("SELECT * FROM turnament WHERE Genre='MLBB'AND Status=0;")
    result_turnament_MLBB_Selesai = cur_turnament_MLBB_Selesai.fetchall()

    #GET Data Table Turnament PB Aktif
    cur_turnament_PB_Aktif   = conn.cursor()
    cur_turnament_PB_Aktif.execute("SELECT * FROM turnament WHERE Genre='PB'AND Status=1;")
    result_turnament_PB_Aktif = cur_turnament_PB_Aktif.fetchall()

    #GET Data Table Turnament PB Selesai
    cur_turnament_PB_Selesai   = conn.cursor()
    cur_turnament_PB_Selesai.execute("SELECT * FROM turnament WHERE Genre='PB'AND Status=0;")
    result_turnament_PB_Selesai = cur_turnament_PB_Selesai.fetchall()

    return render_template('user/home.html', 
    turnament_MLBB_Aktif=result_turnament_MLBB_Aktif,
    turnament_MLBB_Selesai=result_turnament_MLBB_Selesai,
    turnament_PB_Aktif=result_turnament_PB_Aktif,
    turnament_PB_Selesai=result_turnament_PB_Selesai)

@app.route('/jadwal')
def index_jadwal():
    conn            = mysql.connection
    #GET Data Table Jadwal MLBB
    cur_jadwal_MLBB   = conn.cursor()
    cur_jadwal_MLBB.execute("SELECT * FROM turnament_jadwal WHERE Genre='MLBB';")
    result_jadwal_MLBB = cur_jadwal_MLBB.fetchall()

    #GET Data Table Jadwal PUBG
    cur_jadwal_PUBG   = conn.cursor()
    cur_jadwal_PUBG.execute("SELECT * FROM turnament_jadwal WHERE Genre='PUBG';")
    result_jadwal_PUBG = cur_jadwal_PUBG.fetchall()

    #GET Data Table Jadwal PB
    cur_jadwal_PB   = conn.cursor()
    cur_jadwal_PB.execute("SELECT * FROM turnament_jadwal WHERE Genre='PB';")
    result_jadwal_PB = cur_jadwal_PB.fetchall()

    return render_template('user/jadwal.html', 
    jadwal_mlbb=result_jadwal_MLBB,
    jadwal_pubg=result_jadwal_PUBG,
    jadwal_pb=result_jadwal_PB)

@app.route('/team')
def index_team():
    conn            = mysql.connection
    #GET Data Nama Team
    cur_team_MLBB   = conn.cursor()
    cur_team_MLBB.execute("SELECT id,Team,NamaKapten FROM daftar_ml;")
    result_team_MLBB = cur_team_MLBB.fetchall()
    return render_template('user/team.html',
    team_MLBB=result_team_MLBB)
#===================
#SECTION HOME END
#===================

#===================
#MOBILE LEGEND START
#===================
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
                                                Email, Whatsapp, Waktu)\
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                                %s,%s,%s,%s,%s,%s,%s,%s,%s)", 
                                (get_Team, get_Nama_Kapten, get_IGN_Kapten, get_Id_Kapten,
                                get_Nama_Player_2, get_IGN_Player_2, get_Id_Player_2,
                                get_Nama_Player_3, get_IGN_Player_3, get_Id_Player_3,
                                get_Nama_Player_4, get_IGN_Player_4, get_Id_Player_4,
                                get_Nama_Player_5, get_IGN_Player_5, get_Id_Player_5,
                                get_Email, get_Whatsapp, get_waktu))
            conn.commit()
            #Create Session
            session['success'] = True
            session['team'] = get_Team
            session['genre'] = 'MLBB'
            return redirect(url_for('indexPembayaran'))
        else:
            abort(405)
    else:
        return render_template('user/register.html', form=form)
#===================
#MOBILE LEGEND END
#===================

#========================
# Upload Bukti Pembayaran
#========================
@app.route('/pembayaran')
def indexPembayaran():
    if 'success' in session:
        form = Esport_Mobile_Legend()
        return render_template('user/pembayaran.html', form=form)
    else:
        return redirect(url_for('index'))

@app.route('/upload_bukti', methods=['POST'])
def uploadBukti():
    if request.method == 'POST':
        get_team = session['team']
        get_genre = session['genre']
        get_BuktiPembayaran = request.files['bukti-tf']
        get_waktu = datetime.datetime.now()
        if get_BuktiPembayaran and allowed_file(get_BuktiPembayaran.filename):
            try:
                filename = get_BuktiPembayaran.filename
                get_BuktiPembayaran.save(os.path.join(app.config['UPLOAD_FOLDER_BUKTI'], get_team  + str(get_waktu.strftime("-%f-%d-%B")) +'.jpg'))
            except:
                abort(403)
            '''
            Myqsl Configuration
            '''
            conn = mysql.connection
            cur = conn.cursor()
            cur.execute("INSERT INTO bukti_pembayaran (Team, Foto, Genre) VALUES (%s,%s,%s)", (get_team, get_team + str(get_waktu.strftime("-%f-%d-%B")) + '.jpg', get_genre))
            conn.commit()
            session.pop('success', None)
            session.pop('team', None)
            session.pop('genre', None)
            flash('Berhasil Terdaftar', 'Success')
            return redirect(url_for('index_team'))
        else:
            flash('Upload Gagal!', 'Failed')
            return redirect(url_for('register_ML'))
    else:
        abort(405)
'''
VIEW USER END
'''





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')