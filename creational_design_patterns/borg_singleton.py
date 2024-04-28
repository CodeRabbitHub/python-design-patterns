class ClassRecord:
    _shared_state = {"class_name": None, "class_teacher": None, "class_students": []}

    def __init__(self, class_name, class_teacher):
        self.__dict__ = self._shared_state
        self.set_class_details(class_name, class_teacher)

    def set_class_details(self, class_name, class_teacher):
        self.class_name = class_name
        self.class_teacher = class_teacher

    def add_student(self, student_name):
        self.class_students.append(student_name)

    def get_class_details(self):
        return {
            "class_name": self.class_name,
            "class_teacher": self.class_teacher,
            "class_students": self.class_students,
        }


class Classroom(ClassRecord):
    def __init__(self, class_name, class_teacher):
        super().__init__(class_name, class_teacher)


# Let's test our Classroom class

# Creating the first instance of Classroom
class1 = Classroom("Grade 10", "Mr. Smith")
class1.add_student("Alice")
class1.add_student("Bob")

print("Class 1 Details:", class1.get_class_details())

# Trying to create another instance of Classroom
# This should not create a new instance but return the existing one
class2 = Classroom("Grade 11", "Ms. Johnson")
class2.add_student("Charlie")

print("Class 2 Details:", class2.get_class_details())  # Should be the same as class1
