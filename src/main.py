#This is primarily for recording my stats in staying consistent with my new schedule.
# Should make a project book sort of thing

#Day logging
import json
import os
from datetime import date
import random

DATA_FILE = "data.json"
current_date = date.today() #prints yyyy-mm-dd
data_dictionary = {
	"name": "null",
	"last_date": str(current_date),
	"streak": 0,
	"start_date" : str(current_date),
	"new": True
}
day = current_date.day

def load_data():
	if os.path.exists(DATA_FILE):
		if os.path.getsize(DATA_FILE) == 0: #This check needs to be done or else on startup, program will try to load an empty JSON file, which throws an error.
			return{}
		with open(DATA_FILE, "r") as file:
			return json.load(file)
	return{}

def save_data(key, value):
	data = load_data()
	data[key] = value
	with open("data.json", "w") as file:
		json.dump(data, file, indent=4)

def check_in(streak):
	if (int(start_date.split("-")[2]) == last_check_in) and user_data.get("new", 0) == True: #Meant to check if ur just starting but wrong.
		streak = 1
		save_data("new", False)
		print(f"Congrats on getting the streak going!")
	elif last_check_in + 1 == int(day): #Consecutive day. Not Tested
		streak += 1
		print(f"Congrats on another successful day!")
	elif last_check_in == day: #Tried checking in twice in one day. Not Tested
		print("You already checked in today!")
	elif last_check_in + 1 != day: #Streak Reset. Not Tested
		#if day == 1 or day == 21 or day == 31:
		#	ending = "st"
		#elif day == 2 or day == 22:
		#	ending = "nd"
		#elif day == 3 or day == 23:
		#	ending = "rd"
		#elif day >= 4 >= 20 or day >= 24 >= 30:
		#	ending = "th"
		streak = 1
		print(f"Your last check in was on the {last_check_in}, your streak just got reset!")
	else:
		print("fsjd")
	print(f"\tCurrent streak length: {streak}\n")
	save_data("streak", streak)
def random_phrase():
	phrases = ["Awesome!", "Nice!", "Congrats!", "Good hustling!", "Nice work!", "You're doing great!"]
	return phrases[random.randrange(len(phrases))]


def main():
	global last_check_in, curr_streak, start_date, user_data
	if os.path.isfile("data.json"):
		user_data = load_data()
		last_check_in = int(user_data.get("last_date", 0).split("-")[2])
		curr_streak = user_data.get("streak", 0)
		start_date = user_data.get("start_date", 0)
		print("\nWelcome to Habit Tracker!")
		while True:
			phrase = random_phrase()
			result = input("\n\tEnter a command (H for help): ").lower()
			if result == "check in":
				check_in(curr_streak)
				user_data = load_data()
			elif result == "test save":
				save_data("last_date", current_date.isoformat())
			elif result == "my data":
				print(user_data)
			elif result == "streak length":
				length = user_data.get("streak", 0)
				definition = user_data.get("streak_definition", 0)
				if length < 1:
					print("Start a new streak first!")
				elif length == 1:

					print(f"For 1 day, you've {definition}. {phrase}")
				else:
					print(f"For {length} days, you've {definition}. {phrase}")
			elif result == "define streak":
				definition = input("Please list what you'd like to keep track of, this will come up as:\n \t'For x days, you've --(list of things here)-- . <- Note the full stop \n So make sure to use the correct tense!\n Type here: ")
				save_data("streak_definition", definition)
				user_data = load_data()
			elif result == "h":
				print("\n LIST OF COMMANDS:\n \t\t -- Check In -- \n \tAllows you to update your streaks for the day! Available once per calendar day.\n \t \t -- Streak Length -- \n \tShows how long your current streak is\n \t \t -- Define Streak -- \n \tAllows you to change what streaks your currently tracking. \n \t Appears like this: For X days, you've (What you're tracking) . <- Note the period\n \t \t-- Exit -- \n \tCloses the program.")
			elif result == "exit":
				break
	else:
		print("Welcome to StreakLogger! If you've just downloaded this, could I make a file next to the app to store your streak info?")
		result = input("Y/N \n--- If you've already set this up, make sure your data.json is placed next to the app file. \n If that's the case, type 'restart.'\n")
		if result == "Y":
			with open("data.json", "w") as file:
				json.dump(data_dictionary, file)
				return main()
		if result == "N":
			print("In order to keep your streaks, we have to save data somewhere! Simply restart if you meant to hit Y.")
		if result == "restart":
			return main()

	
main()

