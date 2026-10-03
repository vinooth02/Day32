class Employee:

    company = "ABC Technologies"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", Employee.company)

    @staticmethod
    def check_salary(salary):
        if salary >= 30000:
            return "Good salary"
        else:
            return "Low salary"