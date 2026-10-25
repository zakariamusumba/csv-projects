import csv

countries = [
	["Australia" , "Canberra"],
	["Brazil" , "Brasilia"],
	["Canada" , "Ottawa"],
	["China" , "Bejing"],
	["Egypt" , "Cairo"],
	["France" , "Paris"],
	["Germany" , "Berlin"],
	["India" , "New Delhi"],
	["Japan" , "Tokyo"],
	["Kenya" , "Nairobi"]

]

with open("countries.csv" , "w" , newline= "" , encoding= "utf-8") as file:
	write = csv.writer(file)
	write.writerows(countries)
	print("country file saved.")