balance = 501
annualInterestRate = 0.25

monthlyInterest = annualInterestRate / 12
simulation = 0

fixedPay = int(balance / 12)
debt = balance

finalFixedPay = 0

while debt > 0:
    debt = balance

    # if debt < 10:
    #     finalFixedPay =  10
    #     break

    simulation += 1

    # print("Simulation: " + str(simulation), end=" ")
    # print("Fixed Payment: " + str(fixedPay))

    for i in range(1, 13):
        debt = debt - fixedPay
        # print("Month: " + str(i), end=" ")
        if debt <= 0:
            # print("Debt: " + str(debt))
            finalFixedPay =  fixedPay
        else:
            debt = debt * (1+ monthlyInterest)
            # print("Debt: " + str(debt))

    # Increase epsilon
    fixedPay += 10


print('Before Payment: '+ str(finalFixedPay))
while finalFixedPay % 10 !=0:
    finalFixedPay +=1

print('Lowest Payment: '+ str(finalFixedPay))