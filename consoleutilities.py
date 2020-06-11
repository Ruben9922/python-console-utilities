"""
Note: As this library is still in version 0.y.z, keep in mind that the API may change at any time. See Item 4 of the
Semantic Versioning Specification: https://semver.org/#spec-item-4.
"""

from typing import Optional, List


def input_int(prompt: Optional[str] = None, min_value: Optional[int] = None, max_value: Optional[int] = None,
              error_message: Optional[str] = None, include_max: bool = False) -> int:
    """Allows the user to input an integer, possibly within a specified range.

    Specifically, this function prints the prompt, waits for the user to enter a value, and checks the value is valid
    (i.e. is a valid integer and in the specified range, if applicable). If valid, the value is returned; else, the
    error message is printed and this process is repeated until a valid value is entered. Hence, this function should
    only ever return a valid value.

    Args:
        prompt: Prompt message to print on waiting for input. Use `None` for the default prompt.
        min_value: Minimum value allowed. Inclusive. Use `None` if a minimum value is not required.
        max_value: Maximum value allowed. Inclusive if `include_max` is `True`; exclusive otherwise. Use `None` if a
            maximum value is not required.
        error_message: Error message to print after entering an invalid value.
        include_max: Specifies whether the `max_value` is inclusive. Use `True` for inclusive or `False` for exclusive.
    Returns:
        The valid integer value entered by the user.
    """

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


def input_float(prompt=None, min_value=None, max_value=None, error_message=None, include_min=True, include_max=False) \
        -> float:
    """Allows the user to input a float, possibly within a specified range.

    Specifically, this function prints the prompt, waits for the user to enter a value, and checks the value is valid
    (i.e. is a valid float and in the specified range, if applicable). If valid, the value is returned; else, the
    error message is printed and this process is repeated until a valid value is entered. Hence, this function should
    only ever return a valid value.

    Args:
        prompt: Prompt message to print on waiting for input. Use `None` for the default prompt.
        min_value: Minimum value allowed. Inclusive if `include_min` is `True`; exclusive otherwise. Use `None` if a
        minimum value is not required.
        max_value: Maximum value allowed. Inclusive if `include_max` is `True`; exclusive otherwise. Use `None` if a
            maximum value is not required.
        error_message: Error message to print after entering an invalid value.
        include_min: Specifies whether the `min_value` is inclusive. Use `True` for inclusive or `False` for exclusive.
        include_max: Specifies whether the `max_value` is inclusive. Use `True` for inclusive or `False` for exclusive.
    Returns:
        The valid float value entered by the user.
    """

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


def input_option_char(options: List[str], chars: List[str], prompt: str = None, error_message: str = None,
                      ignore_case: bool = True) -> str:
    """Allows the user to select from a list of options by entering a character.

    Specifically, this function does the following:

    #. Displays a list of option names with their associated characters
    #. Prints the prompt
    #. Waits for the user to enter a value
    #. Checks the value is valid (i.e. is a valid integer and in the specified range, if applicable).
    #. If valid, the value is returned; else, the error message is printed and this process is repeated until a valid
       value is entered. Hence, this function should only ever return a valid value.

    `options` and `chars` are expected to be lists of the same length. Additionally, `chars` must not contain
    duplicates, to avoid ambiguity. If `ignore_case` is `True` then case is also ignored when checking for duplicates.

    Args:
        options: List of option names. For example: `["Export to PDF", "Export to HTML"]`.
        chars: List of characters to associate with each option. For example: `["p", "h"]`.
        prompt: Prompt message to print on waiting for input. Use `None` for the default prompt.
        error_message: Error message to print after entering an invalid value.
        ignore_case: Specifies whether case should be ignored. If `True`, this also means that the characters in `chars`
            will be output in lower case to reduce confusion for the user. (To me, displaying some characters in upper
            case and some in lower case implies that case is not ignored.)

    Returns:
        The character corresponding to the selected option.

    Todo:
        * Replace the `options` and `chars` lists with a single list of objects.
    """

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


def input_option_int(options: List[str], prompt: Optional[str] = None, error_message: Optional[str] = None) -> int:
    """Allows the user to select from a list of options by entering the option's index.

    Specifically, this function does the following:

    #. Displays a list of option names with their indices
    #. Waits for the user to input an index (i.e. an integer between 0 and `len(options) - 1`) using `input_option_int`

    Args:
        options: List of option names. For example: `["Export to PDF", "Export to HTML"]`.
        prompt: Prompt message to print on waiting for input. Use `None` for the default prompt.
        error_message: Error message to print after entering an invalid value.

    Returns:
        The index of the selected option.
    """

    for index, option in enumerate(options):
        print(f"[{index}]: {option}")
    return input_int(prompt, 0, len(options), error_message)


def input_boolean(prompt: str, default: Optional[bool] = False, error_message: Optional[str] = None,
                  true_string: str = "y", false_string: str = "n") -> bool:
    """Allows the user to input a boolean.

    Specifically, this function does the following:

    #. Displays a list of option names with their indices
    #. Waits for the user to input an index (i.e. an integer between 0 and `len(options) - 1`) using `input_option_int`

    Args:
        prompt: Prompt message to print on waiting for input. Use `None` for the default prompt.
        default: Specifies the behaviour on entering an invalid value (i.e. a value other than `true_string` or
            `false_string`). If `True`, an invalid value will be considered `True`. If `False`, an invalid value will be
            considered `False`. If `None`, the user must enter either `true_string` or `false_string`---on entering an
            invalid value, the function will output the error message and loop until a valid value is entered.
        error_message: Error message to print after entering an invalid value.
        true_string: The string to be used to represent `True`.
        false_string: The string to be used to represent `False`.

    Returns:
        The boolean value entered by the user.
    """

    # Generate full prompt
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
