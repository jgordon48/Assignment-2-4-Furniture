# input statements
salary=float(input("Enter the salary: "))
numDependents=int(input("Enter the number of dependents: "))


# calculate taxes here
stateTax = salary * 0.065
federalTax = salary * 0.28
dependentDeduction = (salary * 0.025) * numDependents
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding
# print out the results here
print("State Tax: $" + str(round(stateTax, 2)))
print("Federal Tax: $" + str(round(federalTax, 2)))
print("Dependents: $" + str(round(dependentDeduction, 2)))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))