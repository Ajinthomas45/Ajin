class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person object for {self.name} is created.")

    def __del__(self):
        print(f"Person object for {self.name} is being destroyed.")


person1 = Person("hamshi", 22)
person2 = Person("shitha", 20)

del person1
del person2

