class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):
    def bark(self):
        print(叫)


class Xiaotianquan(Dog):
    def fly(self):
        print("飞")


class Cat(Animal):
    def catch(self):
        print("抓老鼠")


wangcai = Xiaotianquan()
wangcai.run()
wangcai.fly()
