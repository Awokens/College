
# discount for local theater group members
DISCOUNT = 0.05

# Seating costs & their types
ORCHESTRAL_PRICE = 75
CENTER_STAGE_PRICE = 50
OUTER_STAGE_PRICE = 25

# main function
def main():
    # get input amount of per type of seats
    orchestral_seats = int(input('Enter amount of orchestral seats: '))
    center_stage_seats = int(input('Enter amount of center stage seats: '))
    outer_stage_seats = int(input('Enter amount of outer stage seats: '))
    local_member = input('Are you a local theater group member? (yes or no): ')


    # perform calculations for total costs (orchestral, center stage & outer stage seats)
    orchestral_cost = (orchestral_seats * ORCHESTRAL_PRICE)
    center_stage_cost = (center_stage_seats * CENTER_STAGE_PRICE)
    outer_stage_cost = (outer_stage_seats * OUTER_STAGE_PRICE)

    total_sales = (orchestral_cost + center_stage_cost + outer_stage_cost)
    if local_member == 'yes':
        total_sales = determine_discount(total_sales)
        print('Seats discount:', f'{DISCOUNT * 100}% OFF')
    elif local_member == 'no':
        print('Seats discount: none')

    # display results for each type of seat sale
    # and display total sales of revenue
    print("orchestral sales:", f'{orchestral_cost}$')
    print("center stage sales:", f'{center_stage_cost}$')
    print("outer stage sales:", f'{outer_stage_cost}$')
    print("Total revenue sales:", f'{total_sales}$')

# determines the sales after local members discount
def determine_discount(sales):
    return sales - (sales * DISCOUNT)

# call main function
main()

        
