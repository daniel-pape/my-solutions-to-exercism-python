def word_count(phrase: str):
    def tokenize(phrase: str):
        INVALID_CHARS = ':!!&@$%^&.,_'

        for c in INVALID_CHARS:
            phrase = phrase.replace(c, ' ')

        splits = phrase.split()
        tokens = [s.lower().strip('\'') for s in splits]

        return tokens

    def count_tokens(tokens: list):
        counts = dict()

        for t in tokens:
            counts[t] = counts.get(t, 0) + 1

        return counts

    tokens = tokenize(phrase)
    result = count_tokens(tokens)

    return result
