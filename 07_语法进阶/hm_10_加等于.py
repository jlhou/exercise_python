def demo(num, num_list):
    print("函数开始")
    num += num
    num_list += num_list
    print(num)
    print(num_list)
    print("函数结束")


gl_num = 9
gl_num_list = [1, 2, 3]
print(gl_num)
print(gl_num_list)
print(demo(gl_num, gl_num_list))