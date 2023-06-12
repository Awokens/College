
# the main function
def main():
    print ('\t\t\tMENU WORKSHOP SELECTOR')
    print ('\tWORKSHOPS \tRegistration Fee \tDays')
    print ('1) Handling Stress \t$2000 \t\t\t3 ')
    print ('2) Time Management\t$800 \t\t\t3 ')
    print ('3) Supervision Skills\t$1500 \t\t\t3 ')
    print ('4) How to Interview \t$500 \t\t\t1\n')
    print ('\tLOCATION \tLodging Fee per Day')
    print ('1) Austin \t\t$150')
    print ('2) Chicago\t\t$225 ')
    print ('3) Phoenix\t\t$175 ')
    print ('4) Orlando\t\t$300 ')
    WORKSHOP = int(input('\nEnter the number of your chosen workshop (1-4): '))
    match WORKSHOP:
        case 1:
            workshop_fee = 2000
            days = 3
        case 2:
            workshop_fee = 800
            days = 3
        case 3: 
            workshop_fee = 1500
            days = 3
        case 4:
            workshop_fee = 500
            days = 1
        case _:
            return print('Invalid workshop number, please try again.')    
    LOCATION = int(input('Enter the number of your chosen location (1-4): '))
    lodging_fee = calc_lodging_fees(LOCATION, days)
    total_fee = calc_total_cost(lodging_fee, workshop_fee)

    # display total and workshop fee
    print('\nRegistration: $', format(workshop_fee, ',.2f'))
    print('Lodging: $', format(lodging_fee, ',.2f'))
    print('Total: $', format(total_fee, ',.2f') + '\n')

# calculate the total lodging fees
def calc_lodging_fees(lodging, days):
    match lodging:
        case 1:
            lodging_fee = 150
        case 2:
            lodging_fee = 225
        case 3:
            lodging_fee = 175
        case 4:
            lodging_fee = 300
        case _:
            return print('Invalid location number, please try again.')
    return lodging_fee * days

# calculate the total cost from lodging and workshop fees
def calc_total_cost(lodging_fee, workshop_fee):
    # total lodging fee and workshop fee
    total_fee = lodging_fee + workshop_fee
    return total_fee

# call the main function
main()

