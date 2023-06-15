def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_value = roman_dict[roman_string[0]]
    output = prev_value

    for i in range(1, len(roman_string)):
        curr_value = roman_dict[roman_string[i]]

        if curr_value > prev_value:
            output += curr_value - 2 * prev_value
        else:
            output += curr_value

        prev_value = curr_value

    return output
