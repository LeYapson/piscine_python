import argparse
import datetime as dt
import json
from menu import create_menu
from sort_list import sort_recipes_by_title
from filter_recipes import filter_recipes_by_max_persons

# Define the CLI parser
def create_cli_parser():
    parser = argparse.ArgumentParser(description="CLI tool for generating a menu.")
    parser.add_argument("--start", "-s", required=True, help="Start date (format: dd/mm/yyyy)")
    parser.add_argument("--max-persons", "-p", type=int, default=4, help="Maximum persons for recipes (default: 4)")
    return parser

def main():
    # Parse command line arguments
    parser = create_cli_parser()
    args = parser.parse_args()

    # Convert the start date argument to a datetime object
    start_date = dt.datetime.strptime(args.start, "%d/%m/%Y").date()

    # Load recipes data from recipes_data.json
    with open("recipes_data.json", "r") as file:
        recipes_data = json.load(file)

    # Sort recipes by title
    sorted_recipes = sort_recipes_by_title(recipes_data)

    # Filter recipes by maximum persons
    filtered_recipes = filter_recipes_by_max_persons(sorted_recipes, args.max_persons)

    # Create a menu and write it to menu.txt
    create_menu(start_date, filtered_recipes, "menu.txt")

if __name__ == "__main__":
    main()
