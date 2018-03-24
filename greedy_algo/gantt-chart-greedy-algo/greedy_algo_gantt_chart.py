import sys	
import datetime
from datetime import timedelta

import plotly.plotly as py
import plotly.figure_factory as ff

'''
########################################################################
Greedy interval scheduling program.
########################################################################
This program will find the most optimal way to complete as many jobs as possible in a limited amount of time.
This is accomplished by starting with the job that take the smallest amount of time to complete,
and eventually processing them until either no more can be processed, or the alotted time has already been
exceded.
'''
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

	create_gantt_chart(job_queue)

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

def create_gantt_chart(jobs):
	df, i, start_date = [], 1, datetime.date.today()
	for job in jobs:	
		df.append(dict(Task="Job " + str(i), Start=start_date.isoformat(), Finish=(start_date + timedelta(days=job.job_length)).isoformat()))
		i = i + 1
		start_date = start_date + timedelta(days=job.job_length)
	fig = ff.create_gantt(df)
	py.plot(fig, filename='greedy-algo-gantt-chart', world_readable=True)

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