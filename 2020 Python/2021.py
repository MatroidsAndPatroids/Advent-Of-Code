import utility # my own utility.pl file
import collections # OrderedDict

# Simulates the instructions
def allergenAssessment(instructions, part2 = False):
    # Parse data
    foods = []
    allergens = []
    ingredientSet = set()
    allergenSet = set()
    for line in instructions:
        food, allergen = line.split(' (contains ')
        food = set(food.split())
        allergen = allergen.split(', ')
        allergen[-1] = allergen[-1][:-1]
        foods += [food]
        allergens += [allergen]
        ingredientSet = ingredientSet.union(set(food))
        allergenSet = allergenSet.union(set(allergen))
    
    # Collect possible allergen -> ingredient pairs
    possibleIngredients = {}
    for allergen in allergenSet:
        possible = ingredientSet.copy()
        for x in range(len(foods)):
            if allergen in allergens[x]:
                possible = possible.intersection(foods[x])
        possibleIngredients[allergen] = possible
#     print(possibleIngredients)
    
    # Determine which ingredient dangerousIngredients which allergen
    uniqueIngredient = {}
    modified = True
    while modified:
        modified = False
        for allergen, ingredients1 in possibleIngredients.items():
            if len(ingredients1) == 1:
                modified = True
                ingredient = next(iter(ingredients1))
                uniqueIngredient[allergen] = ingredient
                
                for ingredients2 in possibleIngredients.values():
                    if ingredient in ingredients2:
                        ingredients2.remove(ingredient)
                break
#     print(uniqueIngredient)
    
    # Detemine safe ingredients and count how many times they appear in the food list
    dangerousIngredients = set(uniqueIngredient.values())
    safeIngredients = ingredientSet.difference(dangerousIngredients)
    safeIngredientCount = sum(len(food.intersection(safeIngredients)) for food in foods)
    
    # Sort dangerous ingredients by their allergens
    orderedByAllergen = collections.OrderedDict(sorted(uniqueIngredient.items()))
    canonicalDangerousIngredients = ','.join([v for k, v in orderedByAllergen.items()])
    
    print(canonicalDangerousIngredients) if part2 else print(safeIngredientCount)
    return canonicalDangerousIngredients if part2 else safeIngredientCount


# Check test cases
smallExample = """
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
""".strip().split('\n')
assert allergenAssessment(smallExample) == 5
assert allergenAssessment(smallExample, part2 = True) == 'mxmxvkd,sqjhc,fvjkl'

# Display info message
print("Give a list of food ingredients paired with allergens instructions:\n")
instructions = utility.readInputList()

# Display results
print(f'{allergenAssessment(instructions) = }')
print(f'{allergenAssessment(instructions, part2 = True) = }')