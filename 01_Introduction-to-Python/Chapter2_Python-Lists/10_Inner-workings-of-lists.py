# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy don't use areas_copy = areas because it will be a reference to areas
# and if you change areas_copy you will change areas too
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
