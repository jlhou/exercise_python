card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用名片管理系统Ｖ1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")
    card_dict = {}
    name_str = input("请输入姓名")
    phone_str = input("请输入电话")
    qq_str = input("请输入qq")
    email_str = input("请输入email")
    card_dict = {"name": name_str, "phone": phone_str, "qq": qq_str, "email": email_str}
    card_list.append(card_dict)
    print(card_list)
    print("添加%s的用户信息成功" % name_str)


def show_all_card():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")
    print("=" * 50)
    for name in ["姓名", "电话", "qq", "email"]:
        print(name, end="\t\t")
    print("")
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))
    print("=" * 50)


def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
    find_name = input("请输入您要查找的用户")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            for name in ["姓名", "电话", "qq", "email"]:
                print(name, end="\t\t")
            print("")
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            deal_card_dict(card_dict)
            break
    else:
        print("您的输入有误，请重新输入！")


def deal_card_dict(find_dict):
    """处理名片信息

    :param find_dict: 查找到的名片
    """
    action_str = input("请选择您想进行的操作"
                       "[1]修改　[2]删除　[0]返回首页")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "修改姓名")
        find_dict["phone"] = input_card_info(find_dict["phone"], "修改电话")
        find_dict["qq"] = input_card_info(find_dict["qq"], "修改qq")
        find_dict["email"] = input_card_info(find_dict["email"], "修改email")
        print("修改完成")
    elif action_str == "2":
        card_list.remove(find_dict)


def input_card_info(dict_value, mes_tip):
    """　输入名片信息
    :param dict_value:字典中原有的值
    :param mes_tip:输入的提示信息
    :return:如果用户输入了内容，则返回内容，否则返回字典中原有的值
    """
    # 1.提示用户输入内容
    result_str = input(mes_tip)
    # 2.针对用户的输入进行判断，如果用户输入了内容，直接返回户结果
    if len(result_str) > 0:
        return result_str

    # 3.如果用户没有输入内容，返回原有的值
    else:
        return dict_value