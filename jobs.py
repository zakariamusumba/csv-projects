import csv

jobs = [
	["Support staff" , 11553],
	["Security guard" , 20000],
	["Cook" , 25000],
	["Driver" , 40724],
	["Teacher" , 100000],
	["Accountant" , 120000],
	["Software Engineer" , 1220000],
	["Bank Manager" , 3300000],
	["Surgeon" , 7300000],
	["CEO" , 15000000]

]

with open("jobs.csv" , "w" , newline = "" , encoding = "utf-8") as file:
	write = csv.writer(file)
	write.writerows(jobs)
	print("jobs has been archived")