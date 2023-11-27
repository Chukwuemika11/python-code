class Employee:
    def __init__(self, ID, name, salary):
        self.ID = ID
        self.name = name
        self.salary = salary

# Create an instance of Employee
emp = Employee('0001', 'uju', 1000)

# Access and print information about the instance
print(f'My name is: {emp.name}')
print(f'My staff ID is: {emp.ID}')
print(f'My salary is: {emp.salary}')
