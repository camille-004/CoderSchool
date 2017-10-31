import pymysql.cursors, sys, csv, time, names

from node import Node
from neighbor import Neighbor

CONFIG = {'host': '127.0.0.1',
		  'user': 'root',
		  'password': 'root',
		  'db': 'graph_db',
		  'charset': 'utf8mb4',
		  'cursorclass': pymysql.cursors.DictCursor
		 }
FILES_DIRECTORY = 'friend_graphs/'
INSERT_QUERY = '''INSERT INTO nodes (id, val) VALUES (%s, "%s");'''
INSERT_QUERY_NEIGHBOR = 'INSERT INTO neighbors (node_id, neighbor_id) VALUES (%s, %s);'
TRUNCATE_NODES_QUERY = 'TRUNCATE TABLE nodes;'
TRUNCATE_NEIGHBORS_QUERY = 'TRUNCATE TABLE neighbors;'
CONNECTION = None

def exec_query_list(connection, query, params = ()):
	with connection.cursor() as cursor:
		sql = query % params
		cursor.execute(sql)
		result = cursor.fetchall()
		if 'INSERT' in query:
				connection.commit()
		return result


def truncate_tables(connection):
	exec_query_list(connection, TRUNCATE_NODES_QUERY)
	exec_query_list(connection, TRUNCATE_NEIGHBORS_QUERY)

def read_user_relationships(number_of_users):
	nodes = []
	for i in range(0, number_of_users):
		input_file = FILES_DIRECTORY + "user_" + str(i) + ".csv"
		neighbors = []
		with open(input_file, "r") as csvfile:
			reader = csv.reader(csvfile)
			for neighbor_id in reader:
				neighbor = Neighbor(i, neighbor_id[0])
				neighbors.append(neighbor)
		node = Node(i, names.get_full_name(), neighbors)
		nodes.append(node)
	return nodes

def save_relationships(connection, nodes):
	for node in nodes:
		exec_query_list(connection, INSERT_QUERY, (node.id, node.val))
		for neighbor in node.neighbors:
			exec_query_list(connection, INSERT_QUERY_NEIGHBOR, (neighbor.node_id, neighbor.neighbor_id))

def main(args):
	number_of_users = None
	try:
		number_of_users = int(args[1])
	except IndexError as e:
		print "Program usage: 'python main.py <int> -- where int is the number of users in friend_graphs directory'"
		exit()
	connection = None
	try:
		connection = pymysql.connect(**CONFIG)
		truncate_tables(connection)
		nodes = read_user_relationships(number_of_users)
		save_relationships(connection, nodes)
	finally:
		connection.close()


if __name__ == "__main__":
	main(sys.argv)
	