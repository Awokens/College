#Print menu
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


# main function
# find the workshop by the workshop variable's value
# then calculate and display the registeration fees

def __main__():
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

    match LOCATION:
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
    # calculate total fee and display the total fee along with the days
    total_lodging = lodging_fee * days

    # total lodging fee and workshop fee
    total_fee = total_lodging + workshop_fee

    # display total and workshop fee
    print('\nRegistration: $', format(workshop_fee, ',.2f'))
    print('Lodging: $', format(total_lodging, ',.2f'))
    print('Total: $', format(total_fee, ',.2f') + '\n')

# input constants
# get workshop number and location
# then run the "__main__" function        
try:
    WORKSHOP = int(input('\nEnter the number of your chosen workshop (1-4): '))
    LOCATION = int(input('Enter the number of your chosen location (1-4): '))
    __main__()
except:
    print('Something went wrong, you likely entered invalid numbers. Otherwise please try again.')