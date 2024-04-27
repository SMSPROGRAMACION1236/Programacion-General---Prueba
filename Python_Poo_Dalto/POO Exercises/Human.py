
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
            pass
    def sleep(self):
            pass
class Programmer(Human):
    def __init__(self, name, age, language, experience):
        super.__init__(name, age)
        self.language = language
        self.experience = experience

    def code(self):
        print( f"I'm: {self.name} with {self.age} years old , I use: {self.language} and have: {self.experience} years of experience")
class Architect(Human):
    def __init__(self, name, age, degree,  houses: int):
        super().__init__(name, age)
        self.houses = houses
        self.degree=degree
    def show_architect(self):
        print(f"I'm {self.name} with {self.age} years has {self.houses} houses building and  has {self.degree} on architecture")

class Teacher(Human):
    def __init__(self, name, age, subject, school):
        super().__init__(name, age)
        self.subject = subject
        self.school = school
    def show_professor(self):
        print(f"Hi, I'm {self.name} with {self.age} years old, I'm teaching {self.subject} on {self.school}")

class Animal:
    def __init__(self, kind, race) -> None:
        self.kind = kind
        self.race = race
    def show_identify(self):
        print(f"I'm a {self.kind} of the race of: {self.race}")

class Strange(Human, Animal):
    def __init__(self,name, age, kind, race ,danger):
        Human.__init__(self,name, age)
        Animal.__init__(self,kind, race)
        self.danger = danger
    def show_the_danger(self):
        print(f"My name is: {self.name} with : {self.age} years old, I'm a {self.kind} of the race of: {self.race} with a range of danger of {self.danger} points")


