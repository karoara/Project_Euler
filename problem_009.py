# PROBLEM 9 -------------------------------------------------------------------
# Special Pythagorean Triplet

# variables
limit = 1000

# iterate over possible b values, find a
b = 1
while b < limit + 1:
  poss_a_rem = (2000 * b - 1000000) % (2 * b - 2000)
  poss_a_quo = (2000 * b - 1000000) // (2 * b - 2000)
  if poss_a_rem == 0: 
    a = poss_a_quo
    break
  b += 1

# get a * b * c
answer = a * b * (1000 - a - b)

print(answer)