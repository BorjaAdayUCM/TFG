from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ZnvzV4whRfi4xpQw'
app.config['MYSQL_DB'] = 'bd_tfg'
 
mysql = MySQL(app)

with app.app_context():
	print(mysql.connection)