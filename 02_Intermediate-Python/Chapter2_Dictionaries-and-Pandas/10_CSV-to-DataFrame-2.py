# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv("02_Intermediate-Python\Chapter2_Dictionaries-and-Pandas\cars.csv", index_col=0)

# Print out cars
print(cars)
