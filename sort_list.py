def sort_recipes(recipes, by):
    if by not in ['title', 'persons']:
        raise ValueError("Invalid 'by' parameter. It must be 'title' or 'persons'.")

    return sorted(recipes, key=lambda x: x[by])
