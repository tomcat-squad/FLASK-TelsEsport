from flask import (Flask, render_template, request, 
                    redirect, url_for, flash, abort,
                    session, Response)
from flask_mysql_connector import MySQL
from werkzeug.utils import secure_filename
from flask_wtf.csrf import CSRFProtect, CSRFError
from static.TOKEN import Esport_Mobile_Legend
import os
import datetime
import io
import csv

csrf = CSRFProtect()
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=1) #Expaired Session 1 Hari
csrf.init_app(app)

#==============================
# CUSTOM ERROR PAGE START
#==============================
@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    code_error = '400'
    pesan_error = 'TOKEN EXPAIRED, REFRESH PAGE'
    return render_template('error_page/error.html', code=code_error, pesan=pesan_error), 400

@app.errorhandler(403)
def page_forbiden(e):
    code_error = '403'
    pesan_error = 'FORBIDEN :)'
    return render_template('error_page/error.html', code=code_error, pesan=pesan_error), 403

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

@app.errorhandler(413)
def page_failed_upload(e):
    return render_template('error_page/upload_failed.html'), 413

@app.errorhandler(500)
def page_server_error(e):
    code_error = '500'
    pesan_error = 'SERVER ERROR :('
    return render_template('error_page/error.html', code=code_error, pesan=pesan_error), 500
#==============================
# CUSTOM ERROR PAGE END
#==============================


#==============================
# PROSES UPLOAD IMGAE START
#==============================
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 # SIZE MAX
ALLOWED_EXTENSIONS = set(['png', 'jpeg', 'jpg']) # EKSTENSION ALLOWED
UPLOAD_FOLDER_BUKTI = 'static/assets/bukti_transfer' # TEMPAT FOLDER
app.config['UPLOAD_FOLDER_BUKTI'] = UPLOAD_FOLDER_BUKTI
UPLOAD_FOLDER_THUMBNAIL = 'static/assets/thumbnail' # TEMPAT FOLDER
app.config['UPLOAD_FOLDER_THUMBNAIL'] = UPLOAD_FOLDER_THUMBNAIL
#==============================
# PROSES UPLOAD IMGAE END
#==============================


#==============================
# KONEKSI DATABASE START
#==============================
app.config['MYSQL_HOST']        = 'localhost'
app.config['MYSQL_USER']        = 'root'
app.config['MYSQL_PASSWORD']    = ''
app.config['MYSQL_DATABASE']    = 'tomcatsq_esport'
mysql = MySQL(app)
#==============================
# KONEKSI DATABASE END
#==============================

'''
VIEW ADMIN START
'''
#==============================
# EXPORT DATA MOBILE LEGEND START
#==============================
@app.route('/download/csv_mlbb')
def download_mlbb():
    if 'admin' in session:
        conn = mysql.connection
        cur = conn.cursor()
        cur.execute("SELECT * FROM daftar_ml;")
        result = cur.fetchall()
        output = io.StringIO()
        writer = csv.writer(output)

        line = ['ID', 'Nama Team', 
        'Nama Kapten', 'IGN-Kapten', 'ID-Kapten',
        'Player-2', 'IGN-Player2', 'ID-Player2',
        'Player-3', 'IGN-Player3', 'ID-Player3',
        'Player-4', 'IGN-Player4', 'ID-Player4',
        'Player-5', 'IGN-Player5', 'ID-Player5',
        'Player-6', 'IGN-Player6', 'ID-Player6',
        'Email', 'Nomor-WA', 'Waktu', 'order_id']
        writer.writerow(line)
        for row in result:
            line = [row[0], row[1], row[2], row[3], 
            row[4], row[5], row[6], row[7], row[8], 
            row[9], row[10], row[11], row[12], row[13], 
            row[14], row[15], row[16], row[17], row[18] , 
            row[19], row[20], row[21], row[22], row[23]]
            writer.writerow(line)
        output.seek(0)
        return Response(output, mimetype="text/csv", headers={"Content-Disposition":"attachment;filename=data_mlbb.csv"})
    else:
        flash('Login Terlebih Dahulu', 'Failed')
        return redirect(url_for('index_admin'))
#==============================
# EXPORT DATA MOBILE LEGEND END
#==============================

