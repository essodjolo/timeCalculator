import re

# Assumptions and constrains:
#   Assume that the start times are valid times.
#   The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.

days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


def get_following_day(day_of_week: str) -> str:
    match day_of_week:
        case "monday":
            return "tuesday"
        case "tuesday":
            return "wednesday"
        case "wednesday":
            return "thursday"
        case "thursday":
            return "friday"
        case "friday":
            return "saturday"
        case "saturday":
            return "sunday"
        case "sunday":
            return "monday"


def format_output_time(time: str, number_of_days: int, starting_day_of_the_week: str) -> str:
    new_day = starting_day_of_the_week

    # To get the new day, we divide the number of days by 7 and use the remainder to find the new day.
    # Example: if number of days = 10, we will only go to the third following day to get the new day.
    for i in range(number_of_days % 7):
        new_day = get_following_day(new_day)

    # Return output following the pattern given in the exercise
    output = time

    if starting_day_of_the_week in days_of_week:
        output += ", " + new_day.title()

    if number_of_days == 1:
        output += " (next day)"
    elif number_of_days > 1:
        output += " (" + str(number_of_days) + " days later)"

    return output


def convert_time_to_24h_format(time: str) -> str:
    hours_minutes_am_pm = time.split()
    hours_minutes = hours_minutes_am_pm[0]
    hours_minutes = hours_minutes.split(':')
    hours = hours_minutes[0]
    minutes = hours_minutes[1]
    am_pm = hours_minutes_am_pm[1].upper()

    # If the time is in AM, we return the same value while removing the AM part.
    # Else, we add 12 to the number of hours, and remove the PM part.
    # Special cases of 12 AM and 12 PM are handled according to the convention at
    # https://en.wikipedia.org/wiki/12-hour_clock: 12 AM denotes midnight and 12 PM denotes noon
    if am_pm == "AM":
        if hours == "12":  # 12 AM denotes midnight and 12 PM denotes noon
            hours = "00"
            return str.rjust(hours, 2, "0") + ":" + str.rjust(minutes, 2, "0")
        else:
            return str.rjust(hours, 2, "0") + ":" + str.rjust(minutes, 2, "0")
    else:
        # I'm not checking if it's PM, as we assume the format is correct and apart from AM we can only hav PM.
        if hours == "12":  # 12 AM denotes midnight and 12 PM denotes noon
            return str.rjust(hours, 2, "0") + ":" + str.rjust(minutes, 2, "0")
        else:
            hours = int(hours) + 12
            return str.rjust(str(hours), 2, "0") + ":" + str.rjust(minutes, 2, "0")


def convert_time_to_12h_format(time: str) -> str:
    hours_minutes = time.split(':')
    hours = hours_minutes[0]
    minutes = hours_minutes[1]

    # If the hour is < 12, we return the same value while adding the AM part.
    # Else, we return hours - 12 while adding the PM part.
    # Special cases of 12:00 and 00:00 are handled according to the convention at
    # https://en.wikipedia.org/wiki/12-hour_clock: 12 AM denotes midnight and 12 PM denotes noon
    hours = int(hours)
    if 0 < hours < 12:
        return str(hours) + ":" + str.rjust(minutes, 2, "0") + " AM"
    elif hours == 12:
        return str(hours) + ":" + str.rjust(minutes, 2, "0") + " PM"
    elif hours == 0:
        return "12:" + str.rjust(minutes, 2, "0") + " AM"
    else:
        # I'm not checking if it's PM, as we assume the format is correct and apart from AM we can only hav PM.
        hours -= 12
        return str(hours) + ":" + str.rjust(minutes, 2, "0") + " PM"


def add_time(
        start_time: str,
        duration_time: str,
        starting_day_of_the_week: str = ""
) -> str:

    # Make sure that starting_day_of_the_week is one of the expected values.
    starting_day_of_the_week = starting_day_of_the_week.lower()
    if starting_day_of_the_week != "" and starting_day_of_the_week not in days_of_week:
        return "Starting day of the week is incorrect."

    # Check the provided duration time
    duration_hours_minutes = duration_time.split(':')
    if len(duration_hours_minutes) == 2:
        duration_hours = duration_hours_minutes[0]
        duration_minutes = duration_hours_minutes[1]

        # Make we have numbers
        pattern = "[0-9]+"
        if re.fullmatch(pattern, duration_hours) is None or re.fullmatch(pattern, duration_minutes) is None:
            return "Duration time is incorrect."

        # Make sure the minutes in duration time are less than 60
        if int(duration_minutes) > 60:
            return "Duration time is incorrect."

        # Here lies the core logic of the function
        else:
            # As per instructions, we assume that the start time is valid.
            # So we are not checking, we simply proceed to parsing its value,
            # And go ahead with computing the time addition.

            start_time_hours_minutes = convert_time_to_24h_format(start_time).split(':')
            start_time_hours = start_time_hours_minutes[0]
            start_time_minutes = start_time_hours_minutes[1]
            total_hours = eval(start_time_hours + "+" + duration_hours)
            total_minutes = eval(start_time_minutes + "+" + duration_minutes)
            total_days = 0

            # If minutes >= 60, we divide its value by 60 to retrieve the number of hours (to be added to total_hours),
            # and keep the remainder will be the new value for the total_minutes.
            if total_minutes >= 60:
                (hours, minutes) = divmod(total_minutes, 60)
                total_hours += hours
                total_minutes = minutes

            # If total_hours > 24, we need to determine the number of days the time addition will take us to.
            # We compute quotient and remainder: the quotient determines the number of days,
            # and the remainder determines the number of minutes.
            if total_hours >= 24:
                (days, hours) = divmod(total_hours, 24)
                total_days += days
                total_hours = hours

            return format_output_time(
                convert_time_to_12h_format(str(total_hours) + ":" + str(total_minutes)),
                total_days,
                starting_day_of_the_week
            )

    else:
        return "Duration time is incorrect."
