import csv

shop = [
	["name","price","quantity"],
	["microphone",4500,1],
	["tv", 60000 , 1],
	["smartphone", 70000 , 1],
	["headphone", 2400 , 1],
	["laptop", 40000 , 1],
	["earphones", 1500 , 1],
	["speaker", 3500 ,1],
	["computer", 114000 , 1],
	["ps controllers" , 1200 , 2],
	["xbox controller", 2500 , 4]

]

with open("shop.csv", "w" , newline= "", encoding= "utf-8") as file:
	write= csv.writer(file)
	write.writerows(shop)
	print("shop items saved.")