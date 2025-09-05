class FileReadDemo:
    def __init__(self, filename):
        self.filename = filename

    def read_all(self):
        """Read entire file at once"""
        with open(self.filename, "r") as f:
            data = f.read()
        print("📖 Using read():\n", data)

    def read_line_by_line(self):
        """Read file line by line using readline()"""
        with open(self.filename, "r") as f:
            print("📖 Using readline():")
            line = f.readline()
            while line:
                print(line.strip())
                line = f.readline()

    def read_all_lines(self):
        """Read all lines into a list using readlines()"""
        with open(self.filename, "r") as f:
            lines = f.readlines()
        print("📖 Using readlines():")
        for line in lines:
            print(line.strip())

    def read_with_loop(self):
        """Read file directly in a for loop"""
        with open(self.filename, "r") as f:
            print("📖 Using for loop on file object:")
            for line in f:
                print(line.strip())


# Main Program
if __name__ == "__main__":
    # Create a sample file for demo
    with open("sample.txt", "w") as f:
        f.write("Line 1: Python File Handling\n")
        f.write("Line 2: Demonstration\n")
        f.write("Line 3: Reading Methods\n")

    demo = FileReadDemo("sample.txt")
    demo.read_all()
    demo.read_line_by_line()
    demo.read_all_lines()
    demo.read_with_loop()
