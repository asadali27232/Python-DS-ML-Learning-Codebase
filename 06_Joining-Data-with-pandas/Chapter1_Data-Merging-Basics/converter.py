import pickle as pkl
import pandas as pd

with open("zip_demo.p", "rb") as f:
    object = pkl.load(f)

df = pd.DataFrame(object)
df.to_csv(r"zip_demo.csv")
