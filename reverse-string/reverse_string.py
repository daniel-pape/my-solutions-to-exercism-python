def reverse(input=''):
    if not isinstance(input, str):
        msg = "Function `reverse(input)` requires string input; found type(ìnput)={}` instead.".format(type(input))
        raise Exception(msg)

    return input[::-1]