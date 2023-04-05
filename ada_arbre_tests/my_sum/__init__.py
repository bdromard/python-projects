def sum(arg):
    total = 0
    for val in arg:
        if type(arg) == list:
            total += arg[val - 1]
        else:
            total += arg
    return total