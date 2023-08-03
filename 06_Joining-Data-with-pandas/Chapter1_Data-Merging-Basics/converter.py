import pickle as pkl
import pandas as pd

with open("licenses.p", "rb") as f:
    object = pkl.load(f)

df = pd.DataFrame(object)
df.to_csv(r"licenses.csv")

with open("business_owners.p", "rb") as f:
    object = pkl.load(f)

df = pd.DataFrame(object)
df.to_csv(r"biz_owners.csv")
