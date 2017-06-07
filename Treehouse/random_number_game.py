import random

level = 100
random_number: int = None
guessed_number: int = None

def show_game_help():
	print("Welcome to the random number game!")
	print("Aim of the game: guess the number I'm thinking of")
	print("The number will be between 0 and whatever level you've chosen...")
	print("""
GIVE UP - this will end the game and reveal the number I'm thinking of
NEW GAME - this will start a new game with a new number
HELP - shows this really helpful help message
""")


def get_new_level():
	try:
		new_level = int(input("Choose your level:\n> "))
	except:
		print("That's not a number! Try again...")
		get_new_level()
	else:
		return new_level


def start_new_game():
	print("Starting new game...\n")
	global random_number
	random_number = random.randint(0, get_new_level())
	print("Now start guessing...")
	ask_for_number()


def ask_for_number():
	guess = input("> ").lower()
	if guess == "give up":
		end_game(False)
	elif guess == "new game":
		start_new_game()
	elif guess == "help":
		show_game_help()
		ask_for_number()
	else:
		try:
			guessed_number = int(guess)
		except:
			print("That's not a number! Try again...")
			ask_for_number()
		else:
			check_number(guessed_number)


def end_game(won):
	if won:
		print("YES! That's my number! You won!")
	else:
		print("Unlucky! The number was {}".format(random_number))
	ask_to_play_again()


def ask_to_play_again():
	play_again = input("Want to play again? Y/N \n> ")
	if play_again.lower() == "y":
		start_new_game()		
	else:
		print("Thanks for playing!")


def check_number(number: int):
	if number == random_number:
		end_game(True)
	elif number > random_number:
		print("Almost, try a little lower...")
		ask_for_number()
	elif number < random_number:
		print("Almost, try a little higher...")
		ask_for_number()


def main():
	show_game_help()
	start_new_game()



main()
