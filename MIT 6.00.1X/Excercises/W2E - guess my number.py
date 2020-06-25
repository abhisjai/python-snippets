# Source: https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2020/courseware/0de4fecc5a9a4749923133fcf4de181f/62f08cc899344863a1ab678aee506dec/?activate_block_id=block-v1%3AMITx%2B6.00.1x%2B2T2020%2Btype%40sequential%2Bblock%4062f08cc899344863a1ab678aee506dec
# Create a program that guesses a secret number!
# The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). 
# The computer makes guesses, and you give it input - is its guess too high or too low? 
# 
# Using bisection search, the computer will guess the user's secret number!
# your program should use input to obtain the user's input! Be sure to handle the case when the user's input is not one of h, l, or c.
# When the user enters something invalid, you should print out a message to the user explaining you did not understand their input. Then, you should re-ask the question, and prompt again for input. For example:
# Is your secret number 91?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. y
# Sorry, I did not understand your input.
# Is your secret number 91?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c

print("Please think of a number between 0 and 100!")

low = 0
high = 100
ans = int((low + high) / 2)
print("Is your secret number " + str(ans) + "?")

user_choice = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

while user_choice: 
    if user_choice == "c":
        print("Game over. Your secret number was: " + str(ans))
        break
    elif user_choice == "h":
        high = ans
    elif user_choice == "l":
        low = ans
    else:
        print("Sorry I didn't understand your choice")
    
    ans = int((low + high) / 2)
    print("Is your secret number " + str(ans) + "?")
    user_choice = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
