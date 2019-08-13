# PROBLEM 6 -------------------------------------------------------------------
# Sum square difference.

# variables
sum, sum_of_sqs = 0, 0
n = 100

# find sum squared, sum of squares
for i in range(1, n+1): 
  sum += i
  sum_of_sqs += i**2
difference = sum**2 - sum_of_sqs

print(difference)