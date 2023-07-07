# Import cars data
import pandas as pd

cars = pd.read_csv("02_Intermediate-Python\Chapter3_Logic-Control-Flow-and-Filtering\cars.csv", index_col=0)

# Extract drives_right column as Series: dr
dr = cars["drives_right"]

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)
