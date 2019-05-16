def sum_numbers(num):
    #出口
    if num == 1:
        return 1
    temp = sum_numbers(num-1)
    return num+temp

print(sum_numbers(3))