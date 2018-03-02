import pymysql.cursors, sys
from node import Node
from neighbor import Neighbor
'''
This program reads in an integer representing a user_id from the command line.
It then reads all of the info of that user and fetches all "friends" 
from a MySQL database table and prints it out to the console.

This exercise is to practice how to store a graph of nodes and edges into 
a database that can be fetched later.
'''

CONFIG = {'host': '127.0.0.1',
		  'user': 'root',
		  'password': 'root',
		  'db': 'graph_db',
		  'charset': 'utf8mb4',
		  'cursorclass': pymysql.cursors.DictCursor
		 }

GET_NODE_QUERY = "SELECT * FROM nodes WHERE id = %s"
GET_NEIGHBORS_FROM_NODE = "SELECT id, val FROM neighbors JOIN nodes ON neighbors.neighbor_id = nodes.id WHERE node_id = %s;"

def main(args):
	# Step 1: Read a node_id from the command line
	node_id = None
	try:
		node_id = int(args[1])
	except ValueError as e:
		print "Expecting Integer Input: " + str(e)
		exit()
	node_graph = get_node_graph(node_id)
	print node_graph.id, node_graph.val, node_graph.neighbors

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
				return result
	finally:
		connection.close()

def exec_query_list(query, params):
	connection = pymysql.connect(**CONFIG)
	try:
		with connection.cursor() as cursor:
			sql = query % params
			cursor.execute(sql)
			result = cursor.fetchall()
			return result
	finally:
		connection.close()

def get_node_graph(node_id):
	# Gets a graph with the node with ID as entry point to the graph
	node = exec_query(GET_NODE_QUERY, (node_id))
	neighbor = exec_query_list(GET_NEIGHBORS_FROM_NODE, (node_id))

	root_node = Node(node['id'], node['val'])
	neighbors = []
	for n in neighbor:
		new_node = Node(n['id'], n['val'])
		neighbors.append(new_node)
	root_node.set_neighbors(neighbors)
	return root_node


if __name__ == "__main__":
	main(sys.argv)
