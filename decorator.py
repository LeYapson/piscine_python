# decorator.py
import datetime as dt

def with_current_date(function):
    def modified_function(*args, **kwargs):
        # Add the current_date parameter to the function
        current_date = dt.date.today()
        return function(*args, current_date=current_date, **kwargs)

    return modified_function
