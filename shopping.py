def remember_the_milk(shopping_list):
    if not shopping_list:
        return []

    if 'milk' not in shopping_list:
        shopping_list.append("milk")

    return shopping_list