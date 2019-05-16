class Cat:
    def __init__(self, new_name):
        print("chishihua")
        self.name = new_name

    def eat(self):
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("%s爱喝水" % self.name)


tom = Cat("Tom")
print(tom.name)
tom.drink()
tom.eat()