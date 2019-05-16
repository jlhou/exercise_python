def print_line(char, times):
    print(char*times)


name = "hm"


def print_lines(char, times, rows):
    row = 0
    while row < rows:
        print_line(char, times)
        row += 1
