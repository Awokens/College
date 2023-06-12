
# get input user's item price
original_price = float(input("Enter item's initial price: "))

# calculate discount from percentage
discount = original_price * 0.2

# total sale cost
sale_cost = original_price - discount

print("The sale price is ", sale_cost)