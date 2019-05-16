#!/home/hjl/anaconda3/bin/python3
import card_tools
while True:
    # 名片显示页面
    card_tools.show_menu()
    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是［%s］" % action_str)
    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            card_tools.new_card()
        elif action_str == "2":
            card_tools.show_all_card()
        else:
            card_tools.search_card()
    elif action_str == "0":
        print("感谢您的使用，欢迎下次使用！")
        break
    else:
        print("您的输入有误！请重新输入")
