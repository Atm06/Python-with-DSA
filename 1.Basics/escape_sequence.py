# Escape Sequence denotes special characters (which always comes in double/single quotes: "", '')

"""
\n -> new Line
\t -> tab
\\ -> backslash
\' -> single quote
\"  -> Double Quotes
\b -> Backspace

"""
print("Hello\tWorld\nGood Bye\nI am learning Python")
# \n is used to move the cursor to next line. It is used to print the output in new line.

# Single and Double Quotes are used for defining string literals. We can use any

print("My name is Ashutosh\nMy age is 22\nI am learning Python")

#Keyboard shortcut to comment multiple lines: use ctrl + / (forward slash)
# print("hii")
# print("hello")

#output: Trainer's name is A\\nirudh
print("Trainer's name is A\\\\nirudh")

#output: Trainer's name is "Anirudh"
print('Trainer\'s name is "Anirudh"')

print("Trainer\'s name is \"Anirudh\"")

print("Trainer's name is 'Anirudh'")

"""
TASK 1

REQUIRED OUTPUT: a"\\"xyz'"\

"""
#Solution:
print("a\"\\\\\"xyz'\"\\")

"""
TASK 2

REQUIRED OUTPUT: a"\/\"xyz'"\
"""
#solution:
print("a\"\\/\\\"xyz'\"\\")