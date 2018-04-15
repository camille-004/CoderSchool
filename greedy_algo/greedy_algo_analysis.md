# Greedy Algorithms

## What is a "greedy" algorithm?
A greedy algorithm goes about solving a problem by breaking it down into different simple problems that can be solved independently.  When all of these smaller problems are solved, the solutions would combine and form one that can be "globally optimal."

## Examples of a greedy algorithm
### Locally optimal solution leads to a globally optimal solution
Take for example a set of dollar bills, each of a different value, from $1 to $100 ($1, $5, $10, $20, $50, $100).  If allowed to take n bills, **one at a time**, how would you choose as to maximize the amount of money you would get?  

If given the option to choose only one dollar bill out of the set, this algorithm would choose the one of the most "optimal" value, $100.  

Now, you may choose a second dollar bill.  In order to obtain the most amount of money possible, which one would you choose?  

If you chose $50, you would end up with $150, which, if only given the chance to choose two dollar bills, would be the most optimal solution to the global problem:  How do I acquire the most amount of money possible?  By deciding to pick up the dollar bill of the largest value ($100), and then deciding on the one of the second-to-largest value ($50), you have followed the logical process any greedy algorithm would take. This process is breaking the problem up into smaller bits to eventually reach a global optimum.

```python
max([1, 5, 10, 20, 50, 100]) # returns 100
max([1, 5, 10, 20, 50]) # returns 50
max([1, 5, 10, 20]) # returns 20
...
```

### Greedy algorithms don't always lead to a globally optimal solution
Now, consider a network of roads that you would take from your house to reach a destination.  The goal - the global problem - is to reach your destination while travelling the smallest distance possible.  

Suppose there is one street on the route that is 100 yards long, and another 200 yards long.  Which street would you choose to take as to minimize the distance you travel?

Choosing the 100-yard street solves a local problem - you have solved one part of the global problem in order to get closer to reaching the global solution.  

However, after taking the 100-yard street, you must take a road that is 500 yards long.  On the contrary, the street that comes after the 200-yard one is only 250 yards long.  That set of streets yields a 450-yard route, as opposed to the 600-yard route you must take.  You can no longer reach your globally optimal solution because you are not reaching your destination by travelling the smallest distance possible.

Even though you solved one part of the problem - taking the shortest possible road in the beginning - it did not lead to the globally optimal solution.


## Real world problem
### Interval scheduling 
Finally, consider a set of jobs in a company.  The global problem is that there is only a limited amount of time to complete the greatest number of jobs possible.

A reasonable approach would likely be to complete the jobs that take the least time first so that a larger number of jobs would fit in the allocated time slot.  We would begin with the job that takes the shortest amount of time and work towards the job with the largest time until time runs out.  This process is emulated by the following Python function: 
```python
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
```
This function iterates through a list of ```Job``` objects, ```jobs```, with time length and ID properties (Python instance variables ```job_length``` and ```job_id```).  It first uses the zeroth element of the list as the shortest-time job, ```min_job```, as a basis for comparison - if the next element has a smaller ```job_length``` value than does the zeroth element, it replaces it as the new ```min_job```.  The element is then removed from ```jobs``` and added to a ```job_queue```.  This process repeats until either the time is up or all respective Jobs have been analyzed (contingent on how much time is given).  

By the end of the algorithm, the ```job_queue``` contains all analyzed ```Job```s, ordered by how short their times are.  The code produces a Gantt chart that illustrates the start and finish dates of each ```Job``` from the queue based on their times.  The following shows an example:
![Greedy Algo Scheduling](gantt-chart-greedy-algo/greedy-algo-gantt-chart.png)
