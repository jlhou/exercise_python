i = 0
while i < 10:
    if i == 3:
        #注意：在使用contiune这个关键字时一定要确认计数器是否已
        # 经修改，若无，则可能导致死循环
        i += 1
        continue
    print(i)
    i += 1