#==============================
# PROSES LOGIN ADMIN START
#==============================
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
        cur.execute("SELECT * FROM akun WHERE username=%s AND password=%s AND level='admin'", (get_username, get_password))
        account = cur.fetchone()
        if account:
            get_waktu = datetime.datetime.now()
            get_ip    = request.environ['REMOTE_ADDR']
            conn = mysql.connection
            cur = conn.cursor()
            cur.execute(f"UPDATE akun SET waktu='{get_waktu}', ip='{get_ip}' WHERE username='{get_username}'")
            conn.commit()
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
        conn    = mysql.connection
        #Statistik Mobile Legends
        cur_mlbb = conn.cursor()
        cur_mlbb.execute("SELECT * FROM daftar_ml;")
        result_mlbb = cur_mlbb.fetchall()
        #Logger Terakhir Login
        cur_log = conn.cursor()
        cur_log.execute("SELECT username,waktu,ip FROM akun ORDER BY waktu ASC LIMIT 1;")
        result_log = cur_log.fetchall()
        return render_template('admin/BerhasilLogin/dashboard.html', result_mlbb=result_mlbb, result_log=result_log)
    else:
        flash('Login Terlebih Dahulu', 'Failed')
        return redirect(url_for('index_admin'))
#==============================
# PROSES LOGIN ADMIN END
#==============================

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
        cur.execute("SELECT * FROM daftar_ml INNER JOIN bukti_pembayaran ON daftar_ml.order_id=bukti_pembayaran.order_id WHERE Genre='MLBB';")
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

            get_Nama_Player_6   = request.form['NamaPlayer6']
            get_IGN_Player_6    = request.form['IGN_Player6']
            get_Id_Player_6     = request.form['IdPlayer6']

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
                                            NamaPlayer6=%s, IGN_Player6=%s, ID_Player6=%s,\
                                            Email=%s, Whatsapp=%s, Waktu=%s\
                                            WHERE id=%s", 
                                            (get_Nama_Kapten, get_IGN_Kapten, get_Id_Kapten,\
                                            get_Nama_Player_2, get_IGN_Player_2, get_Id_Player_2,\
                                            get_Nama_Player_3, get_IGN_Player_3, get_Id_Player_3,\
                                            get_Nama_Player_4, get_IGN_Player_4, get_Id_Player_4,\
                                            get_Nama_Player_5, get_IGN_Player_5, get_Id_Player_5,\
                                            get_Nama_Player_6, get_IGN_Player_6, get_Id_Player_6,\
                                            get_Email, get_Whatsapp, get_waktu, get_id))
            conn.commit()
            flash('BERHASIL EDIT TEAM', 'Success')
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
        flash('BERHASIL HAPUS TEAM', 'Success')
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
            flash('BERHASIL BUAT TURNAMENT', 'Success')
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
            get_judul       = request.form['judul']
            get_genre       = request.form['genre']
            get_biaya       = request.form['biaya']
            get_slot        = request.form['slot']
            get_hadiah      = request.form['hadiah']
            get_tanggal     = request.form['waktu']
            get_status      = request.form['status']
            '''
            Myqsl Configuration
            '''
            conn = mysql.connection
            cur = conn.cursor()
            cur.execute("UPDATE turnament SET Judul=%s, Genre=%s, Biaya=%s, Slot=%s, \
                                                Hadiah=%s, Waktu=%s, Status=%s WHERE id=%s",
                                                (get_judul, get_genre, \
                                                get_biaya, get_slot, get_hadiah, get_tanggal, get_status, get_id))
            conn.commit()
            flash('BERHASIL EDIT TURNAMENT', 'Success')
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
        flash('BERHASIL HAPUS TURNAMENT', 'Success')
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
        form    = Esport_Mobile_Legend()
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
        form=form,
        jadwal_mlbb=result_jadwal_MLBB,
        jadwal_pubg=result_jadwal_PUBG,
        jadwal_pb=result_jadwal_PB)
    else:
        flash('Login Terlebih Dahulu', 'Failed')
        return redirect(url_for('index_admin'))  

@app.route('/uploadJadwal', methods=['POST'])
def uploadJadwal():
    if 'admin' in session:
        if request.method == 'POST':
            get_team      = request.form['Team']
            get_waktu     = request.form['Jam']
            get_tanggal   = request.form['Tanggal']
            get_genre     = request.form['Genre']
            conn = mysql.connection
            cur = conn.cursor()
            cur.execute("INSERT INTO turnament_jadwal (Team, Jam, Tanggal, Genre) VALUES (%s,%s,%s,%s)", 
                                                (get_team, get_waktu, get_tanggal, get_genre))
            conn.commit()
            flash('BERHASIL BUAT JADWAL BERMAIN', 'Success')
            return redirect(url_for('dashboardJadwal'))
        else:
            abort(405)
    else:
        flash('Login Terlebih Dahulu', 'Failed')
        return redirect(url_for('index_admin'))

