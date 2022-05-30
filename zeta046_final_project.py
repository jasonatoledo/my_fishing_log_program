# -*- coding: utf-8 -*-
"""
Jason Toledo
Class: CS 521 - Fall 1
Date: 10/04/2021
Homework Problem Final Project Code
Description of Problem (just a 1-2 line summary!):
    This is a fishing log program that provides the user with the ability to
choose their fishing habitat and describe how they think each fish tastes on
a given day. The input file will read out the previous fishing log and the
output file will create a new log for the current day.
    
"""
import sys
from datetime import date
from fish import Fish

# import the user's previous fishing log 2021-10-20_fishing_log.txt 
try:
    file = input("Please enter the file name of your previous fishing log: ")\
        .lower()
    my_file = open(file,"r+")
except FileNotFoundError as e:
    print(e, "Sorry, this file does not exist, please start over!")
    sys.exit()
else:
    print("\nThank you! Here is your last fishing log:\n")

# read the file and print out the contents from previous fishing log
data = my_file.read()
for line in data:
    print(line,end='')

# ask user where they would like to fish today and confirm their choice
locations = ["Bay", "Ocean", "Lake"]

print("\n\nPlease choose the location you are fishing at today:\n")
for loc in locations:
    print(loc)

while True:
    loc_preference = input("Where do you want to fish today? ").lower()
    if loc_preference.title() not in locations:
        print("\nPlease choose from one of the listed locations")
        continue
    else:
        break

print("\nOkay, you are fishing at the", loc_preference.title(), "today.")

# create game object based on the user input value
user_game = loc_preference.lower()+"_game"

# create set of available game options specific to their location choice
ocean_game = {"perch", "salmon", "bass"}
bay_game = {"shark", "ray", "sturgeon"}
lake_game = {"bass","trout","catfish"}

# assign the type of game available based on user input
if user_game == "ocean_game":
    game = ocean_game
elif user_game == "bay_game":
    game = bay_game
elif user_game == "lake_game":
    game = lake_game

# accept user input for fishing goal today up to 30 fish
print("\n\n------- Let's set our Goal for today! --------")

while True:
    goal = input("How many fish do you want to catch today? Remember, the max\
 allowed per species is 10 per day! Please enter a positive integer only: ")
    if ',' in goal:
        print("\nPlease try again without entering commas.")
        continue
    elif "!" in goal or "\"" in goal or "#" in goal or "$" in\
        goal or "%" in goal or "&" in goal or "\\" in goal\
        or "?" in goal or "'" in goal or "(" in goal or ")" in\
        goal or "*" in goal or "+" in goal or "/" in goal or\
        ":" in goal or ";" in goal or "<" in goal or ">" in\
        goal or "=" in goal or "@" in goal or "[" in goal or\
        "]" in goal or "^" in goal or "_" in goal or "`" in\
        goal or "{" in goal or "}" in goal or "|" in goal or\
        "~" in goal or "\\" in goal:
        print("\nSorry, no punctation characters allowed, please try again.")
    elif goal.isalpha() or ' ' in goal:
        print("\n",goal,"is not a valid number. Please try again")
        continue
    elif goal == '':
        print("\nPlease enter a value: ")
        continue
    elif int(goal) <= 0:
        print("\nThat's not a positive integer, please try again!")
        continue
    elif int(goal) > 30:
        print("\nSorry, that goal seems unrealistic, please try again!")
        continue
    else:
        break

# Rate the user's goal and tell them we are going to start fishing
if 1 <= int(goal) <= 5:
    print("\nThat's an easy goal, you can do it!")
elif 6 <= int(goal) <= 10:
    print("\nThat's a good goal, let's get started!")
elif 11 <= int(goal) <= 20:
    print("\nThat's an ambitious goal, let's get started!")
else:
    print("\nWow! That's a huge goal, let's get started!")
    
