def emiCalc(balance, annualInterestRate): 
    monthlyInterest = annualInterestRate / 12
    simulation = 0

    fixedPay = int(balance / 12)
    debt = balance

    while debt > 0:
        debt = balance
        simulation += 1

        # print("Simulation: " + str(simulation), end=" ")
        # print("Fixed Payment: " + str(fixedPay))

        for i in range(1, 13):
            debt = debt - fixedPay
            # print("Month: " + str(i), end=" ")
            if debt <= 0:
                # print("Debt: " + str(debt))
                while fixedPay % 10 !=0:
                    fixedPay +=1
                
                return fixedPay
            else:
                debt = debt * (1+ monthlyInterest)
                # print("Debt: " + str(debt))
 
        # Increase epsilon
        fixedPay += 5



print('Lowest Payment: '+ str(emiCalc(3329, 0.2)))
print('Lowest Payment: '+ str(emiCalc(4773, 0.2)))
print('Lowest Payment: '+ str(emiCalc(3926, 0.2)))
print('Lowest Payment: '+ str(emiCalc(207, 0.18)))
print('Lowest Payment: '+ str(emiCalc(198, 0.18)))
print('Lowest Payment: '+ str(emiCalc(3833, 0.2)))
print('Lowest Payment: '+ str(emiCalc(4125, 0.04)))