#!/usr/bin/env python
__author__ = 'Ruben9922'
__project__ = "ConsoleUtilities"


def input_int(message):
    input_valid = False
    while not input_valid:
        try:
            number = int(input(message))
            input_valid = True
            return number
        except ValueError as e:
            print("Integers only! ({0})".format(e))


def input_float(message):
    input_valid = False
    while not input_valid:
        try:
            number = float(input(message))
            input_valid = True
            return number
        except ValueError as e:
            print("Numbers only! Decimals are allowed. ({0})".format(e))


def input_option_char(valid_options, message="Enter option: "):
    option = ""
    input_valid = False
    while not input_valid:
        option = input(message).lower()
        for valid_option in valid_options:
            if option == valid_option:
                input_valid = True
                break
        if not input_valid:
            print("Invalid option!")
    return option


def input_option_int(titlelist, optioncount):
    for i in range(0, len(titlelist)):
        print("  {0}: {1}".format(i, titlelist[i]))
    while True:
        option = input_int("Enter option: ")
        if 0 <= option < optioncount:
            break
        else:
            print("Invalid option!")
    return option


def search_array(item, array):
    for i in range(len(array)):
        if item == array[i]:
            return i
    return -1
