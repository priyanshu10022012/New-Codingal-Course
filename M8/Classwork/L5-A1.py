# parent class
class person():
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class employee(person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        person.__init__(self, name, idnumber)
a = employee("Penguin", 12345, 50000, "Intern")
a.display()