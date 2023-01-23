"""
Library used for time calculations
"""
from typing import Literal

# Constants
UNITS = Literal["h", "m", "s"]


def convert_time(value: float, unit: UNITS, convert_to: UNITS) -> float:
    """
    Converts time to a different unit
    :param value: The amount of time
    :param unit: The current unit of time
    :param convert_to: The unit of time to convert to
    :return: The converted value of time as a float
    """
    if unit == convert_to:
        return value
    elif unit == "h":
        if convert_to == "m":
            return value * 60
        elif convert_to == "s":
            return value * 3600
    elif unit == "m":
        if convert_to == "h":
            return value / 60
        elif convert_to == "s":
            return value * 60
    elif unit == "s":
        if convert_to == "h":
            return value / 3600
        elif convert_to == "m":
            return value / 60


def add_time(value1: float, unit1: UNITS, value2: float, unit2: UNITS, unit_out: UNITS) -> float:
    """
    Adds the values of time together
    :param value1: The amount of time
    :param unit1: The unit of time
    :param value2: The amount of time to add
    :param unit2: The unit of time
    :param unit_out: The unit of time to return
    :return: The added time value as a float
    """
    # Convert values to output unit
    v1 = convert_time(value1, unit1, unit_out)
    v2 = convert_time(value2, unit2, unit_out)
    return v1 + v2


def subtract_time(value1: float, unit1: UNITS, value2: float, unit2: UNITS, unit_out: UNITS) -> float:
    """
    Subtracts the values of time from each other
    :param value1: The amount of time
    :param unit1: The unit of time
    :param value2: The amount of time to subtract
    :param unit2: The unit of time
    :param unit_out: The unit of time to return
    :return: The difference between time values as a float
    """
    # Convert values to output unit
    v1 = convert_time(value1, unit1, unit_out)
    v2 = convert_time(value2, unit2, unit_out)
    return v1 - v2


def multiply_time(value1: float, unit1: UNITS, value2: float, unit2: UNITS, unit_out: UNITS) -> float:
    """
    Multiplies the values of time together
    :param value1: The amount of time
    :param unit1: The unit of time
    :param value2: The amount of time to multiply by
    :param unit2: The unit of time
    :param unit_out: The unit of time to return
    :return: The multiplied time value as a float
    """
    # Convert values to output unit
    v1 = convert_time(value1, unit1, unit_out)
    v2 = convert_time(value2, unit2, unit_out)
    return v1 * v2


def divide_time(value1: float, unit1: UNITS, value2: float, unit2: UNITS, unit_out: UNITS) -> float:
    """
    Divides the values of time
    :param value1: The amount of time
    :param unit1: The unit of time
    :param value2: The amount of time to divide by
    :param unit2: The unit of time
    :param unit_out: The unit of time to return
    :return: The divided time value as a float
    """
    # Convert values to output unit
    v1 = convert_time(value1, unit1, unit_out)
    v2 = convert_time(value2, unit2, unit_out)
    return v1 / v2


def simplify_time(total_hours: int, total_minutes: int, total_seconds: int) -> list:
    """
    Simplifies time into full minutes and hours
    :param total_hours:
    :param total_minutes:
    :param total_seconds:
    :return: A list containing the hours, minutes, and seconds in that order
    """
    hours = total_hours
    minutes = total_minutes
    seconds = total_seconds

    if seconds >= 60:
        minutes += int(convert_time(seconds, "s", "m"))
        seconds = round(convert_time((convert_time(seconds, "s", "m") % 1), "m", "s"))
    if minutes >= 60:
        hours += int(convert_time(minutes, "m", "h"))
        minutes = round(convert_time((convert_time(minutes, "m", "h") % 1), "h", "m"))

    return [hours, minutes, seconds]


def get_time_in_seconds(hours: int, minutes: int, seconds: int) -> float:
    """
    Converts the hours and minutes to seconds and adds the seconds
    :param hours:
    :param minutes:
    :param seconds:
    :return: The provided time in seconds
    """
    return convert_time(hours, "h", "s") + convert_time(minutes, "m", "s") + seconds

