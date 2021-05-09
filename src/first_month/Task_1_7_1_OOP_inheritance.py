from Task_1_5_2_OOP_Money_Class import Money
from CustomExceptions import InvalidInputError


class Person:
    def __init__(self, name, surname, age, gender):
        try:
            if type(age) == str:
                raise InvalidInputError("Age can't be string", age)
            elif age < 0:
                raise InvalidInputError("Negative Value is not acceptable for aga", age)
            elif type(name) != str:
                raise InvalidInputError("Name must be string", name)
            elif type(surname) != str:
                raise InvalidInputError("Surname must be string", surname)
            elif type(gender) != str:
                raise InvalidInputError("Gender must be string", gender)
            else:
                self.__name = name
                self.__surname = surname
                self.__gender = gender
                self.__age = age
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)

    def __repr__(self):
        return "Name: {}; Surname: {}; Gender: {}; Age: {}".format(self.__name, self.__surname, self.__gender, self.__age)


class Student(Person):
    def __init__(self, name, surname, age, gender, university, faculty, course, middle_score):
        super().__init__(name, surname, age, gender)
        try:
            if type(university) != str:
                raise InvalidInputError("University must be string", university)
            elif type(faculty) != str:
                raise InvalidInputError("Faculty must be string", faculty)
            elif type(course) != str:
                raise InvalidInputError("Course must be integer", course)
            elif type(middle_score) != int:
                raise InvalidInputError("Faculty must be integer", middle_score)
            else:
                self.__university = university
                self.__faculty = faculty
                self.__course = course
                self.__middle_score = middle_score
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)

    def __repr__(self):
        return super().__repr__() + ", {} university, {} faculty, {} course, {} score".format(self.__university, self.__faculty, self.__course, self.__middle_score)

    def get_score(self):
        return self.__middle_score

    def set_score(self, val):
        try:
            if type(self.__middle_score) == int:
                self.__middle_score = val
            else:
                raise InvalidInputError("You can set only integer value for Score", val)
        except InvalidInputError as e:
            print("Score value must be number", e)

    def get_course(self):
        return self.__course

    def set_course(self, val):
        try:
            if type(self.__course) == str:
                self.__course = val
            else:
                raise InvalidInputError("You can set only integer value for Course", val)
        except InvalidInputError as e:
            print("Course value must be number", e)

    def get_faculty(self):
        return self.__faculty

    def set_faculty(self, val):
        try:
            if type(self.__faculty) == str:
                self.__faculty = val
            else:
                raise InvalidInputError("You can set only String value for Faculty", val)
        except InvalidInputError as e:
            print("Faculty value must be string", e)

    def get_university(self):
        return self.__university

    def set_university(self, val):
        try:
            if type(self.__university) == str:
                self.__university = val
            else:
                raise InvalidInputError("You can set only String value for University", val)
        except InvalidInputError as e:
            print("University value must be string", e)


class Teacher(Person):
    def __init__(self, name, surname, age, gender, university, faculty, discipline, experience, salary):
        super().__init__(name, surname, age, gender)
        try:
            if type(university) != str:
                raise InvalidInputError("University must be string", university)
            elif type(faculty) != str:
                raise InvalidInputError("Faculty must be string", faculty)
            elif type(discipline) != str:
                raise InvalidInputError("Course must be integer", discipline)
            elif type(experience) != int:
                raise InvalidInputError("Faculty must be integer", experience)
            elif type(salary) != int:
                raise InvalidInputError("Faculty must be integer", salary)
            else:
                self.__university = university
                self.__faculty = faculty
                self.__discipline = discipline
                self.__experience = experience
                self.__salary = Money(salary, "USD")
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)

    def __repr__(self):
        return super().__repr__() + ", {} university, {} faculty, {} discipline, experience - {} month, salary: {}".format(self.__university, self.__faculty, self.__discipline, self.__experience, self.__salary)

    def get_university(self):
        return self.__university

    def set_university(self, val):
        try:
            if type(self.__university) == str:
                self.__university = val
            else:
                raise InvalidInputError("You can set only String value for University", val)
        except InvalidInputError as e:
            print("University value must be string", e)

    def get_faculty(self):
        return self.__faculty

    def set_faculty(self, val):
        try:
            if type(self.__faculty) == str:
                self.__faculty = val
            else:
                raise InvalidInputError("You can set only String value for Faculty", val)
        except InvalidInputError as e:
            print("Faculty value must be string", e)

    def get_discipline(self):
        return self.__discipline

    def set_discipline(self, val):
        try:
            if type(self.__discipline) == str:
                self.__discipline = val
            else:
                raise InvalidInputError("You can set only String value for Discipline", val)
        except InvalidInputError as e:
            print("Discipline value must be string", e)

    def get_experience(self):
        return self.__experience

    def set_experience(self, val):
        try:
            if type(self.__experience) == int or type(self.__experience) == float:
                self.__experience = val
            else:
                raise InvalidInputError("You can set only String value for Experience", val)
        except InvalidInputError as e:
            print("Experience value must be string", e)

    def get_salary(self):
        return self.__salary

    def set_salary(self, val):
        try:
            if type(self.__salary) == int or type(self.__salary) == float:
                self.__salary = val
            else:
                raise InvalidInputError("You can set only Number for Salary", val)
        except InvalidInputError as e:
            print("Salary must be number", e)

s = Student("John", "Doe", 25, "Male", "UCLA", "Business Management", "Project Coordinator", 178)
print(s)
t = Teacher("Mari", "Brown", 48, "Female", "Cambridge", "Natural and applied sciences", "Biology", 15, 200000)
print(t)
