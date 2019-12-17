fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple":  "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage": "baby sauerkraut",
       "sprouts": "a vessel for onions and bacon",
       "broccoli": "small delicious trees"}

print(veg)

# .update() combines two dictionaries
veg.update(fruit)  # adds the elements of fruit to veg
print(veg)

# dictionary.update() doesn't return a new dictionary, it just performs an operation on the existing one
# just like how .sort() doesn't return anything
print(fruit.update(veg))

# to create a new dictionary that's a combination of the two, it's best to use .copy() on one
# and then .update() to include the rest
fruit_and_veg = fruit.copy()
fruit_and_veg.update(veg)
