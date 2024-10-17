import numbers
alter = 49

def check_numeric(x):
    if not isinstance(x, (int, float, complex)):
        raise ValueError('{0} is not numeric'.format(x))

check_numeric(input("in: "))
