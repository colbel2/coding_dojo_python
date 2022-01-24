class Employee():
    #every class created needs an initialization method. Special method called when uses an "isntance of a class" or an object of the type.
    def __init__(self, f_name, l_name, starting_salary, m_name = None):
    #every method requires (self, ) then a parameter
        self.first_name = f_name
        self.middle_name = m_name
        self.last_name = l_name
        self.salary = starting_salary

    def full_name(self):
        if self.middle_name is not None:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.last_name}"

new_employee = Employee('Mark', 'John', 'Adams', 80000)
new_employee_2 = Employee('Sarah', 'Connor', 'Smith', 78000)
new_employee_3 = Employee('Adam', 'Bart', 'Jones', 61000)
new_employee_4 = Employee('Melissa', None, 'Hart-Smith', 55000)

employees = [new_employee, new_employee_2, new_employee_3, new_employee_4]

# for employee in employees: #when establishing a for loop the variable use (in this case employee) is arbitrary. A variable that means something and is understandable is best. In this example, employee is the variable and it could have been anything ex) x, e, lexi, etc...
#     print(f"{employee.first_name} {employee.last_name}")

# #DRY Dont Repeat Yourself

for employee in employees:
    print(f"{employee.full_name()}")