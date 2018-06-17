def word_count(phrase: str):
    def tokenize(phrase: str):
        INVALID_CHARS = ':!!&@$%^&.,_'

        for c in INVALID_CHARS:
            phrase = phrase.replace(c, ' ')

        splits = phrase.split()
        tokens = [s.lower().strip('\'') for s in splits]

        return tokens

    def count_tokens(tokens: list):
        keys = set(tokens)

        counts = dict([(key, 0) for key in keys])

        for t in tokens:
            counts[t] += 1

        return counts

    # def count_tokens_alt(tokens: list):
    #     counts = dict()
    #
    #     for t in tokens:
    #         counts[t] = counts.get(t, 0) + 1
    #
    #     return counts

    tokens = tokenize(phrase)
    result = count_tokens(tokens)

    return result
