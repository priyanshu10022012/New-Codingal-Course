from abc import ABC, abstractmethod
class animal(ABC):
    @abstractmethod
    def move(self):
        pass    
class Human(animal):
    def move(self):
        print("I can walk and run")
class Snake(animal):
    def move(self):
        print("I can crawl")
class Dog(animal):
    def move(self):
        print("I can bark")
class Lion(animal):
    def move(self):
        print("I can roar")
H = Human()
H.move()
S = Snake()
S.move()
D = Dog()
D.move()
L = Lion()
L.move()
