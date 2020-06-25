# Source: https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2020/courseware/0de4fecc5a9a4749923133fcf4de181f/e137765987514da7851a59dedeb5ecec/?child=first
# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
# The following variables contain values as described below:
#   balance - the outstanding balance on the credit card
#   annualInterestRate - annual interest rate as a decimal
#   monthlyPaymentRate - minimum monthly payment rate as a decimal
# For each month, calculate statements on the monthly payment and remaining balance. 
# At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy
# A summary of the required math is found below:
#     Monthly interest rate= (Annual interest rate) / 12.0
#     Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#     Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#     Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)


def minPay(balance, annualInterestRate, monthlyPaymentRate):

    monthlyInterestRate = annualInterestRate/12.0
    totBalance = 0

    for i in range(1, 13):
        
        # Calculate monthly payment
        minMonthlyPayment = round((monthlyPaymentRate * balance), 2)
       
        # Total balance is money paid so far + min monthly payment being made this month
        totBalance = round((totBalance + minMonthlyPayment), 2)

        # Calculate remaining balance for the month
        balance = balance - minMonthlyPayment
        
        # new balance due for next month
        balance = round((balance * (1 + monthlyInterestRate)), 2)

        # print("Month: " + str(i))
        # print("Min balance paid this month: " + str(minMonthlyPayment))
        # print("Balance due this month: " + str(balance))
        # print(" Month " + str(i) + " Remaining balance: " + str(balance))

    # print("Total paid: " + str(totBalance))
    # print("Total balance: " + str(balance))
    print("Remaining balance: " + str(balance) )

minPay(42,0.2,0.04)
minPay(484,0.2,0.04)