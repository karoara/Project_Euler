# PROBLEM 10 ------------------------------------------------------------------
# Summation of primes.

# imports
import math

# variables
sum, limit = 0, 2000000
init_limit = int(math.sqrt(limit))
numbers = [0] * limit

# sieve of eratosthenes
for i in range(2, init_limit + 1):
  if numbers[i] == 0:
    sum += i
    for j in range(i**2, limit, i): numbers[j] = 1

# add remaining primes
for i in range(init_limit + 1, limit):
  if numbers[i] == 0: sum += i

print(sum)