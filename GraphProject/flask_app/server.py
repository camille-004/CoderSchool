import pymysql.cursors
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

CONFIG = {'host': '127.0.0.1',
		  'user': 'root',
		  'password': 'root',
		  'db': 'graph_db',
		  'charset': 'utf8mb4',
		  'cursorclass': pymysql.cursors.DictCursor
		 }

GET_FOLLOWERS_QUERY = '''SELECT id, val 
FROM neighbors 
JOIN nodes 
ON neighbors.neighbor_id = nodes.id
WHERE node_id = %s;'''
GET_FOLLOWING_QUERY = '''SELECT id, val FROM neighbors
JOIN nodes ON nodes.id = neighbors.neighbor_id
WHERE node_id = %s;'''


def exec_query_list(connection, query, params = ()):
	with connection.cursor() as cursor:
		sql = query % params
		cursor.execute(sql)
		result = cursor.fetchall()
		if 'INSERT' in query:
				connection.commit()
		return result

@app.route('/followers/<int:user_id>')
def get_followers(user_id):
	connection = None
	try:
		connection = pymysql.connect(**CONFIG)
		followers = exec_query_list(connection, GET_FOLLOWERS_QUERY, (user_id))
		return jsonify(followers)
	finally:
		connection.close()

@app.route('/following/<int:user_id>')
def get_following(user_id):
	connection = None
	try:
		connection = pymysql.connect(**CONFIG)
		following = exec_query_list(connection, GET_FOLLOWING_QUERY, (user_id))
		return jsonify(following)
	finally:
		connection.close()