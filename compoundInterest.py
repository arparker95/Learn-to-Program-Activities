initialInvestment = input("How much are you going to invest? ")
term = input("How many years are you going to invest the money? ")
interestRate = input("Input the annual interest rate as a decimal. [For 2% enter .02] ")
x = 1
print "Month\tInterest Earned\tTotal"
while x < (term*12+1):
    interestEarned = initialInvestment * (interestRate/12)
    initialInvestment = interestEarned + initialInvestment
    print x, "\t" , "$", "{:.2f}".format(interestEarned) , "\t" , "$" , "{:.2f}".format(initialInvestment)
    x = x + 1
                     

                
