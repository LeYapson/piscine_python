def create_recipe(name, persons, ingredients):
    # Check if title length is within the limit
    if len(name) > 150:
        raise ValueError("Title is too long")

    # Check if persons is null or greater than 50
    if persons is None or persons > 50 or persons == 0:
        raise ValueError("Invalid persons number")

    # Check if ingredients list is empty
    if not ingredients:
        raise ValueError("This recipe has no ingredients")

    recipe = {
        'title': name,
        'persons': persons,
        'ingredients': ingredients,
    }
    return recipe
