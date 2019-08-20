# HELPER FUNCTIONS ------------------------------------------------------------
# Helper functions for early project euler problems.


# imports
import math


# Returns primes up to n.
# nlog(log(n)) complexity. 
def primes(n):

  # variables
  visited = [0] * n
  primes = []

  # sieve of eratosthenes
  for i in range(2, int(math.sqrt(n))):
    if visited[i] == 0: 
      primes.append(i)
      visited[i] = 1
      for j in range(i**2, n, i): visited[j] = 1
  
  # get primes not collected thus far
  for i in range(int(math.sqrt(n)), n):
    if visited[i] == 0: primes.append(i)
  
  return primes


# Returns factors of numbers up to (not including) n.
# nlog(n) complexity.
def factors(n):

  # variables
  factors = [[1] for i in range(n-1)]

  # sieve-like method of iteration
  for i in range(2, n):
    for j in range(i, n, i): factors[j-1].append(i)
  
  return factors


# Returns prime factors of numbers up to (not including) n.
# nlog(log(n)) complexity.
def prime_factors(n):

  # variables
  factors = [[] for i in range(n)]
  visited = [0 for i in range(n)]

  # sieve of eratosthenes
  for i in range(2, n):
    if visited[i] == 0:
      for j in range(i, n, i):
        factors[j].append(i)
        visited[j] = 1
  
  return factors


# Returns totient(n) given prime factors of n.
# 2^(x) complexity (where x = # of prime factors of n).
# As x <= log(log(n)) in typical cases, thus approx. log(n) complexity.
def totient(n, factors):

  # handle edge cases (0/1 factor)
  if len(factors) == 0: return n
  if len(factors) == 1: return n - 1
  
  # call recursive helper
  return totient_helper(n, factors, 1, 0, 0, 0)


# Helper function for getting totient(n).
def totient_helper(n, factors, curr_lcm, i, num_factors, totient_n):

  # if we've finished the factors
  if i == len(factors):
    if num_factors == 0: return n
    elif num_factors % 2 == 0: return totient_n + n // curr_lcm
    else: return totient_n - n // curr_lcm
  
  # if not, move to next factor with/without adding current
  totient_n = totient_helper(n, factors, curr_lcm, i+1, num_factors, totient_n)  
  totient_n = totient_helper(n, factors, curr_lcm*factors[i], i+1, num_factors+1, totient_n)

  return totient_n


# Prime factorization of numbers up to n.

# Factors of set of numbers.

# Prime factorization of set of numbers.

# Prime factors of set of numbers.