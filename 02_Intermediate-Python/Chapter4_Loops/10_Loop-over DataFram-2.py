# Import cars data
import pandas as pd

cars = pd.read_csv("02_Intermediate-Python\Chapter4_Loops\cars.csv", index_col=0)

# Adapt for loop
for lab, row in cars.iterrows():
    print(lab.strip() + ": ", str(row["cars_per_cap"]).strip())
