import csv

songs = [
	["Pop music" , 65],
	["Rock music" , 57],
	["Hip-hop" , 32],
	["Country" , 20],
	["latin" , 10],
	["E-dance music" , 8],
	["Rhyme and Blues" , 5],
	["Classical music" , 2],
	["Jazz" , 2],
	["Religious songs" , 10]

]

with open("songs.csv" , "w" , newline= "" , encoding= "utf-8") as file:
	write = csv.writer(file)
	write.writerows(songs)
	print("songs have been archived.")