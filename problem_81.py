# PROBLEM 81 ------------------------------------------------------------------
# Path sum: two ways.

# create matrix
f = open("other_files/matrix.txt", "r")
data, matrix = f.readlines(), []
for line in data: matrix.append([int(number) for number in line.split(",")])

# variables
num_rows, num_cols = len(matrix), len(matrix[0])
dp = [([0] * num_cols) for i in range(num_rows)]

# iterate over matrix/DP-solution squares
for i in range(num_cols - 1, -1, -1):
  for j in range(num_rows - 1, -1, -1):

    # get minimal path sum from current square
    if i == num_cols - 1 and j == num_rows - 1: dp[j][i] = matrix[j][i]
    elif i == num_cols - 1 and j != num_rows - 1: dp[j][i] = dp[j+1][i] + matrix[j][i]
    elif j == num_rows - 1 and i != num_cols - 1: dp[j][i] = dp[j][i+1] + matrix[j][i]
    else:
      if dp[j][i+1] < dp[j+1][i]: dp[j][i] = dp[j][i+1] + matrix[j][i]
      else: dp[j][i] = dp[j+1][i] + matrix[j][i]

print(dp[0][0])