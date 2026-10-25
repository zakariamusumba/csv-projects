import csv

students = [
		["name", "students", "marks"],
		["Brian", "Python", 78],
		["Mary", "Data Science", 85],
		["Amina", "Cybersecurity", 9],
		]

with open("students.csv", "w", newline= "", encoding="utf-8") as file:
			 writer = csv.writer(file)
			 writer.writerows(students)
			 print("csv file saved.")