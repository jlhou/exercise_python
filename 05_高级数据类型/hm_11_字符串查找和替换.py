hello_str = "hello world"
#1.判断是否以指定单词开始
print(hello_str.startswith("hello"))
#2.判断是否以指定单词结束
print(hello_str.endswith("ld"))
#3.查找指定字符串
print(hello_str.find("llo"))
print(hello_str.find("abc"))
#4.替换字符串
print(hello_str.replace("world", "python"))
