# Function to roll call the dwarves
def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves, start=1):
        print(f"{i}. {dwarf}")

# Function to summon Captain Planet
def summon_captain_planet(planeteer_calls):
    # Use list comprehension to capitalize and add an exclamation point
    return [call.capitalize() + '!' for call in planeteer_calls]

# Function to check if any calls are longer than four characters
def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

# Function to find the first cheese in a list of ingredients
def find_the_cheese(ingredients):
    cheeses = ["cheddar", "gouda", "camembert"]
    for ingredient in ingredients:
        if ingredient in cheeses:
            return ingredient
    return None
