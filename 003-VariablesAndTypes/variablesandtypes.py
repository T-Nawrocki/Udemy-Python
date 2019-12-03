# CONTAINS CONTENT FROM

# variables in python are typed, but you do not need to explicitly declare the type
greeting = "Hello"  # because greeting is initialised with a string, the variable is implicitly typed as a string

# variable naming conventions:
#   must begin with upper or lower case letter or _
#   can contain a number, but cannot begin with one
#   variable names are case sensitive

# variables are created when initialised using the = operator
# Python documentation uses the word "bound" to describe the relationship between variable and value
age = 26  # age is bound to the value 26
name = "Tomek"  # name is bound to the string "Tomek"

# Python is strongly typed—values etc have types and these types matter a lot about how they can interact
# Python is dynamically typed—types don't need to be explicitly declared and a degree of implicit conversion is possible

print(type(age))  # type() function returns the type of the argument
print(type(name))

# Because of the way dynamic types work, it makes sense to think of values as typed, rather than variables.
# Variables are just a name. You can attach the name to something new of a different type.
# But you can't change the type of the objects themselves—"string" is always a string, it cannot become an int

age = "27 years"  # the variable is rebound to a string value. This is not changing the type of the values though.

# Python is still strongly typed—eg you cannot concatenate string and int
print(name + " is " + 27 + " years old") # this causes an error—note highlighting of invalidly typed value

##############################################

# Python's built-in data types can be classed as:
#   numeric
#   iterator
#   sequence (which are also iterators)
#   mapping
#   file
#   class
#   exception

# We'll look at numeric types for now:
# There are four numeric data types:
#   int (Python 2 had a long type for larger ints, but Python 3 has expanded int to include these)
#   float
#   decimal
#   complex—contain real and imaginary part, only needed for complex number theory

# int effectively has NO MAXIMUM SIZE. The limit is essentially memory limit
# float's maximum value on a 64-bit computer is ~1.8e+308
# float's minimum value on a 64-bit computer is ~2.2e-308 floats have 52 digit precision.
# If you need more, the decimal data type can handle that, but we won't need that for this course

