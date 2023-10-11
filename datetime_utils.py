import datetime as dt

def parse_time(time_str: str) -> dt.datetime:
    # Parse the input string in the format "dd/mm/YYYY" into a datetime object.
    return dt.datetime.strptime(time_str, "%d/%m/%Y")

def format_date(date: dt.date) -> str:
    # Format the date object as "[english_weekday_name] [day_number] [english_month_name] [4_digits_year]"
    return date.strftime("%A %d %B %Y")
