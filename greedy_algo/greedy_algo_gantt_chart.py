import sys, datetime, time
from random import randint
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
	def __init__(self, job_length, job_id):
		self.job_length = job_length
		self.job_id = job_id

def main():
	job_queue = []
	total_execution_time = int(sys.argv[1])
	terminate = False
	jobs = get_jobs()
	total = 0

	# create_gantt_chart(jobs, 'greedy-algo-gantt-chart-before')

	while not terminate:
		jobs, job_queue, total_execution_time, terminate = add_min_jobs(jobs, job_queue, total_execution_time)
	
	print 'Number of jobs processed: ' + str(len(job_queue))
	print 'Number of jobs unprocessed: ' + str(len(jobs))
	total = sum([j.job_length for j in job_queue])
	print 'Time to execute jobs: ' + str(total)

	print len(jobs)
	print len(job_queue)
	
	create_gantt_chart(job_queue + jobs, 'greedy-algo-gantt-chart-after')

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

def create_gantt_chart(jobs, name):
	df, i, start_date = [], 1, datetime.date.today()
	for job in jobs:	
		df.append(dict(Task="Job " + str(job.job_id), Start=start_date.isoformat(), Finish=(start_date + timedelta(days=job.job_length)).isoformat()))
		i = i + 1
		start_date = start_date + timedelta(days=job.job_length)
	fig = ff.create_gantt(df)
	layout = {
		'shapes': [
		{
			'type': 'line',
			'x0': 1,
			'y0': 0,
			'x1': 1,
			'y1': 2,
			'line': {
				'color': 'rgb(55, 128, 191)',
				'width': 3,
			},
		}]
	}
	py.plot(fig, filename=name, world_readable=True)

def get_jobs():
	jobs = []
	for i in range(30):
		jobs.append(Job(randint(1, 21), i))
	return jobs

if __name__ == '__main__':
	main()