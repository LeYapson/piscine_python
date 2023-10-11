import argparse
import datetime as dt
import json
from menu import build_menu, save_menu
from filter_recipes import filter_recipes
from sort_list import sort_recipes


def main():
    # Define and parse command-line arguments
    parser = argparse.ArgumentParser(description="Generate a menu based on recipes data.")
    parser.add_argument("-s", "--start", type=str, help="Start date in 'dd/mm/yyyy' format", required=True)
    parser.add_argument("-p", "--max-persons", type=int, default=4, help="Maximum number of persons (default: 4)")
    args = parser.parse_args()

    # Read recipes data from recipes_data.json
    with open("recipes_data.json", "r", encoding="utf-8") as file:
        recipes = json.load(file)

    # Sort recipes by title
    recipes = sort_recipes(recipes, 'title')

    # Filter recipes based on the maximum number of persons
    filtered_recipes = filter_recipes(recipes, args.max_persons)
    print(filtered_recipes)
    for recipe in filtered_recipes:
        if isinstance(recipe, dict):
            print(recipe)
        else:
            print(f"Invalid recipe: {recipe}")

    # Get the current week's dates
    start_date = dt.datetime.strptime(args.start, "%d/%m/%Y").date()
    # Get the current week's dates
    week_dates = [start_date + dt.timedelta(days=i) for i in range(7)]
    print(start_date)  # Vérifiez que start_date est correcte.
    print(week_dates)  # Vérifiez que week_dates contient les 7 dates de la semaine.

    # Create the menu and write it to menu.txt
    menu = build_menu(filtered_recipes, week_dates)
    save_menu(menu)


if __name__ == "__main__":
    main()
