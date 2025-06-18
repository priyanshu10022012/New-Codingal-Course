# Parent class Robot
class Robot:
    def __init__(self, name, model, owner="Priyanshu"):
        self.name = name
        self.model = model
        self.owner = owner

    def introduce(self):
        print(f"🤖 Hello! I am {self.name}, a {self.model} robot. I was created by {self.owner}.")

    def work(self):
        print(f"{self.name} is ready to work under {self.owner}'s command!")

# Child class HumanoidRobot inheriting from Robot
class HumanoidRobot(Robot):
    def __init__(self, name, model, language, owner="Priyanshu"):
        # Call parent constructor
        super().__init__(name, model, owner)
        self.language = language

    def introduce(self):
        # Method overriding
        print(f"🤖 Hi, I’m {self.name}. I’m a humanoid {self.model} robot, I speak {self.language}, and I belong to {self.owner}.")

    def dance(self):
        print(f"{self.name} is dancing 💃🕺 for {self.owner}!")

# Another Child class IndustrialRobot inheriting from Robot
class IndustrialRobot(Robot):
    def __init__(self, name, model, task, owner="Priyanshu"):
        super().__init__(name, model, owner)
        self.task = task

    def introduce(self):
        print(f"🤖 Greetings! I’m {self.name}, model {self.model}. My main task is {self.task}, and I proudly serve {self.owner}.")

    def perform_task(self):
        print(f"{self.name} is performing {self.task} ⚙️ under {self.owner}'s guidance.")


# Main program
if __name__ == "__main__":
    # Creating objects with owner Priyanshu
    r1 = HumanoidRobot("RoboSam", "XH-21", "English & Hindi", "Priyanshu")
    r2 = IndustrialRobot("WeldBot", "IR-77", "Welding in factories", "Priyanshu")

    # Introductions
    r1.introduce()
    r1.dance()
    r1.work()

    print("------------")

    r2.introduce()
    r2.perform_task()
    r2.work()