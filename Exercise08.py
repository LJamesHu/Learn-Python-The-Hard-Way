# Exercise 8: Printing, Printing

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"that you could type up right.",
	"but it didn't sing.",
	"So I said good night."
)

#--------------------------------------------------------------

# Study Drills

# 1. Do your checks of your work, write down your mistakes, and try not to make them on the next exercise.
# Done.

# 2. Notice that the last line of output uses both single-quotes and double-quotes for individual pieces. Why do you think that is?
# %r tries to display the text in the most efficient way possible, so it does not need to be consistent