class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def display(self):
        print(self.firstname, self.lastname)
class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
x = student("Priyanshu", "choudhary", 2030)
x.display()
print(x.graduationyear)