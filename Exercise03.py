# Exercise 3: Numbers and Math

# Printing a phrase
print "I will now count my chickens:"

# Prints the label of either Hens or Roosters then a math equation
print "Hens", 25 + 30 / 6
# This one is using subtraction, multiplication and modulus.
print "Roosters", 100 - 25 * 3 % 4

# Printing
print "Now I will count the eggs:"

# Add, add, add, subtract, add, modulus, subtract, division, add
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

# Printing
print "Is it true that 3 + 2 < 5 - 7?"

# Doing logic check
print 3 + 2 < 5 - 7

# Printing question then doing the math
print "What is 3 + 2?", 3 + 2
# Printing question then doing the math
print "What is 5 - 7?", 5 - 7

# Printing
print "Oh, that's why it's False."

# Printing
print "How about some more."

# Printing question then check if greater than.
print "Is it greater?", 5 > -2
# Printing question then seeing if greater than or equal.
print "Is it greater or equal?", 5 >= -2
# Printing question then seeing if less than or equal.
print "Is it less or equal?", 5 <= -2

#--------------------------------------------------------------

# Study Drills

# 1. Above each line, use the # to write a comment to yourself explaining what the line does.
# Done

# 2. Remember in Exercise 0 when you started Python? Start Python this way again and using the above characters and what you know, use Python as a calculator.
# Done

# 3. Find something you need to calculate and write a new .py file that does it.
print 12000 * 10837224969.5 , 84000 * 10837224969.5

# 4. Notice the math seems "wrong"? There are no fractions, only whole numbers. Find out why by researching what a "floating point" number is.
# Floating point numbers are basically numbers that have decimal points. 

# 5. Rewrite ex3.py to use floating point numbers so it's more accurate (hint: 20.0 is floating point).

print "I will now count my chickens:"

print "Hens", 25.0 + 30.0 / 6.0
print "Roosters", 100.0 - 25.0 * 3.0 % 4.0

print "Now I will count the eggs:"

print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0

print "Is it true that 3 + 2 < 5 - 7?"

print 3.0 + 2.0 < 5.0 - 7.0

print "What is 3 + 2?", 3.0 + 2.0
print "What is 5 - 7?", 5.0 - 7.0

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5.0 > -2.0
print "Is it greater or equal?", 5.0 >= -2.0
print "Is it less or equal?", 5.0 <= -2.0