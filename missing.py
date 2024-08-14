import random
winner=random.randint(1,100)
guess=1
number=int(input("Enter the number in 1 to 100 : "))
gameover=False
while not gameover:
	if number==winner:
		print("you are the winner \U0001F604")
		print("Number of times you guess",guess)
		gameover=True
	elif number>winner:
		print("High number")
		guess+=1
		number=int(input("Enter again : "))
	else:
		print("low number")
		guess+=1
		number=int(input("Enter again : "))