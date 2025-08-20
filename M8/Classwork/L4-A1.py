class Employee:
    # Initializing (constructor)
    def __init__(self):
       print('Employee created')
    # deleting (destructor)
    def __del__(self):
       print('Employee deleted','destructor called.')
obj = Employee()  
del obj