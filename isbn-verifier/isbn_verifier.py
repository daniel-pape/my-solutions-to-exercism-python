def verify(isbn: str):
    ISBN_LEN = 10
    DIGITS = '0123456789'

    def parse_start(isbn_start):
        parse_success = True
        parse_result = []

        for c in isbn_start:
            if c in DIGITS:
                parse_result.append(int(c))
            else:
                parse_success = False
                parse_result = None
                break

        return parse_success, parse_result

    def parse_end(isbn_end):
        parse_success = True
        parse_result = []

        if isbn_end == 'X':
            parse_result.append(10)
        elif isbn_end in DIGITS:
            parse_result.append(int(isbn_end))
        else:
            parse_success = False
            parse_result = None

        return parse_success, parse_result

    def compute_verification_sum(parse_result):
        weights = range(ISBN_LEN, 0, -1)
        take_product = lambda pair: pair[0] * pair[1]
        products = map(take_product, zip(parse_result, weights))
        verification_sum = sum(products)

        return verification_sum

    isbn = isbn.replace('-', '')

    if len(isbn) != ISBN_LEN:
        return False
    else:
        isbn_start = list(isbn[:-1])
        isbn_end = isbn[-1]

        parse_success_start, parse_result_start = parse_start(isbn_start)
        parse_success_end, parse_result_end = parse_end(isbn_end)

        if parse_success_start and parse_success_end:
            parse_result = parse_result_start + parse_result_end
            verification_sum = compute_verification_sum(parse_result)

            return (verification_sum % 11 == 0)
        else:
            return False
