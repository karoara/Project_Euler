# PROBLEM 1 -------------------------------------------------------------------
# Multiples of 3 and 5.

# variables
n1, n2 = 3, 5
sum = 0

# add multiples to sum
for i in range(1000):
  if i % 3 == 0 or i % 5 == 0: sum += i 

print(sum)