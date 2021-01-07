#Compute monthlyPayment and totalPayment given annualInterestRate, numberOfYears and loanAmount

#Prompt user to enter annualInterestRate, numberOfYears and loanAmount

annualInterestRate = eval(input("Enter annual interest rate: "))
monthlyInterestRate = annualInterestRate / 1200  #input is annual % format: 4.5% -> monthly % = 4.5%/12 -> need to convert it to decimal, divide it by 100 => 4.5/12/100 = 4.5/1200

numberOfYears = eval(input("Enter number of years as an integer: "))

loanAmount = eval(input("Enter loan amount: "))

monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1/ (1 + monthlyInterestRate) ** (numberOfYears * 12))

totalPayment = monthlyPayment * numberOfYears * 12

print("The monthly payment is: ", int(monthlyPayment * 100) / 100)
print("The total payment is", int(totalPayment * 100) / 100)

