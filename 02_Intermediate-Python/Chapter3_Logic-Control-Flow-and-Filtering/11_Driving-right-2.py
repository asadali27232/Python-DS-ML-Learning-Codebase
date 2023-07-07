# Import cars data
import pandas as pd

cars = pd.read_csv("02_Intermediate-Python\Chapter3_Logic-Control-Flow-and-Filtering\cars.csv", index_col=0)

# Convert code to a one-liner
sel = cars[cars["drives_right"]]

# Print sel
print(sel)
