# Import pandas using the alias pd
import pandas as pd

# Read 'sales.csv' into a DataFrame as homelessness
sales = pd.read_csv("04_Data-Manipulation-with-pandas\Chapter2_ Aggregating-DataFrames\sales.csv", index_col=0, header=0)

# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)
