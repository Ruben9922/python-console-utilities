# TODO: Could look into types


def input_int(prompt=None, min_value=None, max_value=None, error_message=None, include_max=False):
    if max_value is not None and not include_max:
        max_value -= 1

    # Generate prompt and error messages if not provided
    if prompt is None:
        if min_value is None and max_value is None:
            suffix = ""
        else:
            min_value_string = str(min_value) if min_value is not None else ""
            max_value_string = str(max_value) if max_value is not None else ""

            suffix = f" [{min_value_string}..{max_value_string}]"
        prompt = f"Enter integer{suffix}: "
    if error_message is None:
        if min_value is not None and max_value is not None:
            error_message = f"Integers between {min_value} and {max_value} (inclusive) only."
        elif min_value is not None:
            error_message = f"Integers greater than or equal to {min_value} only."
        elif max_value is not None:
            error_message = f"Integers less than or equal to {max_value} only."
        else:
            error_message = "Integers only."

    while True:
        try:
            value = int(input(prompt))

            valid = (min_value is None or value >= min_value) and (max_value is None or value <= max_value)

            if valid:
                return value

            print(error_message)
        except ValueError:
            print(error_message)


def input_float(prompt=None, min_value=None, max_value=None, error_message=None, include_min=True, include_max=False):
    # Generate prompt and error messages if not provided
    if prompt is None:
        if min_value is None and max_value is None:
            suffix = ""
        else:
            interval_start_symbol = "[" if include_min else "("
            interval_end_symbol = "]" if include_max else ")"
            min_value_string = str(min_value) if min_value is not None else ""
            max_value_string = str(max_value) if max_value is not None else ""

            suffix = f" {interval_start_symbol}{min_value_string}..{max_value_string}{interval_end_symbol}"
        prompt = f"Enter real number{suffix}: "

        # if min_value is not None and max_value is not None:
        #
        # elif min_value is not None:
        #     prompt = f"Enter real number {}{min_value}..]: "
        # elif max_value is not None:
        #     prompt = f"Enter real number [..{max_value - 1}]: "
        # else:
        #     prompt = "Enter real number: "
    if error_message is None:
        if min_value is not None and max_value is not None:
            error_message = f"Real numbers between {min_value} ({'inclusive' if include_min else 'exclusive'}) and {max_value} ({'inclusive' if include_max else 'exclusive'}) only."
        elif min_value is not None:
            error_message = f"Real numbers greater than {'or equal to ' if include_min else ''}{min_value} only."
        elif max_value is not None:
            error_message = f"Real numbers less than {'or equal to ' if include_max else ''}{max_value} only."
        else:
            error_message = "Real numbers only."

    while True:
        try:
            value = float(input(prompt))

            min_condition = value >= min_value if include_min else value > min_value
            max_condition = value <= max_value if include_max else value < max_value
            valid = (min_value is None or min_condition) and (max_value is None or max_condition)
            # valid = (min_value is None or value >= min_value) and (max_value is None or value <= max_value) \
            #         and (include_max or value < max_value)

            if valid:
                return value

            print(error_message)
        except ValueError:
            print(error_message)


def input_option_char(options, chars, prompt=None, error_message=None, ignore_case=True):
    if ignore_case:
        chars = list(map(str.lower, chars))

    # Generate prompt and error messages if not provided
    if prompt is None:
        prompt = f"Enter option [{''.join(chars)}]: "
    if error_message is None:
        error_message = f"Only one of the following characters is allowed: {', '.join(chars)}."

    if len(options) != len(chars):
        raise ValueError("options and chars must be lists of the same length.")
    if len(chars) > len(set(chars)):
        raise ValueError("chars must contain distinct elements.")

    for option, char in zip(options, chars):
        print(f"[{char}]: {option}")

    while True:
        char = input(prompt)

        if ignore_case:
            char = char.lower()

        valid = char in chars
        if valid:
            return char
        print(error_message)


def input_option_int(options, prompt=None, error_message=None):
    for index, option in enumerate(options):
        print(f"[{index}]: {option}")
    return input_int(prompt, 0, len(options), error_message)


def input_boolean(prompt, default=False, error_message=None, true_string="y", false_string="n"):
    # Generate prompt if not provided
    prompt = f"{prompt} [{true_string.upper() if default == True else true_string.lower()}/{false_string.upper() if default == False else false_string.lower()}]: "

    if default is None:
        # Generate error message if not provided
        if error_message is None:
            error_message = f"Only \"{true_string}\" or \"{false_string}\" is allowed."

        while True:
            value = input(prompt).lower()
            if value == true_string:
                return True
            if value == false_string:
                return False
            print(error_message)
    elif default:  # If default is True
        return input(prompt).lower() != false_string
    else:
        return input(prompt).lower() == true_string
