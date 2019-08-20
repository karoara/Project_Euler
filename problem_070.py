# PROBLEM 70 ------------------------------------------------------------------
# Totient permutation.

# imports
from helper_functions.early_problems import prime_factors, totient


# permutation-checking helper function
def check_permutation(number1, number2):

  # variables
  str_num_1 = str(number1)
  str_num_2 = str(number2)

  # edge case - diff length
  if len(str_num_1) != len(str_num_2): return False
  
  # create count arrays
  count_1, count_2 = [0] * 10, [0] * 10
  for digit in str_num_1: count_1[int(digit)] += 1
  for digit in str_num_2: count_2[int(digit)] += 1
  
  # check permutation
  for digit in range(10):
    if count_1[digit] != count_2[digit]: return False
  return True


# variables
n = 10000001
min_tot, min_tot_num = 10**8, 10**8

# call helper functions to get factors, totient values
factors = prime_factors(n)
totients = [totient(i, factors[i]) for i in range(n)]

# iterate, find max n/totient(n) when permutation applies
for i in range(2, n):
  if check_permutation(i, totients[i]) and i / totients[i] < min_tot:
    min_tot = i / totients[i]
    min_tot_num = i

print(min_tot_num)
print(totients[min_tot_num])