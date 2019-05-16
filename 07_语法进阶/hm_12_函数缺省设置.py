def print_info(name, title="", gender=True):
    """

    :param title:
    :param name:班上同学的姓名
    :param gender: True男生　False女生
    """
    gender_test = "男生"
    if not gender:
        gender_test = "女生"
    print("[%s]%s是%s" % (title, name, gender_test))


print_info("xiaoming")