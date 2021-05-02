class Person:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
    def __repr__(self):
        return self.name+" "+self.surname+" - "+self.gender+", "+str(self.age)+" years old"


class Student(Person):
   def __init__(self, p, _university, _faculty, _course, _middle_score):
       pass
    def __repr__(self):
        pass
   def get_score(self):
       pass #return middle score
   def get_course(self):
       pass
   def get_faculty(self):
       pass
   def get_university(self):
       pass


class Teacher(Person):
    def __init__(self, p, _university, _faculty, _discipline, _experience, _salary):
        pass
    def __repr__(self):
        pass
    def get_discipline(self):
       pass
    def get_faculty(self):
        pass
    def get_university(self):
        pass
    def get_experience(self):
        pass
    def get_salary(self):
        pass




