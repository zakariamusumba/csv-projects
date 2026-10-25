import csv

menu = [
	["Chicken Biryani" , 950],
	["Grilled chicken" , 850],
	["Beef burger" , 750],
	["wet fry goat meat" , 1200],
	["House breakfast platter" , 1200],
	["Fish fillet strips" , 1500],
	["Loaded fries" , 550],
	["Club sandwich" , 850],
	["Milkshakes" , 600],
	["Shared meat platters" , 2500]

]

with open("menu.csv" , "w" , newline= "" , encoding = "utf-8") as file:
	write = csv.writer(file)
	write.writerows(menu)
	print("menu has been archived.")