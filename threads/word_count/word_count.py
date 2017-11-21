import sys, time, threading, csv
RESULTS = []

def count_words(file, threads):
	lines = []
	slices = []
	# Read in lines of text file
	with open(file, "r") as text_file:
		lines = [line for line in text_file]

	# Divide lines into even slices
	length = len(lines) 
	base = length / int(threads)
	minimum = 0
	maximum = base
	while maximum <= length:
		slices.append(lines[minimum:maximum])
		minimum += base
		maximum += base
	slices.append(lines[minimum:])
	
	# Create n number of threads (threads)
	thread_pool = []
	for i in range(int(threads)):
		thread_pool.append(threading.Thread(target=thread_task, args=(slices[i],)))

	start_time = time.time()

	# Give each thread a slice to count
	for thread in thread_pool:
		thread.start()

	for thread in thread_pool:
		thread.join()

	end_time = time.time()
	with open("output.csv", "a") as text_file:
		writer = csv.writer(text_file)
		writer.writerow([int(threads),end_time - start_time])

def thread_task(lines):
	total_characters = 0
	for line in lines:
		for word in lines:
			for character in word:
				total_characters += 1
	RESULTS.append(total_characters)

if __name__ == "__main__":
	count_words(sys.argv[1], sys.argv[2])