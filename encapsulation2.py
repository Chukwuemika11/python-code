class Employee:
            def __init__(self, ID, name, salary):
                self.ID = ID
                self.name = name
                self.salary = salary

            def show(self):
                print(f'My name is: {self.name}')
                print(f'My staff ID is: {self.ID}')
                print(f'My salary is: {self.salary}')

        # Create an instance of Employee
emp = Employee('0001', 'Uju', 1000)

# Call the show method on the instance
emp.show()
 



