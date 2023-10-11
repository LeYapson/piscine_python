import json

def get_recipes(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            recipes_data = json.load(file)
        return recipes_data
    except FileNotFoundError:
        raise OSError(f"File '{file_name}' not found.")