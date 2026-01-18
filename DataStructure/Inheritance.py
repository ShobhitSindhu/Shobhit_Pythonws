class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}"

class Coder(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def get_details(self):
        self.salary += 10000
        return f"{self.name}, Salary: {self.salary}, Language: {self.language}"

class Designer(Employee):
    def __init__(self, name, salary, tool):
        super().__init__(name, salary)
        self.tool = tool

    def get_details(self):
        self.salary += 5000
        return f"{self.name}, Salary: {self.salary}, Tool: {self.tool}"

employees = [
    Employee("Alice", 70000),
    Coder("Bob", 90000, "Python"),
    Designer("Charlie", 80000, "Photoshop")
]

for emp in employees:
    print(emp.get_details())
