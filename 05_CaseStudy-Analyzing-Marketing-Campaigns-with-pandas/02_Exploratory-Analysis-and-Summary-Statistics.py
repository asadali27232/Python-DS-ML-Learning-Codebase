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

# Isolate english speakers
english_speakers = marketing[marketing["language_displayed"] == "English"]

# Calculate the total number of English speaking users
total = english_speakers["user_id"].nunique()

# Calculate the number of English speakers who converted
subscribers = english_speakers[english_speakers["converted"] == True]["user_id"].nunique()

# Calculate conversion rate
conversion_rate = subscribers / total
print("English speaker conversion rate:", round(conversion_rate * 100, 2), "%")

# Group by language_displayed and count unique users
total = marketing.groupby("language_displayed")["user_id"].nunique()

# Group by language_displayed and count unique conversions
subscribers = marketing[marketing["converted"] == True].groupby("language_displayed")["user_id"].nunique()

# Calculate the conversion rate for all languages
language_conversion_rate = subscribers / total
print(language_conversion_rate)

# Group by date_served and count unique users
total = marketing.groupby("date_served")["user_id"].nunique()

# Group by date_served and count unique converted users
subscribers = marketing[marketing["converted"] == True].groupby("date_served")["user_id"].nunique()

# Calculate the conversion rate per day
daily_conversion_rate = subscribers / total
print(daily_conversion_rate)
