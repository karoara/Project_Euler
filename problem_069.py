# PROBLEM 69 ------------------------------------------------------------------
# Totient maximum.

# imports
from helper_functions.early_problems import prime_factors, totient

# variables
n = 1000001
max_tot, max_tot_num = 0, 0

# call helper functions to get factors, totient values
factors = prime_factors(n)
totients = [totient(i, factors[i]) for i in range(n)]

# iterate through totients, find max n/totient(n)
for i in range(2, n):
  curr_tot = i / totients[i]
  if curr_tot > max_tot: max_tot, max_tot_num = curr_tot, i

print(max_tot_num)