from Task_1_5_2_OOP_Money_Class import Money
from CustomExceptions import InvalidInputError


class Person:
    def __init__(self, name, surname, age, gender):
        self.__name = name
        self.__surname = surname
        self.__gender = gender
        self.__age = age
        try:
            if age < 0:
                raise InvalidInputError("Negative Value is not acceptable for aga")
        except InvalidInputError as e:
            print("CustomValueError Exception!", e)

    def __repr__(self):
        return self.__name+" "+self.__surname+" - "+self.__gender+", "+str(self.__age)+" years old."


class Student(Person):
    def __init__(self, name, surname, age, gender, university, faculty, course, middle_score):
        super().__init__(name, surname, age, gender)
        self.__university = str(university)
        self.__faculty = str(faculty)
        self.__course = str(course)
        self.__middle_score = str(middle_score)

    def __repr__(self):
        s = "Student: " + super().__repr__()
        s += " University: "+self.__university+"; Faculty: "+self.__faculty+"; "
        s += "Course: "+self.__course+"; Mid Score: "+self.__middle_score
        return s

    def get_score(self):
        return self.__middle_score

    def set_score(self, val):
        if type(self.__middle_score) == int or type(self.__middle_score) == float:
            self.__middle_score = val

    def get_course(self):
        return self.__course

    def set_course(self, val):
        if type(self.__course) == int:
            self.__course = val

    def get_faculty(self):
        return self.__faculty

    def set_faculty(self, val):
        if type(self.__faculty) == str:
            self.__faculty = val

    def get_university(self):
        return self.__university

    def set_university(self, val):
        if type(self.__university) == str:
            self.__university = val


class Teacher(Person):
    def __init__(self, name, surname, age, gender, university, faculty, discipline, experience, salary):
        super().__init__(name, surname, age, gender)
        self.__university = str(university)
        self.__faculty = str(faculty)
        self.__discipline = str(discipline)
        self.__experience = str(experience) + " years"
        self.__salary = str(Money(salary, "USD"))

    def __repr__(self):
        s = "Teacher: "+super().__repr__()+" "
        s += "University: " + self.__university + "; Faculty: " + self.__faculty + "; "
        s += "Discipline: " + self.__discipline + "; Experience: " + self.__experience + "; "
        s += "Salary: " + self.__salary
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


s = Student("John", "Doe", 15, "Male", "UCLA", "Business Management", "Project Coordinator", 178)
t = Teacher("Mari", "Brown", 48, "Female", "Cambridge", "Natural and applied sciences", "Biology", 15, 200000)
print(s)
print(t)


