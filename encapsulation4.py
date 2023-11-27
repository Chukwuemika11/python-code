class Employee:
    def __init__(self, ID, name, salary):
        self.__ID = ID
        self.name = name
        self.__salary = salary

# Create instances of Employee
emp = Employee('0001', 'uju', 1000)
emp1 = Employee('0002', 'chika', 5000)

# Access and print information about the instances
print(f'Name: {emp.name}, ID: {emp._Employee__ID}, Salary: {emp._Employee__salary}')
print(f'Name: {emp1.name}, ID: {emp1._Employee__ID}, Salary: {emp1._Employee__salary}')
