'''
If a runner runs 12 kilometers in 30 minutes and 30 seconds.
What is his/her average speed in miles per hour. (Tip: 1 mile = 1.6 km)

'''
km = 12
mins = 30
secs = 30

# First, convert KM to miles
miles = 12 / 1.6
# Next, convert mins to seconds so we can add them together, then convert to hours
mins_to_secs = mins * 60
hrs = (secs + mins_to_secs) / (60 * 60)

# Calculate miles/hour and print it
speed_mi_per_hour = miles / hrs
print(speed_mi_per_hour)
