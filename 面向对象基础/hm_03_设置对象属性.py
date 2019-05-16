class Cat:

    def eat(self):
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("%s爱喝水" % self.name)


tom = Cat()
tom.name = "Tom"
tom.drink()
tom.eat()
