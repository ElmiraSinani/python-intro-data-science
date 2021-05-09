from Task_1_5_2_OOP_Money_Class import Money
from CustomExceptions import InvalidInputError


class Person:
    def __init__(self, name, surname, age, gender):
        try:
            if type(age) == str:
                raise InvalidInputError("Age can't be string")
            if age < 0:
                raise InvalidInputError("Negative Value is not acceptable for aga")
            if type(name) != str or type(surname) != str or type(gender) != str:
                raise InvalidInputError("Name/Surname/Gender must be string")
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)
        else:
            self.__name = str(name)
            self.__surname = str(surname)
            self.__gender = str(gender)
            self.__age = int(age)

    def __repr__(self):
        try:
            return self.__name + " " + self.__surname + " - " + self.__gender + ", " + str(self.__age) + " years old."
        except AttributeError:
            print("Type Error")


class Student(Person):
    def __init__(self, name, surname, age, gender, university, faculty, course, middle_score):
        super().__init__(name, surname, age, gender)
        self.__university = str(university)
        self.__faculty = str(faculty)
        self.__course = str(course)
        self.__middle_score = str(middle_score)

    def __repr__(self):
        val = ""
        try:
            val = "Student: " + super().__repr__()
            val += " University: " + self.__university + "; Faculty: " + self.__faculty + "; "
            val += "Course: " + self.__course + "; Mid Score: " + self.__middle_score
        except TypeError:
            print("Type Error")
        return val

    def get_score(self):
        return self.__middle_score

    def set_score(self, val):
        try:
            if type(self.__middle_score) == int or type(self.__middle_score) == float:
                self.__middle_score = val
            else:
                raise InvalidInputError("Invalid input")
        except InvalidInputError:
            print("Score value must be number")

    def get_course(self):
        return self.__course

    def set_course(self, val):
        try:
            if type(self.__course) == int:
                self.__course = val
            else:
                raise InvalidInputError("Invalid input")
        except InvalidInputError:
            print("Course value must be number")

    def get_faculty(self):
        return self.__faculty

    def set_faculty(self, val):
        try:
            if type(self.__faculty) == str:
                self.__faculty = val
            else:
                raise InvalidInputError("Invalid input")
        except InvalidInputError:
            print("Faculty value must be string")

    def get_university(self):
        return self.__university

    def set_university(self, val):
        try:
            if type(self.__university) == str:
                self.__university = val
            else:
                raise InvalidInputError("Invalid input")
        except InvalidInputError:
            print("University value must be string")


class Teacher(Person):
    def __init__(self, name, surname, age, gender, university, faculty, discipline, experience, salary):
        super().__init__(name, surname, age, gender)
        self.__university = str(university)
        self.__faculty = str(faculty)
        self.__discipline = str(discipline)
        self.__experience = str(experience) + " years"
        self.__salary = Money(salary, "USD")

    def __repr__(self):
        s = "Teacher: " + super().__repr__() + " "
        s += "University: " + self.__university + "; Faculty: " + self.__faculty + "; "
        s += "Discipline: " + self.__discipline + "; Experience: " + self.__experience + "; "
        s += "Salary: " + str(self.__salary)
        return s

    def get_university(self):
        return self.__university

    def set_university(self, val):
        if type(self.__university) == str:
            self.__university = val

    def get_faculty(self):
        return self.__faculty

    def set_faculty(self, val):
        if type(self.__faculty) == str:
            self.__faculty = val

    def get_discipline(self):
        return self.__discipline

    def set_discipline(self, val):
        if type(self.__discipline) == str:
            self.__discipline = val

    def get_experience(self):
        return self.__experience

    def set_experience(self, val):
        if type(self.__experience) == int or type(self.__experience) == float:
            self.__experience = val

    def get_salary(self):
        return self.__salary

    def set_salary(self, val):
        if type(self.__salary) == int or type(self.__salary) == float:
            self.__salary = val

# s = Student("John", 12, 15, "Male", "UCLA", "Business Management", "Project Coordinator", 178)
#print(s)
t = Teacher("Mari", "Brown", 48, "Female", "Cambridge", "Natural and applied sciences", "Biology", 15, 200000)

print(t)
