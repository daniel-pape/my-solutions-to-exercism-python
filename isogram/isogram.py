def is_isogram(string: str):
    lowercase_string = string.lower()

    def is_okay(c: chr):
        is_special_char = c in " -"
        is_unique = (lowercase_string.count(c) == 1)

        return (is_special_char or is_unique)

    return all([is_okay(c) for c in lowercase_string])
