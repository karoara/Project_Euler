# PROBLEM 7 -------------------------------------------------------------------
# 10001st Prime.

# variables
num_primes = 2
primes_so_far = []
curr_num = 5

# keep iterating over numbers
while num_primes < 10001:
  composite = False

  # check if current number is not prime
  for prime in primes_so_far:
    if curr_num % prime == 0: 
      composite = True
      break
  
  # if it is
  if not composite: 
    primes_so_far.append(curr_num)
    num_primes += 1
  
  # update current number
  if (curr_num-1) % 6 == 0: curr_num += 4
  else: curr_num += 2

print(primes_so_far[len(primes_so_far)-1])
