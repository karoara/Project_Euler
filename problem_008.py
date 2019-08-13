# PROBLEM 8 -------------------------------------------------------------------
# Largest product in a series.

# import number
f = open("other_files/p8_number.txt")
number = f.readline()
number = number[:len(number) - 1]

# variables
num_digits = 13
max_product, curr_product = 1, 1
i, recent_zero = 0, -1

# iterate over number, search for max product
while i < len(number):
  if int(number[i]) == 0: recent_zero, curr_product = i, 1
  elif i - recent_zero <= num_digits: curr_product *= int(number[i])
  else:
    curr_product *= int(number[i])   
    curr_product //= int(number[i - num_digits])
    if curr_product > max_product: max_product = curr_product
  i += 1

print(max_product)