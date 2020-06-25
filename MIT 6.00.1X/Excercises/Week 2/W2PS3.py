# Source: https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2020/courseware/
# Write a program that uses these bounds and bisection search to find the smallest monthly payment to the cent such that we can pay off the debt within a year.
# Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). 
# Produce the same return value as you did in Problem 2.

balance = 999999
annualInterestRate = 0.18

monthlyInterestedRate = annualInterestRate / 12
lowerBound = balance /12
upperBound = (balance * (1 + monthlyInterestedRate )**12) / 12

simulation = 0

while(lowerBound < (upperBound-0.001)): # to avoid infinite, define a fixed gap range

    fixedPay = (lowerBound + upperBound)/2
    
    # print("Simulation: " + str(simulation))
    # print("Fixed Pay: " + str(fixedPay), end=' ')
    # print('lowerBound: ' + str(lowerBound), end=' ')
    # print('upperBound: ' + str(upperBound))
    
    debt = balance
    
    for i in range(1,13):
        debt = debt - fixedPay
        debt = debt * (1 + monthlyInterestedRate)
        # print(f"Month: {i} Debt: {debt}")
    
    if debt <= 0: # pay off
        upperBound = fixedPay
    else: # not pay off this time
        lowerBound = fixedPay 
    
    simulation += 1

fixedPay = round(fixedPay, 2)

# print("Total Simulations: " + str(simulation))
print("Lowest Payment: " + str(fixedPay))