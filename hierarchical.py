class A:
    def greet(self):
      print("hi")

class B(A):
    def welcome(self):
      print("welcome")

class C(A):
    def hi(self):
      print("hello")

obj = C()
obj.hi()
obj.greet()

obj1 = B()
obj1.welcome()
obj1.greet()

