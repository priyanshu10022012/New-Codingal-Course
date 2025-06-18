class Parrot:
    # class atribute
    species = "bird"
    #instance atribute
    #constructor method - special method
    def __init__(self, name, age):
        self.name = name
        self.age = age
# instantiate the parrot class 
blu = Parrot("blu" , 10)
woo = Parrot("woo", 15)
# accesss the class attributes 
print("blu is a {}".format(blu.species))
print("woo is a {}".format(woo.species))
#access the instance attributes
print("blu is {} years old".format(blu.name, blu.age))
print("woo is {} years old".format(woo.name, woo.age))