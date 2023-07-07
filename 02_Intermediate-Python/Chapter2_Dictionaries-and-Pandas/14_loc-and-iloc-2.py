# Import cars data
import pandas as pd

cars = pd.read_csv("02_Intermediate-Python\Chapter2_Dictionaries-and-Pandas\cars.csv", index_col=0)

# Print out drives_right value of Morocco
print(cars.loc[["MOR"], ["country", "drives_right"]])

# Print sub-DataFrame
print(cars.loc[["RU", "MOR"], ["country", "drives_right"]])
