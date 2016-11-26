movie_ticket = {
	"Pk": [18,6],
	"Jajba" : [14,8],
	"Raj" : [18,9],
	"Dabang": [12,4],
	"Aan" : [10,3]
}

while True:
	choice = input("Please enter the movie name which you want to watch. ").strip().title()
	if choice in movie_ticket:
		age = int(input("Please enter you age ? ").strip())
		if age >= movie_ticket[choice][0]:
			num_tickets = movie_ticket[choice][1]
			if num_tickets > 0:
				print ("Enjoy the movie!!")
				movie_ticket[choice][1]= movie_ticket[choice][1] - 1
			else:
				print ("Sorry we are sold out.")
		else:
			print("Opps!! you are too young.")
	else:
		print("We dont have any show of this movie.")
			