import pandas as pd

licenses = pd.read_csv("licenses.csv", index_col=0, header=0)
wards = pd.read_csv("wards.csv", index_col=0, header=0)
zip_demo = pd.read_csv("zip_demo.csv", index_col=0, header=0)

# Merge licenses and zip_demo, on zip; and merge the wards on ward
licenses_zip_ward = licenses.merge(zip_demo, on="zip").merge(wards, on="ward")

# Print the results by alderman and show median income
print(licenses_zip_ward.groupby("alderman").agg({"income": "median"}))
