# Import cars data
import pandas as pd

cars = pd.read_csv("02_Intermediate-Python\Chapter4_Loops\cars.csv", index_col=0)

# Code for loop that adds COUNTRY column
for label, data in cars.iterrows():
    cars.loc[label, "COUNTRY"] = data["country"].upper()


# Print cars
print(cars)
