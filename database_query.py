import pymysql.cursors
import sys

CONFIG = {'host': '127.0.0.1',
		  'user': 'root',
		  'password': 'root',
		  'db': 'coder_school',
		  'charset': 'utf8mb4',
		  'cursorclass': pymysql.cursors.DictCursor
		 }
QUERY = 'SELECT first_name, last_name FROM names WHERE email= '

def main(req, res):
	email = sys.argv[1]
	connection = pymysql.connect(**CONFIG)
	try:
		with connection.cursor() as cursor:
			sql = QUERY + "'" + email + "';"
			cursor.execute(sql)
			result = cursor.fetchone()
			print(result)
	finally:
		connection.close()
  
if __name__ == "__main__":
  main()