print("\n\n","-"*10,"Time to go fishing!","-"*10)

# create list and dictionary objects to store fishing records
fishing_list= []
new_fish_list = []

print("Since you are at the", loc_preference.title()+",","the type of fish\
 you can catch are:")
print(*game, sep=", ", end="")
    
# while loop to capture user's catches from game list
while True:
    fish_caught = input("\nDid you catch a/another fish part of the current\
 game list? (y/n): ").lower()
    if fish_caught == "yes" or fish_caught == 'y':
        catch = input("What type of fish did you catch? ").lower()
        if catch in game:
            fishing_list.append(catch)
        else:
            print("that fish isn't part of the current game list - please\
 take note of the fish you've caught that aren't part of your catches today\
 and enter them in the next section.")
        continue
    elif fish_caught == "no" or fish_caught == 'n':
        break
    elif fish_caught != "yes" or fish_caught != "no":
        print("\nPlease enter yes or no only: ")
        continue

# while loop to capture if a user caught fish not part of the game list
while True:
    new_caught = input("Did you catch a/another species of fish not part of\
 the game list? (y/n): ").lower()
    if new_caught == "yes" or new_caught == "y":
        new_fish = input("\nPlease enter a/another species of fish that you\
 caught that weren't part of the current game list: ").lower()
        new_fish_list.append(new_fish)
    elif new_caught == "no" or new_caught == "n":
        print("\nHope you caught as many as you wanted today!")
        break
    elif new_caught != "no" or new_caught != "n":
        print("That isn't a valid response, please try again")
        continue             

# update game set values depending on the fishing location and new fish added
if new_fish_list != []:
    game.update(new_fish_list)

# create total_fish_list object from the two lists and sort it
total_fish_list = fishing_list + new_fish_list
total_fish_list.sort()

# define function to turn the fishing log into a dictionary object
def create_fishing_log(total_fish_list):
    """this function takes a list as the input object and returns a
    dictionary with fish as the key values and the quantities of each fish
    caught as the values."""
    fishing_log = {}
    for fish in total_fish_list:
        if fish not in fishing_log.keys():
            fishing_log[fish] = 1
        else:
            fishing_log[fish] += 1
    return fishing_log

# call create fishing log user defined function using todays_fishing_log
todays_fishing_log = create_fishing_log(total_fish_list)

# print updated fishing log in tuple format
fish_list_tuples = todays_fishing_log.items()
fish_list_tuples = list(fish_list_tuples)

# let user know how they did, total caught, and if they met their goal
print("\nHere are your catches for today:")
for fish in fish_list_tuples:
    print(fish)
    
fish_count = 0
for k, v in todays_fishing_log.items():
    fish_count += v
print("Total fish caught today: ",fish_count)

# create count and logic to tell the user how they did today vs their goal
count = sum(todays_fishing_log.values())
if count == 0:
    print("\nDon't feel bad about not catching anything, it happens to the\
 best of us! Since you caught no fish, you won't have a log today!")
    sys.exit()
elif count < int(goal)*0.50:   
    print("\nAw shucks, you didn't meet your goal today, better luck next\
 time!")
elif count <= int(goal)*0.80:
    print("\nYou were really close! You'll get it the next time you go\
 fishing!")
else:
    print("\nGreat job, you killed it today!")

# convert todays fishing log to set to get unique values then back to list
todays_fishing_set = set(todays_fishing_log)
unique_list = list(todays_fishing_set)
unique_list.sort()

# create taste list to use when invoking class call for final log output
taste_list = []

# iterate through the unique fish list and append user taste choices to dict
print("\nPlease enter your opinion on how each fish tastes for your log.")

# create count object and empty dictionary
taste_count = len(unique_list)
taste_dict = {}

