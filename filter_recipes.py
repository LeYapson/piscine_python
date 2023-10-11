def filter_recipes(recipes, max_persons):
    return [recipe for recipe in recipes if recipe['persons'] <= max_persons]

