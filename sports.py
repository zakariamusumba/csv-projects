import csv

sports = [
	["name" , "type" , "fans"],
	["football" , "Team" , 3.5],
	["cricket" , "Team" , 2.5],
	["Field Hockey" , " Team" , 2],
	["Tennis" , "Doubles" , 1],
	["Volleyball" , "Teams" , 900],
	["Table tennis" , "Doubles" , 850],
	["Basket ball" , "Team" , 800],
	["Baseball" , "Team" , 500],
	["Rugby" , "Team" , 475],
	["Golf" , "Solo" , 450]

]

with open("sports.csv" , "w" , newline= "" , encoding= "utf-8") as file:
	write = csv.writer(file)
	write.writerows(games)
	print("games have been listed.")