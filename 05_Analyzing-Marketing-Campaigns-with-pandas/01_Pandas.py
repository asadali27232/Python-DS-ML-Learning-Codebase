# Import pandas into the environment
import pandas as pd

# Import marketing.csv
marketing = pd.read_csv("marketing.csv")

# Print the first five rows of the DataFrame
print(marketing.head())

# Print the statistics of all columns
print(marketing.describe())

# Check column data types and non-missing values
print(marketing.info())

# Check the data type of is_retained
print(marketing["is_retained"].dtype)

# Convert is_retained to a boolean
marketing["is_retained"] = marketing["is_retained"].astype("bool")

# Check the data type of is_retained, again
print(marketing["is_retained"].dtype)
