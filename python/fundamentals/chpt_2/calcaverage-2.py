# get the three input test scores
# and assign them to individual variables

exam_one = float(input("Enter the first test score: "))
exam_two = float(input("Enter the second test score: "))
exam_three = float(input("Enter the third test score: "))

# calculates the average amongst the three test scores
# and assigns the result to the variable called average
average_score = (exam_one + exam_two + exam_three) / 3.0

# display the average score result
print("The average test score is", average_score)