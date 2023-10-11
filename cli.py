import argparse
from datetime_utils import format_date
from menu import build_menu
from filter_recipes import filter_recipes
from sort_list import sort_recipes
from read_recipes import get_recipes


def main():
    # Define and parse command-line arguments
    parser = argparse.ArgumentParser(description="Generate a menu based on recipes data.")
    parser.add_argument("-s", "--start", type=str, help="Start date in 'dd/mm/yyyy' format", required=True)
    parser.add_argument("-p", "--max-persons", type=int, default=4, help="Maximum number of persons (default: 4)")
    args = parser.parse_args()

    # Read recipes data from recipes_data.json
    recipes = get_recipes("recipes_data.json")

    # Sort recipes by title
    recipes = sort_recipes(recipes, 'title')

    # Get the current week's dates
    week_dates = format_date(args.start)

    # Filter recipes based on the maximum number of persons
    filtered_recipes = filter_recipes(recipes, args.max_persons)

    # Create the menu and write it to menu.txt
    build_menu(week_dates, filtered_recipes)


if __name__ == "__main__":
    main()
