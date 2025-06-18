class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    
    def sleep(self):
        print(f"{self.name} is sleeping")

    def eat(self):
        print(f"{self.name} is eating")

class Cat(Animal):
    pass

class Dog(Animal):
    pass

class Mouse(Animal):
    pass

cat = Cat("Charlie")
dog = Dog("Bob")
mouse = Mouse("Alexander")

cat.eat()
dog.sleep()
mouse.eat()