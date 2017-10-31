import pymysql.cursors
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# TODO 1: Create a messages table `messages` with the following columns (id INT(20) AUTO_INCREMENT (PRIMARY_KEY), message VARCHAR(255), recipient_user_id INT(20), sender_user_id INT(20))


CONFIG = {'host': '127.0.0.1',
		  'user': 'root',
		  'password': 'root',
		  'db': 'coder_school',
		  'charset': 'utf8mb4',
		  'cursorclass': pymysql.cursors.DictCursor
		 }
GET_USER_ID_QUERY = "SELECT `id` FROM `users` WHERE first_name = '%s' AND last_name = '%s';"
INSERT_USER_MESSAGE = "INSERT INTO `messages` (message, recipient_user_id, sender_user_id) VALUES ('%s', %s, %s);"
GET_MESSAGES_FOR_USER = """SELECT m.id as message_id, m.message as message, u.first_name as sender_first_name, u.last_name as sender_last_name
FROM messages m
JOIN users u
ON m.sender_user_id = u.id
WHERE m.recipient_user_id = %s
ORDER BY message_id DESC;
"""
def exec_query(query, params):
	# This function should return either a List containing 1 item (fetchone())
	# OR a List of multiple items
	# OR the ID of the last inserted row (for inserts only)
	connection = pymysql.connect(**CONFIG)
	try:
		with connection.cursor() as cursor:
			sql = query % params
			cursor.execute(sql)
			if 'INSERT' in query:
				connection.commit()
			result = cursor.fetchone()
			if result == None:
				return cursor.lastrowid
			else:
				return jsonify(result)
	finally:
		connection.close()

def exec_query_list(query, params):
	connection = pymysql.connect(**CONFIG)
	try:
		with connection.cursor() as cursor:
			sql = query % params
			cursor.execute(sql)
			result = cursor.fetchall()
			return jsonify(result)
	finally:
		connection.close()

@app.route('/users')
def get_user_id():
	# Gets recipient's ID
	first_name = request.args.get('first_name')
	last_name = request.args.get('last_name')
	return exec_query(GET_USER_ID_QUERY, (first_name, last_name))

@app.route('/users/<int:user_id>/message', methods=['GET', 'POST'])
def user_endpoint(user_id):
	if request.method == 'GET':		
		return read_messages(user_id)
	elif request.method == 'POST':
		body = request.json
		response_body = {}
		response_body['message_id'] = send_message(user_id, body["sender_id"], body["message"])
		return jsonify(response_body)

def send_message(recipient_id, sender_id, message):
	return exec_query(INSERT_USER_MESSAGE, (message, recipient_id, sender_id))

def read_messages(user_id):
	# Recipient reads message
	return exec_query_list(GET_MESSAGES_FOR_USER, (user_id))