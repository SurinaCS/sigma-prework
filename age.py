import datetime


def age_calc():
    """
    Function to calculate age given user inputted date.
    RETURNS:
    age (int) - difference between todays date and inputted date in years.
    """
    today = datetime.date.today()
    given = input("Enter a date in the format DD-MM-YYYY: ")

    # parsing input into datetime object, returning only date part of it
    date = datetime.datetime.strptime(given, '%d-%m-%Y').date()

    age = today.year - date.year
    # account for where we are in the current year
    if (today.month, today.day) < (date.month, date.day):
        age -= 1

    return print(age)


age_calc()
