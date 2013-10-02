# Exercise 6: Strings and Text

# String with reference
x = "There are %d types of people." % 10
# Making variables
binary = "binary"
do_not = "don't"
# Using above variables
y = "Those who know %s and those who %s." % (binary, do_not)

# Printing above strings
print x
print y

# Printing with above strings as variables
print "I said: %r." % x
print "I also said: '%s'." % y

# Using a boolean and string with boolean
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Printing above
print joke_evaluation % hilarious

# Creating 2 strings
w = "This is the left side of..."
e = "a string with a right side."

# Concatenation
print w + e

#--------------------------------------------------------------

# Study Drills

# 1. Go through this program and write a comment above each line explaining it.
# Done.

# 2. Find all the places where a string is put inside a string. There are four places.
# y = "Those who know %s and those who %s." % (binary, do_not)
# print "I said: %r." % x
# print "I also said: '%s'." % y

# 3. Are you sure there are only four places? How do you know? Maybe I like lying.
# Because the other instances are an integer and a boolean

# 4. Explain why adding the two strings w and e with + makes a longer string.
# It combines the two into one longer string