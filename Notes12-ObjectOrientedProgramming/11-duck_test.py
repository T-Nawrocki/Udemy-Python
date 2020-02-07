class Duck:

    def walk(self):
        print("Waddle, waddle, waddle.")

    def swim(self):
        print("Splish splash.")

    def quack(self):
        print("Hjönk.")


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
