card_list = [{"name": "zhangsan",
              "qq": 12345,
              "phone": 110},
             {"name": "lisi",
              "qq": 54321,
              "phone": 10086}]
for card_info in card_list:
    for k in card_info:
        print(k, card_info[k])