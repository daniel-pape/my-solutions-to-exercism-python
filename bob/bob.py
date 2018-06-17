def hey(phrase: str):
    def phrase_is_question():
        return phrase.endswith("?")

    def phrase_is_yelled():
        return phrase.isupper()

    def phrase_is_yelled_question():
        return phrase_is_yelled() and phrase_is_question()

    def phrase_says_anything():
        return phrase.replace(" ", "") == ""

    phrase = (phrase
              .replace("\n", " ")
              .replace("\r", " ")
              .replace("\t", " ")
              .strip())

    if phrase_is_yelled_question():
        return "Calm down, I know what I'm doing!"
    elif phrase_is_question():
        return "Sure."
    elif phrase_is_yelled():
        return "Whoa, chill out!"
    elif phrase_says_anything():
        return "Fine. Be that way!"
    else:
        return "Whatever."
