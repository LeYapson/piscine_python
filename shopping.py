def remember_the_milk(shopping_list):
    if not shopping_list:
        return []

    if 'milk' not in shopping_list:
        shopping_list.append("milk")

    return shopping_list

def clean_list(shopping_list):
  """Cleans a list of strings by removing all spaces before and after, capitalizing the first letter, and adding an index number and separator before each item.

  Args:
    shopping_list: A list of strings.

  Returns:
    A list of strings with the cleaned items.
  """

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