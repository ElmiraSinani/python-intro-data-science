from Task_1_5_2_OOP_Money_Class import Money

class Person:
    def __init__(self, name, surname, age, gender):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__gender = gender
    def __str__(self):
        return self.__name+" "+self.__surname+" - "+self.__gender+", "+str(self.__age)+" years old."

class Student(Person):
    def __init__(self, name, surname, age, gender, university, faculty, course, middle_score):
        super().__init__(name, surname, age, gender)
        self.__university=university
        self.__faculty=faculty
        self.__course=course
        self.__middle_score=middle_score
    def __str__(self):
        str = "Student: " + super().__str__()
        str += " University: "+self.get_university()+"; Faculty: "+self.get_faculty()+"; "
        str += "Course: "+self.get_course()+"; Mid Score: "+self.get_score()
        return str
    def get_score(self):
        return str(self.__middle_score)
    def get_course(self):
        return self.__course
    def get_faculty(self):
        return self.__faculty
    def get_university(self):
        return self.__university

class Teacher(Person):
    def __init__(self, name, surname, age, gender, university, faculty, discipline, experience, salary):
        super().__init__(name, surname, age, gender)
        self.__university = university
        self.__faculty = faculty
        self.__discipline = discipline
        self.__experience = experience
        self.__salary = salary
    def __str__(self):
        str = "Teacher: "+super().__str__()+" "
        str += "University: " + self.get_university() + "; Faculty: " + self.get_faculty() + "; "
        str += "Discipline: " + self.get_discipline() + "; Experience: " + self.get_experience() + "; "
        str += "Salary: " + self.get_salary()
        return str
    def get_university(self):
        return self.__university
    def get_faculty(self):
        return self.__faculty
    def get_discipline(self):
        return self.__discipline
    def get_experience(self):
        return str(self.__experience)+" years"
    def get_salary(self):
        return str(Money(self.__salary, "USD"))


s = Student("John", "Doe", 15, "Male", "UCLA", "Business Management", "Project Coordinator", 178)
t = Teacher("Mari", "Brown", 48, "Female", "Cambridge", "Natural and applied sciences", "Biology", 15, 200000)
print(s)
print(t)



