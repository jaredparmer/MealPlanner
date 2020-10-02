class Amount:
    """ represents an amount of an Ingredient """
    # class attributes
    valid_units = ['g', 'cups', 'ml', 'tsp', 'tbsp', 'EL', 'TL', 'oz', 'fl oz',
                   'ea', 'can']
    
    def __init__(self, quantity, unit):
        self.quantity = float(quantity)
        self.unit = str(unit)


    def __str__(self):
        return f"{self.quantity} {self.unit}"

    # conversion functions TBD


class Ingredient:
    """ represents an ingredient """
    def __init__(self, name, location='', synonyms=[]):
        self.name = str(name)
        self.location = str(location)
        self.synonyms = []
        for element in synonyms:
            self.synonyms.append(str(element))


    def __str__(self):
        result = f"{self.name}, found in {self.location} "
        if self.synonyms:
            result += "aka:\n\t" + ', '.join(self.synonyms)
        return result


class Meal:
    """ represents a single meal, including recipe """
    def __init__(self, name, recipe={}, servings=1):
        self.name = str(name)
        self.recipe = dict(recipe)
        self.servings = int(servings)


    def __str__(self):
        result = f"{self.name}, {self.servings} servings: \n"
        for ingredient in self.recipe.keys():
            result += f"\t {ingredient.name}, {self.recipe[ingredient]} \n"
        return result


    def set_servings(self, servings):
        self.servings = int(servings)
        for ingredient in self.recipe.keys():
            new_amt = Amount(self.recipe[ingredient].value * servings,
                             self.recipe[ingredient].unit)
            self.recipe[ingredient] = new_amt


def load_recipes(filename='recipes.txt'):
    meals = {}
    with open(filename) as fin:
        line = fin.readline().strip('\n')
        print(f"first line read: '{line}'")
        while line != "":
            if line == '***':
                # beginning a new recipe; skip marker, grab name and servings
                name = fin.readline().strip('\n')
                print(f"just read: {name}")
                portions = fin.readline().strip('\n').split(' ')[0]
                print(f"just read: {portions}")
                meals[name] = Meal(name, recipe={}, servings=portions)
                #print("hardcore:")
                #print(Meal(name, servings=portions))
                print(f"Storing:")
                print(meals[name])

            # read ingredients in
            line = fin.readline().strip('\n')
            print(f"just read: {line}")
            contents = line.split()
            print(f"split up: {contents}")
            if is_number(contents[0]):
                # amount of ingredient is given
                quantity = contents[0]
                unit = contents[1]
                ingredient_name = ' '.join(contents[2:])
            else:
                quantity = 0.0
                unit = '-'
                ingredient_name = ' '.join(contents)

            print(f"ingredient_name: {ingredient_name}")
            print("Meal item before loading Amount:")
            print(meals[name])
            print("Meal item recipe:")
            print(meals[name].recipe)
            new_ingredient = Ingredient(ingredient_name)
            meals[name].recipe[new_ingredient] = Amount(quantity, unit)
            print("Meal item recipe after load attempt:")
            print(meals[name].recipe)
            print("Storing:")
            print(meals[name])
                
    return meals


def is_number(string):
    """ checks whether string is integer or float """
    try:
        float(string)
        return True
    except ValueError:
        return False


meals = load_recipes()
print("RECIPES:")
for item in meals.keys():
    print(meals[item])
