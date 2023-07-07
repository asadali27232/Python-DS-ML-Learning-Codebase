# Import cars data
import pandas as pd

cars = pd.read_csv("02_Intermediate-Python\Chapter4_Loops\cars.csv", index_col=0)

# Iterate over rows of cars
for lab, data in cars.iterrows():
    print(lab)
    print(data)
