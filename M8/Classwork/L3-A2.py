class student:
    grade = 8
    name = "Priyanshu"
    #method1
    def introduction(self):
       print("Hi I am a student")
    #method2
    def details(self):
        print("My name is", self.name)
        print("I am in grade", self.grade)
ob = student()
ob.introduction()
ob.details()