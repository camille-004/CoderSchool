import csv, sys, math
from random import randint

def main(args):
	try :
		number_of_users = int(args[1])
	except ValueError as e:
		print e
	for i in range(number_of_users):
		file_name = 'user_' + str(i) + '.csv'
		with open(file_name, 'w') as csvfile:
			writer = csv.writer(csvfile)
			friends = []
			for j in range(randint(0, number_of_users - 1)):
				friends.append(randint(0, number_of_users - 1))
			friends = set(friends)
			for friend in friends:
				writer.writerow([friend])


if __name__ == '__main__':
	main(sys.argv)
