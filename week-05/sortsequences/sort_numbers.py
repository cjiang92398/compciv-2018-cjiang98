from datastubs import NUMBER_LIST


def reverse_numerical_order():
    """
    Sort the list of numbers but in reverse order
    """
    return sorted(NUMBER_LIST, reverse=True)


def numerical_order():
    """
    Sort the list of numbers in numerical order
    """
    return sorted(NUMBER_LIST)

def as_absolute_value():
    """
    The absolute value of a number `n` is its value
    regardless of positive or negative sign
    """
    return sorted(NUMBER_LIST, key=abs)

def as_inverse_number():
    """
    An inverse of a number `n` is defined as: `1/n`
    The bigger the number, the smaller its inverse, and vice versa
    """
    def get_inv(n):
        return 1/n
    return sorted(NUMBER_LIST, key=get_inv)
