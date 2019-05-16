class Women:
    def __init__(self, name):
        self.name = name
        self.age = 18

    def secret(self):
        print("%s的年龄是%d" % (self.name, self.age))


xm = Women("xm")
print(xm.age)
print(xm.name)
xm.secret()
