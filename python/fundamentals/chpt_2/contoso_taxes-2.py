## get input purchase price, state & federal taxes

purchase = float(input("Enter your purchase price: "))

# constants for tax rates
STATE_TAX = 6.0
FEDERAL_TAX = 3.5


# perform calculations

# determine the total tax & tax cost on purchase
total_tax = STATE_TAX + FEDERAL_TAX
tax_cost = purchase * (total_tax / 100)


# determine the total of the purchase after taxes

total_sale = purchase + tax_cost


# display results
# sale before tax & after tax, federal & state rate, and total tax
print("Before tax, sale price is: ", f'{purchase}$')
print("Federal Tax:", f'{FEDERAL_TAX}%')
print("State Tax:", f'{STATE_TAX}%')
print("Total tax:", f'{total_tax}%')
print("After tax, total sale price is:", f'{total_sale}$')