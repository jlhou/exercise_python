class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("nfdjk")


class B(A):

    def demo(self):
        print(self.__num2)
        self.__test()

c = B()
print(c)
