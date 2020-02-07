# INHERITANCE is essentially the concept of subclassing—a class can inherit attributes and methods from another class
# and add its own on top of those, thereby EXTENDING that class.

# Python supports MULTIPLE INHERITANCE—ie, it is possible to be a subclass of more than one superclass.
# So, for example, Bird has the subclasses FlyingBird, SwimmingBird, and FlightlessBird.
# The Class "Penguin" could be a subclass of both SwimmingBird and FlightlessBird,
# while "Gull" would be a subclass of both FlyingBird and SwimmingBird.
# This is not supported in all other languages—eg in C#, there is no multiple inheritance,
# so inheritance is strictly hierarchical.

# Although multiple inheritance is possible, it is best avoided unless you know for sure that it's what you want to do.
# It's one of those things which can cause problems if you aren't careful, so for now we'll avoid it.

import random


class Enemy:  # note that all classes inherit from the class "Object", so this could be written "class Enemy(Object)"
    """
    Superclass for enemies for our game.

    Attributes:
        name (str): The enemy's name. Defaults to "Enemy"
        hp (int): The enemy's hit points. Defaults to 1.
        lives (int): The enemy's lives. Defaults to 1.
        alive (bool): Is the enemy alive? Defaults to True.

    Methods:
        take_damage(self, int): Sets hp to hp minus the int argument.
            If hp hits 0, sets lives to lives - 1.
            If lives hits 0, sets alive to False.
    """

    def __init__(self, name="Enemy", hp=1, lives=1):
        self.name = name
        self.hp = hp
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_hp = self.hp - damage
        if remaining_hp > 0:
            self.hp = remaining_hp
            print(f"{self.name} took {damage} damage. {self.hp} hp remaining.")
        else:
            self.lives -= 1
            print(f"{self.name} took {damage} damage and died. {self.lives} lives remaining.")
            if self.lives > 0:
                print(f"{self.name} is dead. But they'll be back!")
            else:
                print(f"{self.name} is dead, and there's no coming back from that...")
                self.alive = False


class Troll(Enemy):  # Troll inherits from/extends Enemy

    def __init__(self, name):
        # Various ways to give attributes of name = passed name, hp = 23 and lives = 1:
        # Enemy.__init__(self, name, 23, 1)  # This would be the only way to call the superclass init in Python 2
        # super(Troll, self).__init__(name, 23, 1)  # a Python 3 approach. Need this way if using multiple inheritance.
        super().__init__(name, 23, 1)  # Preferred Python 3 approach.
#                                        Don't need to specify which class because no multiple inheritance.

    # This method is part of the Troll class, but not the Enemy superclass.
    def grunt(self):
        print(f"Me {self.name}. Stomp you, maybe...")


class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name, 12, 3)

    def dodges(self):
        if random.randint(1, 3) == 3:  # randint includes both end points
            print(f"{self.name} dodges, taking no damage.")
            return True
        else:
            return False

    # Can override methods from the parent class.
    # Calling the method will always use the most specific definition of the method
    # (ie the one from the subclass lowest in the class hierarchy).
    # Note we can still call the superclass's method (either in this definition or elsewhere)
    # by using the super() function as with our __init__ methods
    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage)


class VampireKing(Vampire):

    def __init__(self, name):
        super().__init__(name)
        self.hp = 140

    def take_damage(self, damage):
        super().take_damage(damage // 4)


if __name__ == '__main__':
    vlad = VampireKing("Vlad")
    while vlad.alive:
        vlad.take_damage(4)