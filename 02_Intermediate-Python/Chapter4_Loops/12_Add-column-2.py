# Import cars data
import pandas as pd

cars = pd.read_csv("02_Intermediate-Python\Chapter4_Loops\cars.csv", index_col=0)

# Use .apply(str.upper)
cars.loc[:, "COUNTRY"] = cars["country"].apply(str.upper)

print(cars)
