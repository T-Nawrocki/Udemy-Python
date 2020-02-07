# This is a version of "7-getters_and_setters.py" which uses the property decorator
# rather than property function to define properties (see the score property of Player, in particular)


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
        self._score = 0
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

    @property  # getter methods use the @property decorator
    def score(self):
        return self._score

    @score.setter  # setter methods use @{property}.setter decorator, and must come after the getter is defined
    def score(self, score):
        self._score = score

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
    tomek.score = 500
    print(tomek)
