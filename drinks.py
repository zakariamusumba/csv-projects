import csv

drinks = [
	["water" , 60],
	["Tea" , 350],
	["Coffee" , 450],
	["milk" , 120],
	["Oat milk" , 450],
	["Fruit juices" , 300],
	["Carbonated soft drinks" , 100],
	["Smoothies" , 700],
	["Alcoholic bevarages" , 350]

]

with open("drinks.csv" , "w" , newline= "" , encoding= "utf-8") as file:
	write = csv.writer(file)
	write.writerows(drinks)
	print("drinks have been saved.")