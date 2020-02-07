# Here, we have three different types of object, bound to three different variables
# However, we can pass each of them to the print() function, and it'll print them.
# So although they are different types of object, they all have similar printable behaviour.

a = 3
b = "tomek"
c = 1, 2, 3

print(a)
print(b)
print(c)

# This is what we mean when we talk about POLYMORPHISM—the ability of objects to have different forms.
# In this example, the polymorphic behaviour in question for the int in a, for example,
# is the standard int behaviour of being able to be added together, etc, plus the behaviour as a printable object.

# In this case, the polymorphic behaviour is implemented using inheritance.
# All three types of object inherit from the base class Object which defines a __str__ method.

# You could also get polymorphism from delegation—inheritance is not the only way, nor necessarily the best.
# The best way of doing this will depend on the circumstances—do you want to ensure (broadly) anything passed to your
# function will do something (in which case inheritance-based polymorphism may be appropriate, because everything
# inheriting from a base class that is compatible with the function will also be compatible), or do you want only
# certain relevant objects to do something (in which case delegation can make sure they're all
# compatible in the same way)
