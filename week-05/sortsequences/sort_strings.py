from datastubs import STRING_LIST


def reverse_alpha():
    """
    return the list of strings sorted in
    reverse alphabetical order.
    """

    return sorted(STRING_LIST, reverse=True)


def alpha_case_insensitive():
    """
    return the list of strings sorted in
    alphabetical order, but without regard to
    capitalization
    """
    def get_lower_case(s):
        return s.lower()
    return sorted(STRING_LIST, key=get_lower_case)


def by_longest_length():
    """
    Sort in descending order of length of strings
    """
    def get_len(s):
        return len(s)
    return sorted(STRING_LIST, key=get_len, reverse=True)

def build_numstr_list():
    return [i for i in STRING_LIST if i.isdigit()]

def filter_and_sort_number_strings():
    """
    Filter the original list for strings that
    contain numbers. Then sort that list of number
    strings but as strings (i.e. alphabetical order)
    """
    numstr_list = build_numstr_list()
    return sorted(numstr_list)


def filter_and_sort_number_strings_as_numbers():
    """
    Filter the list for strings that contain numbers
    and then sort that list of strings in *numerical* order
    """
    numstr_list = build_numstr_list()
    return sorted(numstr_list, key=int)


