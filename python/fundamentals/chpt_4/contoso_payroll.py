
# This program will get the following input of days and then calculate
# exponentially (double) each day initially with one penny
# and then displaying each day and their total pennies

# the penny start
penny = 0.01


# get the input amount of days 
days = int(input('Enter the amount days: '))

# Display the table headings
print('Day', '\t', 'Pay')
print('---------------------')
print(1, '\t', f'${penny}')

# Calculate and print out the penny exponential growth
for day in range(2, days + 1):
    penny *= 2
    print(day, '\t', f'${penny}')

# Display the total pay results
print('Total pay is', f'${penny}')

