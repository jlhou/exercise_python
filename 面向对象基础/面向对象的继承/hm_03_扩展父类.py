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
        print("叫")


class Xiaotianquan(Dog):
    def fly(self):
        print("飞")

    def bark(self):
        #1.针对子类的特有需求，编写代码

        print("叫得和神一样")

        #2.使用super()．调用原本在父类中封装的方法
        super().bark()

        #3.增加其他子类代码
        print("GJKJL$%&*()")


wangcai = Xiaotianquan()
wangcai.bark()
