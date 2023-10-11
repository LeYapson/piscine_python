import datetime
import json
import sys

from datetime_utils import format_date
from filter_recipes import filter_recipes
from menu import build_menu
from recipes import create_recipe
from sort_list import sort_recipes

def parse_arguments():
  """Parses the command line arguments.

  Returns:
    A tuple containing the start date and the maximum number of persons.
  """

  start_date = None
  max_persons = 4

  for arg in sys.argv:
    if arg in ["--start", "-s"]:
      start_date = datetime.datetime.strptime(sys.argv[sys.argv.index(arg) + 1], "%Y-%m-%d")
    elif arg in ["--max-persons", "-p"]:
      max_persons = int(sys.argv[sys.argv.index(arg) + 1])

  return start_date, max_persons

def generate_menu_from_recipes(recipes, start_date, max_persons):
  """Generates a menu from a list of recipes.

  Args:
    recipes: A list of recipes.
    start_date: The start date.
    max_persons: The maximum number of persons.

  Returns:
    A string containing the menu.
  """

  filtered_recipes = filter_recipes(recipes, max_persons)
  sorted_recipes = sort_recipes(filtered_recipes, key=lambda recipe: recipe["title"])

  menu = build_menu(start_date, sorted_recipes)

  return menu

def write_menu_to_file(menu, filename):
  """Writes a menu to a file.

  Args:
    menu: A string containing the menu.
    filename: The filename.
  """

  with open(filename, "w") as f:
    f.write(menu)

def main():
  """The main function."""

  start_date, max_persons = parse_arguments()

  recipes = create_recipe("recipes_data.json")

  menu = generate_menu_from_recipes(recipes, start_date, max_persons)

  write_menu_to_file(menu, "menu.txt")

if __name__ == "__main__":
  main()
