#!/usr/bin/python3

"""
Function that prints My name is <first name> <last name>
first_name must be string
last_name must be string
"""

def say_my_name(first_name, last_name=""):
    """
    Defining the function that prints my name
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
