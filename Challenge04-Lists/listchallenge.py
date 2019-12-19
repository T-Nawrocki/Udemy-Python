# using the menu below, create a program that finds meals without spam, then prints the ingredients of the meal

menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "spam", "spam", "egg", "spam"],
    ["spam", "spam", "spam", "spam", "spam", "spam", "baked beans", "spam", "spam", "spam", "spam"],
    ["Lobster Thermidor aux crevettes with a Mornay sauce, garnished with truffle pâté, brandy and a fried egg on top",
     "spam"]
]

for meal in menu:
    if "spam" not in meal:
        print("Well I suppose you could have", end= " ")
        for ingredient in meal:
            if meal.index(ingredient) == len(meal) - 2:  # adds penultimate "and" separator. - 2 because index from 0
                print(ingredient, end=" and ")
            else:
                print(ingredient, end=", ")
        print("but it's not quite the same without the spam.")
