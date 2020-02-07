# COMPOSITION is a relationship between objects where, rather than being a superclass-subclass relationship,
# the relationship is that the Composite is comprised of its components. So rather than an *is a* relationship,
# it's a *has a* relationship.

# A duck is not a wing, nor is a wing a duck, a duck *has* a wing—the wing is part of the duck.


class Wing:

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Soaring above the clouds.")
        elif self.ratio == 1:
            print("Barely staying aloft.")
        else:
            print("Hubris!")


class Duck:

    # The duck now has a wing (which is a Wing object), even though Wing is not a subclass of Duck.
    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle.")

    def swim(self):
        print("Splish splash.")

    def quack(self):
        print("Hjönk.")

    # Because Duck now has a _wing attribute which is a Wing object, it can use methods of the Wing class.
    def fly(self):
        self._wing.fly()


class Penguin:

    def walk(self):
        print("Also waddle, waddle, waddle.")

    def swim(self):
        print("Swimmy swim swim.")

    def quack(self):
        print("*Confused penguin sounds*")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()


if __name__ == '__main__':

    duck = Duck()
    penguin = Penguin()

    test_duck(duck)
    test_duck(penguin)

    # Although penguin is acting a bit differently to duck, as far as our test is concerned
    # it walks like a duck, swims like a duck, and quacks like a duck. It is a duck.
    # So our penguin is passing the duck test.

    # This shows how Python's dynamic typing means we don't actually care what the *types* of things are,
    # Python only really cares about what they can *do* (ie, their attributes and methods).

    # Languages which share this behaviour are sometimes referred to as "duck-typed"

    # This is also an example of Polymorphism not based on inheritance—
    # Duck and Penguin have the same behaviour, but not because they're sibling classes of a parent class;/
