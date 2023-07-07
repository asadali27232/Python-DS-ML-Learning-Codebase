# Import cars data
import pandas as pd

cars = pd.read_csv("02_Intermediate-Python\Chapter3_Logic-Control-Flow-and-Filtering\cars.csv", index_col=0)

# Create car_maniac: observations that have a cars_per_cap over 500
car_maniac = cars[cars["cars_per_cap"] > 500]

# Print car_maniac
print(car_maniac)
