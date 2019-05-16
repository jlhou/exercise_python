def sum_numbers(*args):
    num = 0
    for i in args:
        num += i
    return num


print(sum_numbers(1, 2, 3))