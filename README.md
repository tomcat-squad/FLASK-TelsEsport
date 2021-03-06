<p align="center"> 
  <img alt="Tels Esport" src="https://user-images.githubusercontent.com/67460437/105674445-191c3700-5f1a-11eb-94ba-c8cc6d603243.jpg" height="200" />
  <h3 align="center"><b>Tels E-Sport</b></h3>
</p>
<p align="center">
   <a href="https://github.com/tomcat-squad/FLASK-TelsEsport/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/tomcat-squad/FLASK-TelsEsport?color=2b9348"></a>
  <a href="https://github.com/tomcat-squad/FLASK-TelsEsport/pulls"><img src="https://img.shields.io/github/issues-pr/tomcat-squad/FLASK-TelsEsport" alt="Pull Requests Badge"/></a>
  <a href="https://github.com/tomcat-squad/FLASK-TelsEsport"><img src="https://img.shields.io/badge/version-1.0-blueviolet" alt="Version"/></a>
  <a href="https://github.com/tomcat-squad/FLASK-TelsEsport"><img src="https://img.shields.io/badge/TomcatSquad-website%20project-blue" alt="Version"/></a>
  <a href="https://github.com/tomcat-squad/FLASK-TelsEsport/network/members"><img src="https://img.shields.io/github/forks/tomcat-squad/FLASK-TelsEsport" alt="Forks Badge"/></a><br>
  Website Daftar Turnament
  <br />
  <a href="https://github.com/tomcat-squad/FLASK-TelsEsport/issues/new/choose">Dokumentasi</a>
  -
  <a href="https://github.com/tomcat-squad/FLASK-TelsEsport/issues/new/choose">Laporkan Bug</a>
  -
  <a href="https://github.com/tomcat-squad/FLASK-TelsEsport/issues/new/choose">Permintaan Fitur</a>
    -
  <a href="https://github.com/tomcat-squad/FLASK-TelsEsport/blob/main/.github/ISSUE_TEMPLATE/kontribusi.md">Kontribusi</a>
</p>
<br>

## Daftar Isi
- [Tentang](#tentang-)
- [Dibuat Dengan Apa?](#teknologi-yang-digunakan-)
- [Desain UI/UX](#desain-uiux-)
- [Versi Python](#python-version-)
- [Cara Install](#installation-%EF%B8%8F)
  - [Linux - Mysql](#linux-mysql)
  - [Windows - Xampp](#windows-xampp)
- [Keamanan](#security-%EF%B8%8F)
- [Uji Keamanan](#testing-guide-)
    
## Tentang 🤷
Tels Esport merupakan turnament yang diselengarakan oleh tomcat squad, Pertama kali dibuat oleh angkatan 10 dan baru dijalankan oleh angkatan 11. 
Genre yang dimainkan dari Mobile, Desktop, Hingga Console..

## Teknologi Yang Digunakan 🤖
[![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=ffffff)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=Flask&logoColor=ffffff)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/-MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=ffffff)](https://www.mysql.com/)
![HTML5](https://img.shields.io/badge/-HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/-CSS-254bdd?style=flat-square&logo=css3&logoColor=white)
![Jinja](https://img.shields.io/badge/-Jinja-b41717?style=flat-square&logo=Jinja&logoColor=white) 
![Javascript](https://img.shields.io/badge/-Javascript-efd81d?style=flat-square&logo=Javascript&logoColor=black)

## Desain UI/UX ✨
<a href="https://www.figma.com/file/CGDbfs8rIKYXZYJnDZMnva/TelsEsport?node-id=0%3A1">Figma Tels Esport</a>

## Python Version 🐍
<a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.6-purple" alt="Version"/></a>
<a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.7-orange" alt="Version"/></a>
<a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.8-blue" alt="Version"/></a>

## Installation 🛠️ 
1. Install module yang dibutuhkan
```
python -m pip install -r requirements.txt
```
2. Import database <a href="https://raw.githubusercontent.com/tomcat-squad/FLASK-TelsEsport/main/Apps/BACK-END/tomcat_esport.sql">tomcat_esport.sql</a> ke mysql
#### Linux (Mysql)
```sql
#Buat Database
mysql -u root -p 
CREATE DATABASE tomcat_esport;
#Import Database
use tomcat_esport; source /home/tomcatsq/tomcat_esport.sql
quit;
```
#### Windows (XAMPP)
```
1. Buat database di phpmyadmin
2. Import tomcat_esport.sql ke database yang dibuat.
3. Selesai
```
3. Sesuaikan user database pada file app.py
```python
app.config['MYSQL_HOST']        = 'localhost'
app.config['MYSQL_USER']        = 'root'
app.config['MYSQL_PASSWORD']    = ''
app.config['MYSQL_DATABASE']    = 'tomcat_esport'
mysql = MySQL(app)
```
4. Sesuaikan directory untuk menyimpan file yang di upload user
```python
UPLOAD_FOLDER_BUKTI = 'static/assets/bukti_transfer'
app.config['UPLOAD_FOLDER_BUKTI'] = UPLOAD_FOLDER_BUKTI

UPLOAD_FOLDER_THUMBNAIL = 'static/assets/thumbnail'
app.config['UPLOAD_FOLDER_THUMBNAIL'] = UPLOAD_FOLDER_THUMBNAIL
```
5. Sesuaikan directory file .htacces untuk blacklist ip address user nakal
```python
#Blacklist Ip Di Htaccess
if len(logger_read) == 5:
    htaccess = open('static/.htaccess', 'a')
    htaccess.write(f'deny from {logger_read[0]}allow from all\n')
    htaccess.close()
    os.remove('static/logger_admin.txt')
```
6. Jalankan file app.py
```
python app.py
```
7. Buka browser 
```
http://127.0.0.1:5000
```
## Security 🛡️
- CSRF Token
- Filter Ekstension
- Filter Size Upload Image
- Input Validation
- Block IP Attacker

## Testing Guide 🕵🏼
Untuk pentester yang ingin melakukan pengujian bisa membaca ketentuanya <a href="https://github.com/tomcat-squad/FLASK-TelsEsport/blob/main/.github/ISSUE_TEMPLATE/pentester.md">disini</a>
