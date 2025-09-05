class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def write_file(self, content):
        with open(self.filename, "w") as f:
            f.write(content)
        print("✅ File written in 'w' mode (old content replaced).")

    def append_file(self, content):
        with open(self.filename, "a") as f:
            f.write(content)
        print("✅ Content appended in 'a' mode.")

    def read_file(self):
        with open(self.filename, "r") as f:
            data = f.read()
        print("📖 File content in 'r' mode:\n", data)

    def read_write_file(self):
        with open(self.filename, "r+") as f:
            print("📖 Before Writing:", f.read())
            f.seek(0)   # move to start
            f.write("New data added using r+ mode.\n")
        print("✅ Modified with 'r+' mode (read + write).")

    def write_read_file(self):
        with open(self.filename, "w+") as f:
            f.write("New content added using w+ mode.\n")
            f.seek(0)
            print("📖 After Writing:", f.read())

    def append_read_file(self):
        with open(self.filename, "a+") as f:
            f.write("Extra line using a+ mode.\n")
            f.seek(0)
            print("📖 After Appending:", f.read())


# Main Program
if __name__ == "__main__":
    handler = FileHandler("student_file.txt")

    # Step 1: Write
    handler.write_file("This is the first line.\n")

    # Step 2: Append
    handler.append_file("This is an appended line.\n")

    # Step 3: Read
    handler.read_file()

    # Step 4: Read + Write
    handler.read_write_file()

    # Step 5: Write + Read
    handler.write_read_file()

    # Step 6: Append + Read
    handler.append_read_file()
