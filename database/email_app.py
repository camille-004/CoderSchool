import pymysql.cursors
from flask import Flask
from flask import request

app = Flask(__name__)


CONFIG = {'host': '127.0.0.1',
		  'user': 'root',
		  'password': 'root',
		  'db': 'coder_school',
		  'charset': 'utf8mb4',
		  'cursorclass': pymysql.cursors.DictCursor
		 }
QUERY = 'SELECT first_name, last_name FROM names WHERE email= '

@app.route('/name_fetch')
def email_fetch():
	email = request.args.get('email')
	connection = pymysql.connect(**CONFIG)
	try:
		with connection.cursor() as cursor:
			sql = QUERY + "'" + email + "';"
			cursor.execute(sql)
			result = cursor.fetchone()
			return str(result)
	finally:
		connection.close()
 
