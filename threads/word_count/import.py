from ggplot import *
import csv

with open("output.csv", "r") as csv_file:
	reader = csv.reader(csv_file)