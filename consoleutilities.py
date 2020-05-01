def input_int(prompt, error_message="Integers only."):
    input_valid = False
    while not input_valid:
        try:
            number = int(input(prompt))
            input_valid = True
            return number
        except ValueError:
            print(error_message)


def input_float(prompt, error_message="Real numbers only."):
    input_valid = False
    while not input_valid:
        try:
            number = float(input(prompt))
            input_valid = True
            return number
        except ValueError:
            print(error_message)


def input_option_char(valid_options, prompt="Choose option: ", error_message="Invalid option."):
    option = ""
    input_valid = False
    while not input_valid:
        option = input(prompt).lower()
        for valid_option in valid_options:
            if option == valid_option:
                input_valid = True
                break
        if not input_valid:
            print(error_message)
    return option


def input_option_int(options, prompt="Choose option: ", error_message="Invalid option."):
    for i in range(0, len(options)):
        print("  {0}: {1}".format(i, options[i]))
    while True:
        option = input_int(prompt)
        if 0 <= option < len(options):
            break
        else:
            print(error_message)
    return option


def input_y_or_n(prompt):
    return input(prompt).lower() == "y"