@app.route('/edit_Jadwal_MLBB', methods=['POST'])
def editJadwalMLBB():
    if 'admin' in session:
        if request.method == 'POST':
            get_id        = request.form['id']
            get_team      = request.form['Team']
            get_waktu     = request.form['Jam']
            get_tanggal   = request.form['Tanggal']
            conn = mysql.connection
            cur = conn.cursor()
            cur.execute("UPDATE turnament_jadwal SET Team=%s, Jam=%s, Tanggal=%s WHERE id=%s",
                                                    (get_team, get_waktu, get_tanggal, get_id))
            conn.commit()
            flash('BERHASIL EDIT JADWAL BERMAIN', 'Success')
            return redirect(url_for('dashboardJadwal'))
    else:
        flash('Login Terlebih Dahulu', 'Failed')
        return redirect(url_for('index_admin'))  

@app.route('/delete_Jadwal_MLBB/<int:get_id>', methods=['GET'])
def deleteJadwal(get_id):
    if 'admin' in session:
        conn = mysql.connection
        cur = conn.cursor()
        cur.execute("DELETE FROM turnament_jadwal WHERE id=%s" %(get_id))
        conn.commit()
        flash('BERHASIL HAPUS JADWAL BERMAIN', 'Success')
        return redirect(url_for('dashboardJadwal'))
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
#SECTION HOME START
#===================
@app.route('/')
def index():
    conn            = mysql.connection

    #GET Data Table Turnament MLBB Aktif
    cur_turnament_MLBB_Aktif   = conn.cursor()
    cur_turnament_MLBB_Aktif.execute("SELECT * FROM turnament WHERE Genre='MLBB'AND Status=1 ORDER BY Waktu DESC;")
    result_turnament_MLBB_Aktif = cur_turnament_MLBB_Aktif.fetchall()

    #GET Data Table Turnament MLBB Selesai
    cur_turnament_MLBB_Selesai   = conn.cursor()
    cur_turnament_MLBB_Selesai.execute("SELECT * FROM turnament WHERE Genre='MLBB'AND Status=0 ORDER BY Waktu DESC;")
    result_turnament_MLBB_Selesai = cur_turnament_MLBB_Selesai.fetchall()

    #GET Data Table Turnament PB Aktif
    cur_turnament_PB_Aktif   = conn.cursor()
    cur_turnament_PB_Aktif.execute("SELECT * FROM turnament WHERE Genre='PB'AND Status=1 ORDER BY Waktu DESC;")
    result_turnament_PB_Aktif = cur_turnament_PB_Aktif.fetchall()

    #GET Data Table Turnament PB Selesai
    cur_turnament_PB_Selesai   = conn.cursor()
    cur_turnament_PB_Selesai.execute("SELECT * FROM turnament WHERE Genre='PB'AND Status=0 ORDER BY Waktu DESC;")
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
    cur_jadwal_MLBB.execute("SELECT * FROM turnament_jadwal WHERE Genre='MLBB' ORDER BY Tanggal ASC;")
    result_jadwal_MLBB = cur_jadwal_MLBB.fetchall()

    #GET Data Table Jadwal PUBG
    cur_jadwal_PUBG   = conn.cursor()
    cur_jadwal_PUBG.execute("SELECT * FROM turnament_jadwal WHERE Genre='PUBG' ORDER BY Tanggal ASC;")
    result_jadwal_PUBG = cur_jadwal_PUBG.fetchall()

    #GET Data Table Jadwal PB
    cur_jadwal_PB   = conn.cursor()
    cur_jadwal_PB.execute("SELECT * FROM turnament_jadwal WHERE Genre='PB' ORDER BY Tanggal ASC ;")
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
    session.pop('success', None)
    session.pop('team', None)
    session.pop('genre', None)
    return render_template('user/team.html',
    team_MLBB=result_team_MLBB)

@app.route('/bagan')
def index_bagan():
    return render_template('user/bagan.html')
#===================
#SECTION HOME END
#===================

