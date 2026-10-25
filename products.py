import csv

products = [
	["name" , "price", "quantity"],
	["Milk" , "sh 70" , 4],
	["Bread" , "sh 80" , 2],
	["Eggs" , "sh 100" , 1]

]

with open("products.csv" , "w" , newline= "", encoding="utf-8" ) as file:
	write = csv.writer(file)
	write.writerows(products)
	print("product file saved")