class calculate:
    def __init__(self,fname):
        self.fname = fname
    def __add__(self, other):
        return self.fname + other.fname
ob1 = calculate("hello ")
ob2 = calculate("world")
print(ob1 + ob2)