#===================
#REGISTER MOBILE LEGEND START
#===================
@app.route('/register_MLBB')
def register_ML():
    form = Esport_Mobile_Legend()
    return render_template('user/register.html', form=form) # Index Register
    #return render_template('error_page/close.html') # Index Jika Sudah Tutup Pendaftaran

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

            get_Nama_Player_6   = request.form['NamaPlayer6']
            get_IGN_Player_6    = request.form['IGN_Player6']
            get_Id_Player_6     = request.form['IdPlayer6']

            get_waktu           = datetime.datetime.now()
            order_id            = datetime.datetime.now().strftime("%H%M%S%d")
            '''
            Myqsl Configuration
            '''
            conn = mysql.connection
            cur = conn.cursor()
            cur.execute(f"SELECT Team FROM daftar_ml WHERE Team='{get_Team}'")
            result_team = cur.fetchall()
            if len(result_team) == 1:
                return render_template('error_page/register_failed.html')
            else:
                cur.execute("INSERT INTO daftar_ml (Team, NamaKapten, IGN_Kapten, ID_Kapten,\
                                                    NamaPlayer2, IGN_Player2, ID_Player2,\
                                                    NamaPlayer3, IGN_Player3, ID_Player3,\
                                                    NamaPlayer4, IGN_Player4, ID_Player4,\
                                                    NamaPlayer5, IGN_Player5, ID_Player5,\
                                                    NamaPlayer6, IGN_Player6, ID_Player6,\
                                                    Email, Whatsapp, Waktu, order_id)\
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
                                    (get_Team, get_Nama_Kapten, get_IGN_Kapten, get_Id_Kapten,
                                    get_Nama_Player_2, get_IGN_Player_2, get_Id_Player_2,
                                    get_Nama_Player_3, get_IGN_Player_3, get_Id_Player_3,
                                    get_Nama_Player_4, get_IGN_Player_4, get_Id_Player_4,
                                    get_Nama_Player_5, get_IGN_Player_5, get_Id_Player_5,
                                    get_Nama_Player_6, get_IGN_Player_6, get_Id_Player_6,
                                    get_Email, get_Whatsapp, get_waktu, order_id))
                conn.commit()
                #Create Session
                session['success'] = True
                session['genre'] = 'MLBB'
                session['order_id'] = order_id
                return redirect(url_for('indexPembayaran', order_id=order_id, genre=session['genre']))
        else:
            abort(405)
    else:
        return render_template('user/register.html', form=form)
#===================
#REGISTER MOBILE LEGEND END
#===================

#========================
# UPLOAD BUKTI PEMBAYARAN START
#========================
@app.route('/pembayaran/<int:order_id>/<genre>/')
def indexPembayaran(order_id, genre):
    conn = mysql.connection
    cur = conn.cursor()
    cur.execute(f"SELECT Team FROM daftar_ml WHERE order_id='{order_id}'")
    result_order_id = cur.fetchall()
    if len(result_order_id) == 1:
        form = Esport_Mobile_Legend()
        return render_template('user/pembayaran.html', form=form, order_id=order_id, get_genre=genre)
    else:
        return redirect(url_for('index_team'))

@app.route('/upload_bukti/', methods=['POST'])
def uploadBukti():
    if request.method == 'POST':
        req_order_id = request.args['order_id']
        req_genre= request.args['genre']
        conn = mysql.connection
        cur = conn.cursor()
        cur.execute(f"SELECT Team FROM daftar_ml WHERE order_id='{req_order_id}'")
        result_order_id = cur.fetchall()
        if len(result_order_id) == 1:
            get_BuktiPembayaran = request.files['bukti-tf']
            get_waktu = datetime.datetime.now()
            if get_BuktiPembayaran and allowed_file(get_BuktiPembayaran.filename):
                try:
                    get_BuktiPembayaran.save(os.path.join(app.config['UPLOAD_FOLDER_BUKTI'], req_order_id  + str(get_waktu.strftime("-%f-%d-%B")) +'.jpg'))
                except:
                    abort(403)
                '''
                Myqsl Configuration
                '''
                conn = mysql.connection
                cur = conn.cursor()
                cur.execute(f"SELECT order_id FROM bukti_pembayaran WHERE order_id='{req_order_id}'")
                result_team = cur.fetchall()
                if len(result_team) == 1:
                    os.remove('static/assets/bukti_transfer/' + req_order_id + str(get_waktu.strftime("-%f-%d-%B")) + '.jpg')
                    flash('Anda Sudah Terdaftar', 'Success')
                    return redirect(url_for('index_team'))
                else:
                    cur.execute("INSERT INTO bukti_pembayaran (Foto, Genre, order_id) VALUES (%s,%s,%s)", (req_order_id + str(get_waktu.strftime("-%f-%d-%B")) + '.jpg', req_genre, req_order_id))
                    conn.commit()
                    flash('Berhasil Terdaftar', 'Success')
                    return redirect(url_for('index_team'))
        else:
            return render_template('error_page/upload_failed.html')
    else:
        abort(405)
'''
VIEW USER END
'''





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')