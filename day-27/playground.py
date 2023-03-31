def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

add(9, 5, 6, 4)


def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)