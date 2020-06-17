class Employee:
    counter = 0
    total_salary = 0

    def __init__(self, name, family, salary, department):
        self.__name = name
        self.__family = family
        self.__salary = salary
        self.__department = department
        Employee.counter += 1
        Employee.total_salary += salary

    def __str__(self):
        return "Name: " + self.__name + "\nFamily name: " + self.__family + "\nSalary: " + str(self.__salary) + "\nDepartment: " + self.__department +"\n"

    @staticmethod
    def average_salary():
        return Employee.total_salary/Employee.counter


class FullTimeEmployee(Employee):
    def __init__(self,name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)


if __name__ == "__main__":
    e1 = Employee("John", "Smith", 100000, "CS")
    e2 = Employee("Cathy", "Wolf", 50000, "IT")
    e3 = Employee("Mark","Black", 75000, "HR")
    print(e1)
    print(e2)
    print(e3)

    fte = FullTimeEmployee("Alex", "Rolex", 200000, "DS")
    print(fte)

    print("Average salary of employees: ", Employee.average_salary())
    print("Counter of Employees : ", Employee.counter)
