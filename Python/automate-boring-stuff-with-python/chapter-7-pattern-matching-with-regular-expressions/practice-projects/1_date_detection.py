# Date Detection, Automate the boring stuff on python, page number: 186

# Write a regular expression that can detect dates in the DD/MM/YYYY format.
# Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999.
# Note that if the day or month is a single digit, it’ll have a leading zero.
# The regular expression doesn’t have to detect correct days for each month or for leap years;
# it will accept nonexistent dates like 31/02/2020 or 31/04/2021.
# Then store these strings into variables named month, day, and year,
# and write additional code that can detect if it is a valid date.
# April, June, September, and November have 30 days, February has 28 days, and
# the rest of the months have 31 days. February has 29 days in leap years.
# Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400.
# Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.

import re


def valid_dates(text: str) -> list:
    """
    This function takes a string of text and returns a list of valid dates.
    """
    date_regex = re.compile(
        r"""
            ([0-3]\d)   # date
            /
            ([01]\d)    # month
            /
            ([0-2]\d{3})    # year
        """,
        re.VERBOSE,
    )

    matched_dates = date_regex.findall(text)
    print(matched_dates)

    # checking for valid dates
    for date in matched_dates:
        day, month, year = int(date[0]), int(date[1]), int(date[2])

        if day > 31 or month > 12 or year > 2999 or year < 1000:
            matched_dates.remove(date)

        elif month == 4 or month == 6 or month == 9 or month == 11:  # check for 30 days
            if day > 30:
                matched_dates.remove(date)

        # check for leap year, and remove if date is higher than 29
        elif (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
            if month == 2 and day > 29:
                matched_dates.remove(date)
        elif (
            month == 2 and day > 28
        ):  # check date for february and remove date if it is higher than 28
            matched_dates.remove(date)

    print(matched_dates)


if __name__ == "__main__":
    # valid_dates(
    #     "23/14/1765 west north 390)& in the  far vast 23/14/1765"
    # )
    valid_dates(
        "32/14/2002 west north 390)& in the  far 13/09/2362  33/06/2362   33/09/2522"
    )
