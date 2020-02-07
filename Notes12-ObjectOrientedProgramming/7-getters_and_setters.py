# Python classes don't *need* getters and setters in order for external code to read/write their attributes.
# In other words, there's no real private/public distinction in Python.

# However, getters and setters can still be *useful*, even if they're not *required*.

# For example, you could use a getter to manipulate your data before it is provided,
# like multiplying a score value by the number of lives a player has in a game,
# so that when another function gets the score, they get the multiplied value,
# but you don't need that calculation to be run before storing the data in the object itself.

# Similarly, a setter could be used to run checks on an attribute before the new value is assigned.
# For example, a setter handling the player's remaining lives might check whether the number of lives
# will be greater than 0, rather than just blindly changing the value to whatever is passed in.

# Getters and setters are used by PROPERTIES when reading and writing the attribute.
# So the PROPERTY is what external code interacts with, not the attribute directly, and the property indicates
# which getter and setter methods are used


class Player:
    """
    Simple player class.

    Attributes:
        name (str): Player name.
        _lives (int): Number of lives. Starts at 3.
        _level (int): Current level. Starts at 1.
        score (int): Current score. Starts at 0.
    """

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self.score = 0
        print(f"New player {self.name} created.")

    # getter for lives
    def _get_lives(self):
        return self._lives

    # setter for lives (validates to prevent lives going below 0)
    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Attempt to reduce lives below 0 failed. Lives set to 0.")
            self._lives = 0

    def _get_level(self):
        return self._level

    # when level is set, also sets score to score + (change in level * 1000)
    def _set_level(self, level):
        if level >= 1:
            delta = level - self._level
            self.score += delta * 1000
            self._level = level
        else:
            print("Attempt to reduce level below 1 failed. Level set to 1.")
            self._level = 1

    # lives property uses the getter and setter when reading and writing the _lives attribute
    # note we're not calling the getter or setter here, so no () after them
    # could omit either getter or setter to make the property write/read only respectively
    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    # __str__ returns a printable version of an object
    # this method overrides the default from the Object class
    def __str__(self):
        return f"Name: {self.name}; Lives: {self.lives}; Level: {self._level}; Score: {self.score}"


if __name__ == '__main__':
    tomek = Player("Tomek")
    print(tomek)

    tomek.lives -= 1
    print(tomek)
    tomek.lives -= 1
    print(tomek)
    tomek.lives -= 1
    print(tomek)
    tomek.lives -= 1
    print(tomek)
    tomek.lives -= 1
    print(tomek)
