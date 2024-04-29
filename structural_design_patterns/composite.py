# Component interface
class Department:
    def __init__(self, name):
        """
        Initialize a new Department object with the given name.

        Args:
            name (str): The name of the department.
        """
        self.name = name

    def add(self, department):
        """
        Add a department or employee to this department.

        Args:
            department (Department): The department or employee to add.
        """
        pass

    def remove(self, department):
        """
        Remove a department or employee from this department.

        Args:
            department (Department): The department or employee to remove.
        """
        pass

    def display(self, depth=0):
        """
        Display the name of this department and its sub-departments or employees.

        Args:
            depth (int): The depth of nesting for indentation.
        """
        pass


# Leaf: Individual Employee
class Employee(Department):
    def display(self, depth=0):
        print("  " * depth, f"Employee: {self.name}")


# Composite: Department
class CompanyDepartment(Department):
    def __init__(self, name):
        super().__init__(name)
        self.sub_departments = []

    def add(self, department):
        self.sub_departments.append(department)

    def remove(self, department):
        self.sub_departments.remove(department)

    def display(self, depth=0):
        print("  " * depth, f"Department: {self.name}")
        for department in self.sub_departments:
            department.display(depth + 1)


# Example usage
engineering_dept = CompanyDepartment("Engineering")

dev_team = CompanyDepartment("Development Team")
dev_team.add(Employee("John"))
dev_team.add(Employee("Alice"))
engineering_dept.add(dev_team)

qa_team = CompanyDepartment("QA Team")
qa_team.add(Employee("Bob"))
qa_team.add(Employee("Carol"))
engineering_dept.add(qa_team)

marketing_dept = CompanyDepartment("Marketing")
marketing_dept.add(Employee("David"))

company = CompanyDepartment("Company")
company.add(engineering_dept)
company.add(marketing_dept)

# Displaying the company structure
company.display()
