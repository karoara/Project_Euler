# PROBLEM 3 -------------------------------------------------------------------
# Largest prime factor.

# imports
import math

# variables
number = 600851475143
biggest_prime = -1
i = 2

# iterate to find prime factors
while i <= int(math.sqrt(number)):
  if number % i == 0: 
    number = number // i 
    biggest_prime = i
  else:
    i += 1

# if leftover factor is bigger than what we've checked
if i < number: biggest_prime = number

print(biggest_prime)