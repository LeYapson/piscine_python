def day_from_number(day_number):
  """Converts a day number to a day word.

  Args:
    day_number: An integer representing the day number.

  Returns:
    A string representing the day word, or None if the day number is invalid.
  """

  day_names = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
  }

  if day_number not in day_names:
    return None

  return day_names[day_number]


def day_to_number(day):
  """Converts a day word to a day number.

  Args:
    day: A string representing the day word.

  Returns:
    An integer representing the day number, or None if the day word is invalid.
  """

  day_names = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7
  }

  if day not in day_names:
    return None

  return day_names[day]