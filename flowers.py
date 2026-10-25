import csv

flowers = [
	["Sunflower" , "mild"],
	["Lilly of the valley" , "harmful"],
	["Rose" , "mild"],
	["Petunia" , "mild"],
	["Pansy" , "mild"],
	["Foxglove" , "harmful"],
	["wistera" , "harmful"],
	["Marigold" , "mild"],
	["Oleander" , "harmful"],
	["Hydrangea" , "harmful"]

]

with open("flowers.csv" , "w" , newline = "" , encoding = "utf-8") as file:
	write = csv.writer(file)
	write.writerows(flowers)
	print("Flowers have been archived")