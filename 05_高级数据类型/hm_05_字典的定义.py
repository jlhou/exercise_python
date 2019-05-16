xiaoming = {"name": "xiaoming",
            "age": 18,
            "gender": True,
            "weight": 75.5}
#1.取值
print(xiaoming["name"])

#2.增加/修改
xiaoming["height"] = 175
print(xiaoming)
xiaoming["name"] = "xiaoxiaoming"
print(xiaoming)
#3.删除
xiaoming.pop("name")
print(xiaoming)

temp_dict = {"height": 1.75,
             "age": 20}
xiaoming.update(temp_dict)
print(xiaoming)