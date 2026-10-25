import csv

vehicle = [
	["Pickup" , 60000],
	["Jet", 1.5000000],
	["Helicopter" , 300000],
	["Speed Boat" , 45000],
	["Motorbike" , 70000],
	["Bus" , 160000],
	["RV" , 80000],
	["Minibus" , 65000],
	["Sport car" , 1000000],
	["Bicycle" , 36000]

]

with open("vehicle.csv" , "w" , newline = "" , encoding = "utf-8") as file:
	write = csv.writer(file)
	write.writerows(vehicle)
	print("vehicles have been archived.")