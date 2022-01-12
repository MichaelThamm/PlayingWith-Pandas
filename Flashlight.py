import pandas as pd

forest = pd.read_excel('DarkBambooForest.xlsx', header=None, usecols="A:J", nrows=10, engine='openpyxl')

"""Enter your code here"""

# Hint
row, col = 8, 0
print(forest[col][row])

# Hint 2
# Keep in mind you are a programmer and this file is called flashlight. You can print more areas around you
# to illuminate your path. This takes some knowledge of lists and 2D arrays so make sure you understand those first
# Ex) A sample of the flashlight at index (8, 1) may look like this:
#       ||
#   ()  .   .
#       ||
