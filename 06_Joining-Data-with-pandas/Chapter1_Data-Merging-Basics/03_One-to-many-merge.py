import pandas as pd

# Read the DataFrames
licenses = pd.read_csv("licenses.csv", index_col=0, header=0)
biz_owners = pd.read_csv("biz_owners.csv", index_col=0, header=0)

# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(biz_owners, on="account")

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby("title").agg({"account": "count"})

# Sort the counted_df in desending order
sorted_df = counted_df.sort_values(by="account", ascending=False)

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())
