def print_line(char, times):
    print(char*times)


def print_lines(char, times, rows):
    row = 0
    while row < rows:
        print_line(char, times)
        row += 1


print_lines("-", 10, 50)
