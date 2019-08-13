# PROBLEM 4 -------------------------------------------------------------------
# Largest palindrome product.

# checks if number is palindrome
def palindrome_checker(number):
  str_num = str(number)
  for i in range(len(str_num)//2):
    if str_num[i] != str_num[len(str_num)-1-i]: return False
  return True

# variables
i, j = 999, 999
i_thresh, j_thresh = 100, 100
lpp = 0

# search the space of 3-digit-number-products for largest palindrome
while i >= i_thresh:
  num = i * j 

  # if we have a new largest palindrome - update LPP, search space
  if palindrome_checker(num) and num > lpp:
    lpp = num
    i_thresh = j + 1
    j_thresh = i_thresh
  
  # update i and j
  if j <= j_thresh:
    i -= 1
    j = i
  else:
    j -= 1

print(lpp)