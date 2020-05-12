# Task
# Generate a list of unique random numbers from a range and count provided by the user

import random

def random_number (count, lower_number, upper_number):
    random_list = []

    n = 0
    while(n <= count):
        new_number = random.randint(lower_number,upper_number)

        if new_number not in random_list:
            random_list.append(new_number)
            n = n+1

    random_list.sort()
    return random_list

# Ask for user input and validate data
count = input("Provide number of random numbers you need: ")
if count:
    try:
        count = int(count)
        if count < 0:
            print("This is not a valid number. Default value of 15 was selected.")
            count = 15
    except ValueError:
        print("This is not a valid number. Default value of 15 was selected.")
        count = 15
else:
    print("This is not a valid number. Default value of 15 was selected.")
    count = 15

smallest_number = input("Provide smallest number in the list: ")
if smallest_number:
    try:
        smallest_number = int(smallest_number)
    except ValueError:
        print("This is not a valid number. Default value of 15 was selected.")
        smallest_number = 15
else:
    smallest_number = 15

highest_number = input("Provide highest number in the list: ")
if highest_number:
    try:
        highest_number = int(highest_number)
    except ValueError:
        print("This is not a valid number. Default value of 200 was selected.")
        highest_number = 200
else:
    highest_number = 200

if smallest_number+count >= highest_number:
    highest_number = smallest_number + 200
    print("Highest number should be greater than smallest number in the range. Default value of {} was selected.".format(highest_number))

print(random_number(count, smallest_number, highest_number))