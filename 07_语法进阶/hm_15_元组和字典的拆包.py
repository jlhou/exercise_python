def demo(*args, **kwargs):
    print(args)
    print(kwargs)


gl_num = (1, 2, 3)
gl_dict = {"name": "xiaoming", "age": 18}

demo(*gl_num, **gl_dict)