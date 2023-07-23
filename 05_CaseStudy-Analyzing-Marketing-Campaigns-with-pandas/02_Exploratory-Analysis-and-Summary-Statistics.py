# In this chapter, you will learn about common marketing metrics and how to calculate them using pandas. You will also visualize your results and practice user segmentation.
import pandas as pd

marketing = pd.read_csv("marketing.csv", parse_date=["date_served", "date_subscribed", "date_canceled"])