while taste_count > 0:
    for fish in unique_list:
        taste = input("How does " + fish.title() + " taste to you?\n\nChoices\
:\nokay\nbad\ngood\nyummy\ndelicious\nweird\nunknown\n\n").lower()
        if taste in Fish.TASTES:
            taste_dict[fish] = taste
            taste_count -= 1
            unique_list.remove(fish)
        elif taste not in Fish.TASTES:
           print("\nSorry, that is not one of the taste options. You will\
 need to enter one of the available choices, sorry.")
           continue

# create dictionary object and use class call to create full descriptions
fish_dict = {}
for i in range(len(total_fish_list)):
    species = total_fish_list[i]
    taste = taste_dict[species]
    fish_dict[species] = fish_dict.get(species, Fish(species = species,\
                         habitat = loc_preference.lower(),taste = taste))
                                       
# display user's dictionary object in order for them to check the contents
print("\nThese are the type of fish you caught today with their habitat and\
 taste values:\n")
for k,v in fish_dict.items():
    print(k,":",v)

# ask user if all habitats look correct for their entries and if not, fix them
while True:
    user_check = input("Do the habitat values match what you want to log?\
 (y/n): ").lower()
    if user_check == "no" or user_check == "n":
        fish_to_fix = input("\nPlease enter the species you want to update\
 the habitat for: ").lower()
        if fish_to_fix not in fish_dict.keys():
            print("Please enter a fish from your log, try again.\n")
            continue
        else:
            print("Available habitats: ")
            print(*Fish.HABITATS,sep=", ",end="")
            new_habitat = input("\nPlease enter a new habitat to update for\
 your fish: ").lower()
            #use private method update to update value and store for log
            fish_dict[fish_to_fix]._Fish__set_habitat(new_habitat)
            print("\nHere are your updated values: ")
            for k,v in fish_dict.items():
                print(k,":",v)
            continue
    elif user_check == "yes" or user_check == "y":
        break
    elif user_check != "yes" or user_check != "y":
        print("That isn't a valid response, please try again")
        continue
    
# ask user if all tastes look correct for their entries and if not, fix them
while True:
    user_taste = input("Do the taste values match what you want to log?\
 (y/n): ").lower()
    if user_taste == "no" or user_taste == "n":
        fish_to_fix = input("\nPlease enter the species you want to update\
 the taste value for: ").lower()
        if fish_to_fix not in fish_dict.keys():
            print("\nPlease enter a fish from your log, try again.\n")
            continue
        else:
            print("\nAvailable taste values: ")
            print(*Fish.TASTES,sep=", ",end="")
            new_taste = input("\nPlease enter a new taste to update for\
 your fish: ").lower()
            # use public method to update value and store for log
            fish_dict[fish_to_fix].update_taste(new_taste)
            print("\nHere are your updated values: ")
            for k,v in fish_dict.items():
                print(k,":",v)
            continue
    elif user_taste == "yes" or user_taste == "y":
        break
    elif user_taste != "yes" or user_taste != "y":
        print("That isn't a valid response, please try again")
        continue   
        
# create output objects to use in output file        
fish_output = "\n".join(str(v) for k, v in fish_dict.items())
str_fish_count = str(fish_count)

# create a fishing log object based on today's date
today = date.today()
today_output = str(today) + "_fishing_log.txt"

# use the fishing log object as the output file name
output_file = open(today_output,"w")

# write file output contents for output file and succesful message
header = "Fishing log for " + str(today) +": \n"
output_file.write(header)
output_file.write("-"*27)
output_file.write("\n\n")
output_file.write(str(fish_list_tuples))
output_file.write("\n\nTotal number of fish you caught: ")
output_file.write(str_fish_count)
output_file.write("\n\n")
output_file.write("-"*10)
output_file.write("Updated Fish and class attributes for the habitat on this\
 day")
output_file.write("-"*10)
output_file.write("\n\n")
output_file.write(fish_output)
print("\n\nThank you! Your fishing log for",today,"has been created!")

# close files at the end of the program
my_file.close()
output_file.close()