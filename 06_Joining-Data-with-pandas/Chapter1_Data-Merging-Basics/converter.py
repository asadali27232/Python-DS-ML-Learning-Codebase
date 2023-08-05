import pickle as pkl
import pandas as pd

with open("land_use.p", "rb") as f:
    object = pkl.load(f)

df = pd.DataFrame(object)
df.to_csv(r"land_use.csv")
