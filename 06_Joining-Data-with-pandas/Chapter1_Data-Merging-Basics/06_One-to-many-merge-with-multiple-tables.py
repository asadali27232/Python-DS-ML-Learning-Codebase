import pandas as pd

land_use = pd.read_csv("land_use.csv", index_col=0, header=0)
census = pd.read_csv("census.csv", index_col=0, header=0)
licenses = pd.read_csv("licenses.csv", index_col=0, header=0)

# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = land_use.merge(census, on="ward").merge(licenses, on="ward", suffixes=["_cen", "_lic"])

# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = land_use.merge(census, on="ward").merge(licenses, on="ward", suffixes=("_cen", "_lic"))

# Group by ward, pop_2010, and vacant, then count the # of accounts
pop_vac_lic = land_cen_lic.groupby(["ward", "pop_2010", "vacant"], as_index=False).agg({"account": "count"})

# Sort pop_vac_lic and print the results
sorted_pop_vac_lic = pop_vac_lic.sort_values(["vacant", "account", "pop_2010"], ascending=[False, True, True])

# Print the top few rows of sorted_pop_vac_lic
print(sorted_pop_vac_lic.head())
