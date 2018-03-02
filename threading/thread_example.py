from threading import Thread

def count1():
	for i in range(1000):
		print i

def count2():
	for i in range(1001, 2000):
		print i

def main():
	t1 = Thread(target=count1)
	t2 = Thread(target=count2)
	t1.start()
	t2.start()

if __name__ == "__main__":
	main()
