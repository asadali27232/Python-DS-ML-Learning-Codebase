# In this chapter, you will learn about common marketing metrics and how to calculate them using pandas. You will also visualize your results and practice user segmentation.
import pandas as pd

marketing = pd.read_csv("marketing.csv", parse_dates=["date_served", "date_subscribed", "date_canceled"])

# Calculate the number of people we marketed to
total = marketing["user_id"].nunique()

# Calculate the number of people who subscribed
subscribers = marketing[marketing["converted"] == True]["user_id"].nunique()

# Calculate the conversion rate
conversion_rate = subscribers / total
print(round(conversion_rate * 100, 2), "%")

# Calculate the number of subscribers
total_subscribers = marketing[marketing["converted"] == True]["user_id"].nunique()

# Calculate the number of people who remained subscribed
retained = marketing[marketing["is_retained"] == True]["user_id"].nunique()

# Calculate the retention rate
retention_rate = retained / total_subscribers
print(round(retention_rate * 100, 2), "%")
