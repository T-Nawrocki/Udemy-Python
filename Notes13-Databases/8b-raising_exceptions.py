# naming convention for these notes doesn't work well for importing as a module,
# so 8a-raising_exceptions has been duplicated in ducks.py
import ducks

# created a bunch of ducks and a penguin, plus a flock
flock = ducks.Flock()
donald = ducks.Duck()
daisy = ducks.Duck()
daffy = ducks.Duck()
pingu = ducks.Penguin()

# added all the birds to the flock, including the penguin
flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(pingu)  # gives a warning because we set a type hint for add_duck
flock.add_duck(daffy)

# this causes an error, because penguin objects do not have a fly method
# all the ducks successfully fly, but when we hit pingu, we can't fly and the exception crashes the program
flock.migrate()
