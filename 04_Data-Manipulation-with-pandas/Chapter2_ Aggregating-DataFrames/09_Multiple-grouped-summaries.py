# Import numpy with the alias np
import numpy as np
import pandas as pd

# Read 'homlessness.csv' into a DataFrame as homelessness
sales = pd.read_csv("04_Data-Manipulation-with-pandas\Chapter2_ Aggregating-DataFrames\sales.csv", index_col=0, header=0)

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby("type")["weekly_sales"].agg([np.min, np.max, np.mean, np.median])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby("type")[["unemployment", "fuel_price_usd_per_l"]].agg([np.min, np.max, np.mean, np.median])

# Print unemp_fuel_stats
print(unemp_fuel_stats)