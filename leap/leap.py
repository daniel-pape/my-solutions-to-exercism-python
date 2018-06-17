from numbers import Integral

def is_leap_year(year):
    if not isinstance(year, Integral):
        raise Exception("Function `is_leap_year(year)` takes one integer argument but got `year={}".format(year))

    def is_evenly_divisible_by(divisor):
        return (year % divisor == 0)

    is_leap_candidate = is_evenly_divisible_by(4)
    is_century = is_evenly_divisible_by(100)
    is_special_century = is_evenly_divisible_by(400)

    result = (is_leap_candidate and
              not is_century or
              is_special_century)

    return result