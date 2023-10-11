def filter_recipes(recipes, max_persons):
    return [recipe['title'] for recipe in recipes if recipe['persons'] <= max_persons]
