# Introducing Priyanshu using OOP Concepts

class Person:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def introduce(self):
        print(f"👋 Hi, my name is {self.name}.")
        print(f"I am {self.age} years old.")
        print(f"My profession is {self.profession}.")

    def hobby(self, hobby_name):
        print(f"In my free time, I enjoy {hobby_name}.")


# Create an object of Person class for Priyanshu
person1 = Person("Priyanshu", 22, "Software Developer")  # change age/profession as per you

# Introduce Priyanshu
person1.introduce()

# Show hobby
person1.hobby("coding and playing cricket")