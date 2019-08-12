# PROBLEM 2 -------------------------------------------------------------------
# Even Fibonacci numbers.

# variables
t1, t2 = 1, 2
sum, limit = 0, 4000000

# iterate over Fibonacci sequence terms, updating sum
while t2 < limit:
  if t2 % 2 == 0: sum += t2
  old_t2 = t2
  t2 = t1 + t2
  t1 = old_t2

print(sum)