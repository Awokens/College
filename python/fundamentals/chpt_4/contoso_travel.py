
# This programm will get the following input from the user
# vehicle speed and the number of driving hours.
# And the program will calculate and display the hour
# and miles driven each hour

# Get the hours
hours = int(input('Enter the amount of time (hours): '))
# Get the speed
speed = int(input('Enter the amount of speed (MPH): ')) 

# Print the table headings
print('Hour\tDistance')
print('----------------------')

#Print the hours and distances
for time in range(1, hours + 1):
    Distance = speed * time
    print(time, '\t', Distance)

