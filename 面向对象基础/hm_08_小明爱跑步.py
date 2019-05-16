class Person:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我是%s,体重%.2f" % (self.name, self.weight)

    def run(self):
        self.weight -= 0.5
        print("%s爱跑步, 跑步锻炼身体,体重%.2f" % (self.name, self.weight))

    def eat(self):
        self.weight += 1
        print("%s爱吃东西, ,体重%.2f" % (self.name, self.weight))


kevin = Person("kevin", 75.0)
print(kevin)
kevin.run()
kevin.eat()

jenny = Person("jenny", 45)
print(jenny)
jenny.run()
jenny.eat()