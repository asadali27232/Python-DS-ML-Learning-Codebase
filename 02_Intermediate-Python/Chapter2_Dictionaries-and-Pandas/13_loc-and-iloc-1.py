# Import cars data
import pandas as pd

cars = pd.read_csv("02_Intermediate-Python\Chapter2_Dictionaries-and-Pandas\cars.csv", index_col=0)

# Print out observation for Japan
print(cars.loc[["JPN"]])

# Print out observations for Australia and Egypt
print(cars.loc[["AUS", "EG"]])
