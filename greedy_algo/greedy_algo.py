import sys

class Job:
	def __init__(self, job_length):
		self.job_length = job_length


def main():
	job_queue = []
	total_execution_time = int(sys.argv[1])
	terminate = False
	jobs = get_jobs()
	total = 0

	while not terminate:
		jobs, job_queue, total_execution_time, terminate = add_min_jobs(jobs, job_queue, total_execution_time)
	
	print 'Number of jobs processed: ' + str(len(job_queue))
	print 'Number of jobs unprocessed: ' + str(len(jobs))
	total = sum([j.job_length for j in job_queue])
	print 'Time to execute jobs: ' + str(total)

def add_min_jobs(jobs, job_queue, total_execution_time):
	min_job = jobs[0]
	for job in jobs:
		if job.job_length < min_job.job_length:
			min_job = job
	if min_job.job_length <= total_execution_time:
		jobs.remove(min_job)
		job_queue.append(min_job)
		total_execution_time -= min_job.job_length
		if total_execution_time == 0 or len(jobs) == 0:
			return jobs, job_queue, total_execution_time, True
		else:
			return jobs, job_queue, total_execution_time, False
	else:
		return jobs, job_queue, total_execution_time, True
	
def print_job_list(jobs):
	print '##############################'
	for job in jobs:
		print job.job_length
	print '##############################'



def get_jobs():
	# 193 is the max
	jobs = []
	jobs.append(Job(18))
	jobs.append(Job(13))
	jobs.append(Job(8))
	jobs.append(Job(3))
	jobs.append(Job(8))
	jobs.append(Job(17))
	jobs.append(Job(3))
	jobs.append(Job(11))
	jobs.append(Job(18))
	jobs.append(Job(8))
	jobs.append(Job(8))
	jobs.append(Job(3))
	jobs.append(Job(16))
	jobs.append(Job(5))
	jobs.append(Job(5))
	jobs.append(Job(13))
	jobs.append(Job(8))
	jobs.append(Job(9))
	jobs.append(Job(1))
	jobs.append(Job(18))
	return jobs	




if __name__ == '__main__':
	main()