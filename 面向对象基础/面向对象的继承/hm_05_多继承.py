class A:
    def test(self):
        print("这是A的test方法")

    def demo(self):
        print("这是A的demo")

class B:
    def demo(self):
        print("这是B...demo")

    def test(self):
        print("这是B的test")


class C(B, A):
    pass


c = C()
c.demo()
c.test()