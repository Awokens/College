
# this program reads the values in the temperature 
# data file created in the previous program
# then it will display each temperature value in the file
# and calculate and display the average temperature

def main():

    # read the temperatures.txt file
    temp_file = open('temperatures.txt', 'r')

    # initialize the total temperature variable
    total_temperature = 0

    for i in range(1, 8):
        # read the temperature day record per iteration
        try:
            temp = int(temp_file.readline())
        except ValueError:
            return print(f'Temperature day {i} is not an integer.')

        print(f'Day {i} temperature is {temp}')
        total_temperature += temp
    
    try:
        average_temperature = total_temperature / 7
        print('The average temperature among all 7 days is ', format(average_temperature, ',.2f'))
    except ZeroDivisionError:
        print('ERROR: tried to divide by 0 (total temperature)')

# call the main function
main()
        
