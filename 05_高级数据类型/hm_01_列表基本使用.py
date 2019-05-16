name_list = ["zhangsan", "lisi", "wangwu"]
temp_list = ["sunwuk", "zhubajie"]
#1.取值和索引
print(name_list[2])
print(name_list.index("lisi"))
#2.修改
name_list[1] = "李四"
# name_list[3] = "王小二"

#3.增加
name_list.append("王小儿")
name_list.insert(1, "小美")
name_list.extend(temp_list)

#4.删除
name_list.remove("wangwu")
name_list.pop()
name_list.pop(3)
name_list.clear()

print(name_list)