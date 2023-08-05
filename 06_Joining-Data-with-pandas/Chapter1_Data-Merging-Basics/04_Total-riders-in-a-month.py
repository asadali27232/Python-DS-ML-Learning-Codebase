import pandas as pd

ridership = pd.read_csv("ridership.csv", index_col=0, header=0)
cal = pd.read_csv("cal.csv", index_col=0, header=0)
stations = pd.read_csv("stations.csv", index_col=0, header=0)

# Merge the ridership and cal tables
ridership_cal = ridership.merge(cal, on=["year", "month", "day"])

# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=["year", "month", "day"]).merge(stations, on="station_id")

# Create a filter to filter ridership_cal_stations
filter_criteria = (ridership_cal_stations["month"] == 7) & (ridership_cal_stations["day_type"] == "Weekday") & (ridership_cal_stations["station_name"] == "Wilson")

# Use .loc and the filter to select for rides
print(ridership_cal_stations.loc[filter_criteria, "rides"].sum())
