class Employee():
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.skills = args
        self.details = kwargs
    def show_employee(self):
        print(f'Employee: {self.name}')
        print(f'Employee: {self.skills}')
        print(f'Employee: {self.details}')
            

employee = Employee('Carlos', 'Python', 'SQL', 'Data visualization', age= 32, country= 'Colombia')
employee.show_employee()


    