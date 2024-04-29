door=input("Choose a door color and open it, the options are: red, yellow, green, blue, purple. ")
#if red door is chosen by the user:
if door == ("red"):
	food=input("What is your favorite food? ")#prompt
	if food == ("pizza"):
		print("Yay! Me too")
		print("Now go choose another door!")
	else:
		print("NOPE. it must be pizza!")
		print("on to the next door!")



#if yellow door is chosen by the user:
if door == ("yellow"):
	animal=input("Who is your favorite animal? ")#prompt
	if animal == ("tiger"):
		print("I love tigers!")
		print("on to the next door!")
	elif animal == ("shark"):
		print("Sharks are cool.")
		print("on to the next door!")
	else:
		print("Nope, I am scared of those.")
		print("on to the next door!")



# if the green door is chosen by the user:
if door == ("green"):
	fav_SH=input("Who is your favorite superhero? ")#prompt
	if fav_SH == ("spiderman") and ("hulk"):
		print("NO WAY! Me too")
		print("on to the next door!")
	else:
		print("oh… okay ):")
		print("on to the next door!")


#if the blue door is chosen by the user:
if door == ("blue"):
	planet=input("What is your favorite planet? ")#prompt
	if planet == ("mars"):
		print("Same dude!")
		print("on to the next door!")
	else:
		print("Sorry it has to be Mars.")
		print("on to the next door!")


#if the purple door is chosen
if door == ("purple"):
	fav_class=input("What is your favorite class? ")#prompt
	if fav_class == ("computer programming"):
		print("I like that class too!")
		print("This is the final door, good job!")
	else:
		print("Cool, mine is computer programming with Mrs. Nelson! ")
		print("This is the final door, good job!")
