import csv
try:
	with open("movies.csv","r") as file:
		read = csv.reader(file)
		r = list(read)
		print(f"last added movie : {r[-1]}")
except FileNotFoundError:
	with open("movies.csv","w",newline='')as file:
		write = csv.writer(file)
		write.writerow(["Title","Genre","Rating"])
while True:
	ask = input("1. Add New Movie\n2. View All Movies\n3. Search Movies by Genre\n4. Show Top Rated Movie\n5. Exit\n enter: ")
	if ask =="1":
		a = input("what do you wanna add format(Title,Genre,Rating): \n")
		with open('movies.csv',"a",newline='')as file:
			ad = csv.writer(file)
			ad.writerow(a.split(","))
	elif ask =="2":
		with open("movies.csv","r")as file:
			read = csv.reader(file)
			for row in read:
				print(row)
	elif ask =="3":
		a = input("enter search: ").capitalize()
		found = False
		with open ("movies.csv","r") as file:
			read = csv.reader(file)
			for r in read:
				if a in r:
					print(r)
					found = True
		if not found:
			print("there is ntg else")
	elif ask =="4":
		top_movie = None
		top_rating = 0
		with open("movies.csv","r") as file:
			r = csv.reader(file)
			next(r)
			for row in r:
				rating = float(row[-1])
				if rating > top_rating:
					top_rating = rating
					top_movie = row
		if top_rating:
			print(f"top rated movie: {top_movie[0]} ({top_movie[1]}) - {top_movie[2]}/10" )
	elif ask =="5":
		print("thx")
		break
	else:
		print("enter from 1-5")