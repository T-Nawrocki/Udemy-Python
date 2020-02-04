"""
A refresher, to make it clear what various key terms mean:

Class: A template for creating objects. All objects created using the same class will have the same characteristics
Object: An instance of a class.
Instantiate: To create an instance of a class.
Method: A function defined within a class.
Attribute: A variable bound to an instance of a class.
"""

# This is not necessarily the case in other object oriented languages,
# but in Python a class is exactly the same thing as a TYPE


class Kettle:

    # class variables—have the same value for each instance of the class
    power_source = "electricity"

    # self is a parameter which refers to the object the method is being called on.
    #
    # While it is technically a parameter, and so could be called anything, the convention is to use "self"
    # this convention is heavily entrenched, so you should never change it, really
    # changing to something other than "self" may break external tools or cause confusion later.
    #
    # You don't need to pass a value for the parameter self when calling a method
    # this is because Python automatically supplies the value when you call the method on an object
    #
    # The __init__ method is a constructor
    # Constructors are a method which are called when an instance of a class is created
    def __init__(self, make, price):

        # instance variables—can have different values for each instance of the class
        self.make = make
        self.price = price
        self.on = False

    # a method to change the attribute "on" to True
    def switch_on(self):
        self.on = True


# can create new attributes on the fly—does not need to be within the class constructor
# when you do this, you can end up with two instances of a class having different attributes
# this is generally not a great idea
# it's more here to demonstrate that mistyping the name of an attribute could end up creating a new attribute
# rather than raising an error like other languages would do
kenwood = Kettle("Kenwood", 8.99)
kenwood.power = 1.5

print(kenwood.power_source)
print(Kettle.__dict__)
