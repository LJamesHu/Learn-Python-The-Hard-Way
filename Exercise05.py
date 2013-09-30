# Exercise 5: More Variables and Printing

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 #inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are unusually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

#--------------------------------------------------------------

# Study Drills

# 1. Change all the variables so there isn't the my_ in front. Make sure you change the name everywhere, not just where you used = to set them.
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 #inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are unusually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# 2. Try more format characters. %r is a very useful one. It's like saying "print this no matter what."
print "I am not %r or %r years old." % (name, age)

# 3. Search online for all of the Python format characters.
# 'd' 	Signed integer decimal.
# 'i' 	Signed integer decimal.
# 'o' 	Signed octal value.
# 'u' 	Obsolete type - it is identical to 'd'.
# 'x' 	Signed hexadecimal (lowercase).
# 'X' 	Signed hexadecimal (uppercase).
# 'e' 	Floating point exponential format (lowercase).
# 'E' 	Floating point exponential format (uppercase).
# 'f' 	Floating point decimal format.
# 'F' 	Floating point decimal format.
# 'g' 	Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.
# 'G' 	Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.
# 'c' 	Single character (accepts integer or single character string). 	 
# 'r' 	String (converts any Python object using repr()).
# 's' 	String (converts any Python object using str()).
# '%' 	No argument is converted, results in a '%' character in the result.

# 4. Try to write some variables that convert the inches and pounds to centimeters and kilos. Do not just type in the measurements. Work out the math in Python.

height_cm = 2.54 * height
print "He's %r centimeters tall." % height_cm

weight_kg = 0.453592 * weight
print "He's %r kilograms heavy." % weight_kg