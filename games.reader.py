import csv

with open("game.csv" , "r" , newline= "" , encoding = "utf-8") as file:
	reader = csv.reader(file)

	for row in reader:
		print(row)