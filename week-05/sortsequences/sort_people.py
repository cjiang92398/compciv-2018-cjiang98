from datastubs import PEOPLE_LIST

def longest_name():
    """
    sort by length of name in descending order
    """
    def foolen(p): # nothing wrong with having a function inside a function
        return len(p['name'])
    return sorted(PEOPLE_LIST, key=foolen, reverse=True)

def get_age(p):
        return p['age']

def youngest():
    """
    sort by age in ascending order
    """
    return sorted(PEOPLE_LIST, key=get_age)


def oldest():
    """
    sort by age in descending order
    """
    return sorted(PEOPLE_LIST, key=get_age, reverse=True)


def name_reverse_alpha():
    """
    sort by name in descending order
    """
    def get_name(p):
        return p['name']
    return sorted(PEOPLE_LIST, key=get_name, reverse=True)


def country_then_age():
    """
    sort by country in ascending order
    in case of tie, sort by age
    """
    def get_country_or_name(p):
        return (p['country'], p['age'])
    return sorted(PEOPLE_LIST, key=get_country_or_name)