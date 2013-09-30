# Exercise 4: Variables And Names

# Number of cars
cars = 100
# Number of people in cars
space_in_a_car = 4.0
# Number of drivers
drivers = 30
# Number of passengers
passengers = 90
# Number of cars left (total cars - total drivers of cars)
cars_not_driven = cars - drivers
# Number of cars driven (assuming every driver, drives (or every driver has a car))
cars_driven = drivers
# Number of people that can be taken (number of cars * number of people in cars)
carpool_capacity = cars_driven * space_in_a_car
# Number of passengers per car on average
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#--------------------------------------------------------------

# Study Drills

# When I wrote this program the first time I had a mistake, and python told me about it like this:

# Traceback (most recent call last):
#       File "ex4.py", line 8, in <module>
#         average_passengers_per_car = car_pool_capacity / passenger
#     NameError: name 'car_pool_capacity' is not defined

# Explain this error in your own words. Make sure you use line numbers and explain why.

# car_pool_capacity does not exist, only carpool_capacity, so it would throw errors trying to reference something that does not exist. As shown in line 9 (7 of original code), it is carpool_capacity, not car_pool_capacity.

# Here's more Study Drills:

# 1. I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?
# It would be just a whole number.

# 2. Remember that 4.0 is a "floating point" number. Find out what that means.
# Floating point means that numbers can contain fraction parts.

# 3. Write comments above each of the variable assignments.
# Done.

# 4. Make sure you know what = is called (equals) and that it's making names for things.
# Yes.

# 5. Remember that _ is an underscore character.
# Yes.

# 6. Try running python as a calculator like you did before and use variable names to do your calculations. Popular variable names are also i, x, and j.
# Done.