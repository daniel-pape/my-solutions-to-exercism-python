from collections import deque


def decode(string):
    def generate_count_pairs_from(string):
        def take_while_is_digit(accumulator, tokens):
            next_token = tokens.popleft()

            if next_token.isdigit():
                accumulator += next_token
                return take_while_is_digit(accumulator, tokens)
            else:
                return accumulator, next_token

        tokens = deque(string)

        while tokens:
            current_token = tokens.popleft()

            if current_token.isdigit():
                current_token, next_token = take_while_is_digit(current_token, tokens)
                yield (next_token, current_token)
            else:
                yield (current_token, 1)

    count_pairs = generate_count_pairs_from(string)
    decoded_string = count_pairs_to_str(count_pairs, encode=False)

    return decoded_string


def count_pairs_to_str(pairs, encode=True):
    """
    :param encode: If `True` return the string representation
     for encoding; otherwise the one for decoding as specified by
     README.md.
    """

    def count_pair_to_str(pair):
        token = pair[0]
        count = int(pair[1])

        if encode:
            if count == 1:
                return '{}'.format(token)
            else:
                return '{}{}'.format(pair[1], pair[0])
        else:
            return '{}'.format(count * token)

    result = ''.join(map(count_pair_to_str, pairs))

    return result


def encode(string):
    def generate_count_pairs_from(string):
        tokens = deque(string)

        last_token = None
        count = 0

        while tokens:
            current_token = tokens.popleft()

            if not last_token:
                last_token = current_token

            if current_token == last_token:
                count += 1
                if not tokens:
                    yield (last_token, count)
            else:
                yield (last_token, count)
                last_token = current_token
                count = 1
                if not tokens:
                    yield (last_token, count)

    count_pairs = generate_count_pairs_from(string)
    encoded_string = count_pairs_to_str(count_pairs)

    return encoded_string
