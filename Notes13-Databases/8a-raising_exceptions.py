class Wing:

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Flying easily!")
        elif self.ratio == 1:
            print("In the air, but barely...")
        else:
            print("Splat.")


class Duck:

    def __init__(self):
        self.wing = Wing(1.8)

    @staticmethod
    def walk():
        print("Waddle waddle.")

    @staticmethod
    def swim():
        print("Splish splash.")

    @staticmethod
    def quack():
        print("Honk!")

    def fly(self):
        self.wing.fly()


class Penguin:

    def __init__(self):
        self.wing = Wing(0.4)

    @staticmethod
    def walk():
        print("Also waddle waddle.")

    @staticmethod
    def swim():
        print("Zoom! Swoop!")

    @staticmethod
    def quack():
        print("*confused penguin noises*")


class Flock:
    def __init__(self):
        self.flock=[]

    def add_duck(self, duck: Duck) -> None:  # Type Hint—tells type checking tools what type is expected, and what type
        self.flock.append(duck)              # the result is. So IntelliJ will give a warning if we pass a non-Duck.
        #                                      PEP 484 recommends giving everything a type hint if you're giving
        #                                      one to anything.

    def add_duck_with_type_checking(self, duck):
        if isinstance(duck, Duck):   # if you want to make an operation conditional on type, always use isintance()
            self.flock.append(duck)  # rather than type(), because type() will return False if the object is an
            #                          instance of a subclass, whereas isinstance() will correctly return True.
            #                          However, this approach is not pythonic, so generally should be avoided.
            #                          Instead, the pythonic approach would be to check if the behaviour you want
            #                          is supported (in this case, does it have a fly method), rather than the type.
            #                          That said, you might still want to use this for very complex classes (like int)
            #                          Where checking if the object has all the behaviour you're looking for would
            #                          be impractical and potentially inaccurate.

    def add_duck_with_attribute_checking(self, duck):
        fly_method = getattr(duck, "fly", None)  # returns the fly method, if it exists, else None
        if callable(fly_method):  # checks if fly_method is callable (ie checking  it's a method not a data attribute)
            self.flock.append(duck)
        else:
            # Because passing a flightless object to a method that requires flight is a programming error,
            # this is a case where actually raising an exception is a good idea, as it is helpful to fixing
            # the programming error, and gives clear indication that there's something wrong with the program.
            raise TypeError("Cannot add duck, are you sure it's not a " + str(type(duck).__name__))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
            except AttributeError as e:  # stores the exception in a variable (e)
                print("One duck down")
                problem = e  # bind exception to variable from outer scope
        if problem:        # raise exception if it exists—doing this out of the for loop so the loop completes before
            raise problem  # raising any exceptions

