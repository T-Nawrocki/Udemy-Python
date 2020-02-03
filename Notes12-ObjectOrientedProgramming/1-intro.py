# There are a number of different programming paradigms which can be used.
# So far, we've been mostly using IMPERATIVE programming
# Imperative Programming involves providing a set of instructions to be carried out in a defined order

# Object Oriented Programming looks to take data and the processes which act on that data into objects
# This is called ENCAPSULATION

# Different programming paradigms are not mutually exclusive
# OOP uses Imperative Programming within the methods that objects use to manipulate their data, for example
# Also, our Imperative Programming thus far has already been making extensive use of objects, as we'll see shortly

# Everything in Python IS an object, although that may not have been clear already.
# For example, even data types are classes, so the int data type has a .__add__() method:

a = 1
b = 2
print(a + b)
print(a.__add__(b))  # uses a method for the int class (ctrl + click __add__ for details)
print("=" * 40)


# OOP uses classes and methods to define data and the functions which act on that data
# methods are just functions which are part of a class (there is a slight difference between the two
# but writing a method is exactly the same as writing a function)

# We will create a Kettle class to illustrate a basic case of what a class is

class Kettle(object):  # classes use camel case naming convention

    # think of classes as a template from which objects can be made
    # all objects from the same class (each INSTANCE of the class) will share the same characteristics
    # so our kettle has a make, price, and can be on or off
    # the __init__ method handles these attributes,
    # giving each instance of this class attributes with the values specified
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 10.99  # attributes of the object can be changed like this
print(kenwood.price)

hamilton = Kettle("Hamilton", 12.99)  # this second instance of the object has different values for the same attributes
print(hamilton.make)
print(hamilton.price)

