# this program will get 7 days of temperature values 
# from the user and then save these values to
# the temperatures.txt file

def main():
    # open the temperatures.txt file in append mode
    temp_file = open('temperatures.txt', 'a')

    # add records to the file
    for i in range(1, 8):
        # get the temperature data
        print(f'Enter temperature day {i} data')
        try:
            temp = int(input('Temperature: '))
        except ValueError:
            return print(f'ERROR: day {i} value must be an integer')
            

        # append the data to the file
        temp_file.write(f'{temp}\n')

    # close the file
    temp_file.close()
    print('Data appended to temperature.txt')

# call the main function
main()
