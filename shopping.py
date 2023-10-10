def remember_the_milk(shopping_list):
    if not shopping_list:
        return []

    if 'milk' not in shopping_list:
        shopping_list.append("milk")

    return shopping_list

def clean_list(shopping_list):
    if not shopping_list:
        return []

    # Add milk at the end of the list if missing.
    if "Milk" not in shopping_list:
        shopping_list.append("Milk")

    cleaned_list = []
    for index, item in enumerate(shopping_list):
        # Remove all spaces before and after.
        item = item.strip()

        # Capitalize the first letter.
        item = item.capitalize()
        # Add the index number and separator.
        cleaned_list.append(f"{index + 1}/ {item}")
    return cleaned_list