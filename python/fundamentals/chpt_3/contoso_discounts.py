# price per widget
WIDGET_PRICE = 95

# get amount of widgets input
WIDGETS = int(input("Enter a number of widgets you'd like to purchase: "))

discount = 0 # default discount value
total_widget_cost = WIDGET_PRICE * WIDGETS # calculates the total widget cost

# check the quantity and associate it with the discount percentage
if 10 <= WIDGETS <= 19:
    discount = 10
elif 20 <= WIDGETS <= 49:  
    discount = 20
elif 50 <= WIDGETS <= 99:
    discount = 30
elif WIDGETS >= 100:
    discount = 40

# calculate total purchase amount (after discount)
total_purchase = total_widget_cost - (total_widget_cost * (discount / 100))

# display discount amount and total purchase amount after discount
print('Discount amount: ', f'{discount}%')
print('Total purchase amount: $', format(total_purchase, ',.2f'))

