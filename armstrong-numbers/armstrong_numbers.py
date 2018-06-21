def is_armstrong(number):
    digits = [int(s) for s in list(str(number))]
    n = len(digits)
    armstrong_sum = sum([d**n for d in digits])

    return armstrong_sum == number


