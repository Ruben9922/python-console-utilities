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
