import datetime as dt

def build_menu(recipes, start_date):
    menu = []
    current_date = start_date

    for recipe in recipes:
        menu.append((current_date, recipe['title']))
        current_date += dt.timedelta(days=1)

    return menu
