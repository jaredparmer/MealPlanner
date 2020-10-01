class Amount:
    """ represents an amount of an Ingredient """
    # class attributes
    valid_units = ['g', 'cups', 'ml', 'tsp', 'tbsp', 'EL', 'TL', 'oz', 'fl oz']
    
    def __init__(self, value, unit):
        self.value = float(value)

        while not isinstance(unit, str) or unit not in self.valid_units:
            unit = input("Invalid unit of measure. Please enter 'g', 'cups',"
                  "'ml', 'tsp', 'tbsp', 'EL', 'TL', 'oz', or 'fl oz': ")
        self.unit = str(unit)


    def __str__(self):
        return f"{self.value} {self.unit}"

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


beans = Ingredient('beans', 'canned goods')
rice = Ingredient('rice', 'dry goods')
cumin = Ingredient('cumin', 'spices')
recipe = {beans: Amount(400, 'g'), rice: Amount(400, 'g'),
          cumin: Amount(1, 'EL')}

beans_and_rice = Meal('beans and rice', recipe)
print(beans_and_rice)

beans_and_rice.set_servings(2)
print(beans_and_rice)
