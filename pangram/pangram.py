import string


def is_pangram(sentence: str):
    letters = string.ascii_lowercase
    sentence_lower = sentence.lower()

    checks = [(l in sentence_lower) for l in letters]

    return all(checks)
