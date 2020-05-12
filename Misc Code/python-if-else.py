#10Task
# Given an integer, , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
# Input Format: A single line containing a positive integer, .
# Constraints: 1 < n < 100
# Source: https://www.hackerrank.com/challenges/py-if-else/problem?h_r=next-challenge&h_v=zen


# n = input("Provide a number between 1 to 100: ")
# n = int(n)

n = int(input().strip())

if (n % 2 == 0):
    #print(f"Number is even {n}")
    if n in range(2, 6):
        #print("Number is between 2 - 5")
        print("Not Weird")
    elif n in range(6, 21):
        #print("Number is between 6 - 20")
        print("Weird")
    else:
        print("Not Weird")
else:
    #print(f"Number is Odd {n}")
    print("Weird")
