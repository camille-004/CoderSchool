import plotly.plotly as py
import plotly.figure_factory as ff

df = [dict(Task="Job A", Start='2018-03-01' str(), Finish='2018-03-02'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30'),
      dict(Task="Job D", Start='2009-05-30', Finish='2009-06-30')]

fig = ff.create_gantt(df)
py.plot(fig, filename='gantt-simple-gantt-chart', world_readable=True)
