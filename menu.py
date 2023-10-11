import datetime as dt

def build_menu(recipes, start_date):
    menu = []
    current_date = start_date

    for recipe in recipes:
        menu.append((current_date, recipe['title']))
        current_date += dt.timedelta(days=1)

    return menu


def save_menu(meals):
    with open('menu.txt', 'w') as file:
        for date, recipe in meals:
            formatted_date = date.strftime("%A %d %B %Y")
            file.write(f"{formatted_date}: {recipe}\n")
