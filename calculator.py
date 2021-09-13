# calculator methods


def add(input1, input2):
    return input1 + input2


def sub(input1, input2):
    return input1 - input2


def mul(input1, input2):
    return input1 * input2


def div(input1, input2):
    if input2== 0:
        raise ZeroDivisionError("The divisor must not be zero")
    return input1 / input2


def mod(input1, input2):
    if input2 == 0:
        raise ZeroDivisionError("The divisor must not be zero")
    return input1 % input2
