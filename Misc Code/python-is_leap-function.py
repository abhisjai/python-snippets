# You are given the year, and you have to write a function to check if the year is leap or not.
# Note that you have to complete the function and remaining code is given as template.
# Source: https://www.hackerrank.com/challenges/write-a-function/problem?h_r=next-challenge&h_v=zen

# Test Case: the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years

def is_leap(year):
    leap = False
    
    # Write your logic here
    # In the Gregorian calendar three criteria must be taken into account to identify leap years:
    # The year can be evenly divided by 4, is a leap year, unless:
    # The year can be evenly divided by 100, it is NOT a leap year, unless:
    # The year is also evenly divisible by 400. Then it is a leap year.

    if (year % 4 ==0) and ((year % 100 != 0) or (year % 400 == 0)):
        #print("Leap year")
        leap = True
    else:
        #print("Not a leap year")
        leap = False

    return leap

year = int(input())
# Should return True or False
print(is_leap(year))