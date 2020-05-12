# Rock, Paper, Scissors Game
# Make a rock-paper-scissors game where it is the player vs the computer.
# The computer’s answer will be randomly generated, while the program will ask the user for their input. 
# This project will better your understanding of while loops and if statements.
# Source: https://www.codementor.io/@ilyaas97/6-python-projects-for-beginners-yn3va03fs

from random import randint

random_number = randint(0,2)

system_array = ["Rock", "Paper", "Scissors", ]
system_choice = system_array[random_number]

# Time to know what machine thought
response = "System Choose: {}. ".format(system_choice)


user_choice = input("Rock (R), Paper (P), Scissors (S), Choose! ")

# List of possible user response synonyms 
rock_syn = ["Rock", "r", "R", "rock"]
paper_syn = ["Paper", "p", "P", "paper"]
scissors_syn = ["Scissors", "S", "s", "scissors"]

mega_list = rock_syn + paper_syn + scissors_syn

# Validate user response
if user_choice not in mega_list:
    print("Invalid response.")
# Check for draw conditions
elif user_choice in rock_syn and system_choice == "Rock":
    response = response + "Game Draw"
elif user_choice in paper_syn and system_choice == "Paper":
    response = response + "Game Draw"
elif user_choice in scissors_syn and system_choice == "Scissors":
    response = response + "Game Draw"
# Check for winning conditions
elif user_choice in rock_syn and system_choice == "Scissors":
    response = response + "Rock crushes Scissors. You Win"
elif user_choice in paper_syn and system_choice == "Rock":
    response = response + "Paper covers Rock. You Win"
elif user_choice in scissors_syn and system_choice == "Paper":
    response = response + "Scissor cuts Paper. You Win"
# You loose for any other combination
else:
    response = response + "Sorry you loose"

# Announce results
print(response)