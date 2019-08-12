# PROBLEM 5 -------------------------------------------------------------------
# Smallest multiple.

# imports
import math

# variables
numbers = [i for i in range(1, 21)]
pf_bag = []
i, lcm = 2, 1

# get "bag" of prime factors
for i in range(2, 21):
  max_times = 0

  # remove current factor from all numbers
  for j in range(len(numbers)):
    times = 0

    # remove factor from current number
    while numbers[j] % i == 0:
      numbers[j], times = numbers[j] // i, times + 1
    if times > max_times: max_times = times
  
  # update bag with factor info
  pf_bag.append([i, max_times])

# get LCM of all numbers using prime factors
for factor_info in pf_bag: lcm *= math.pow(factor_info[0], factor_info[1])

print(lcm)