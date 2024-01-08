
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
        super().__init__(name, age)
        self.language = language
        self.experience = experience

    def code(self):
        print( f"I'm: {self.name} with {self.age}  use: {self.language} and have: {self.experience}")





def presentation(name, age, language, experience):
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    language = input("Enter your language: ")
    experience = input("Enter your experience: ")

    person = Programmer(name, age, language, experience)
    return person.code()

