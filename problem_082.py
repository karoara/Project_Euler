# PROBLEM 82 ------------------------------------------------------------------
# Path sum: three ways.

# imports
import sys

# create matrix
f = open("other_files/p81_82_83_matrix.txt", "r")
data, matrix = f.readlines(), []
for line in data: matrix.append([int(number) for number in line.split(",")])

# variables
num_rows, num_cols = len(matrix), len(matrix[0])
dp = [([0] * num_cols) for i in range(num_rows)]
current_down, current_up = [0] * num_rows, [0] * num_cols

# fill DP-solutions for final column of squares
for i in range(num_rows): dp[i][num_cols - 1] = matrix[i][num_cols - 1]

# iterate over remaining matrix/DP-solution squares
for i in range(num_cols - 2, -1, -1):

    # get down + right solutions for current column
    for j in range(num_rows - 1, -1, -1):
      if j == num_rows - 1: current_down[j] = dp[j][i+1] + matrix[j][i]
      else:
        if dp[j][i+1] < current_down[j+1]: current_down[j] = dp[j][i+1] + matrix[j][i]
        else: current_down[j] = current_down[j+1] + matrix[j][i]
    
    # get up + right solutions for current column
    for j in range(num_rows):
      if j == 0: current_up[j] = dp[j][i+1] + matrix[j][i]
      else:
        if dp[j][i+1] < current_up[j-1]: current_up[j] = dp[j][i+1] + matrix[j][i]
        else: current_up[j] = current_up[j-1] + matrix[j][i]
    
    # choose between down/up solutions
    for j in range(num_rows):
      if current_up[j] < current_down[j]: dp[j][i] = current_up[j]
      else: dp[j][i] = current_down[j]

# find best DP square in first column
solution = sys.maxsize
for i in range(num_rows):
  if dp[i][0] < solution: solution = dp[i][0]

print(solution)