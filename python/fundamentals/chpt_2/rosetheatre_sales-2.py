
# Seating costs & their types
orchestral_price = 75
center_stage_price = 50
outer_stage_price = 25

# get input amount of per type of seats

orchestral_seats = int(input("Enter amount of orchestral seats: "))
center_stage_seats = int(input("Enter amount of center stage seats: "))
outer_stage_seats = int(input('Enter amount of outer stage seats: '))

# perform calculations for total costs (orchestral, center stage & outer stage seats)
1
orchestral_cost = (orchestral_seats * orchestral_price)
center_stage_cost = (center_stage_seats * center_stage_price)
outer_stage_cost = (outer_stage_seats * outer_stage_price)

total_sales = (orchestral_cost + center_stage_cost + outer_stage_cost)

# display results for each type of seat sale
# and display total sales of revenue
print("orchestral sales:", f'{orchestral_cost}$')
print("center stage sales:", f'{center_stage_cost}$')
print("outer stage sales:", f'{outer_stage_cost}$')
print("Total revenue sales:", f'{total_sales}$')
