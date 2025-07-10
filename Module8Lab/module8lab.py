class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
    def speak(self, sound):
        return f"{self.name} says {sound}."
    
pip = Animal("Pip", 6)

print(pip)
print(pip.speak("yip"))

class Dog(Animal):
    def speak(self, sound = "Woof"):
        return super().speak(sound)
    
class Duck(Animal):
    def speak(self, sound = "Quack"):
        return super().speak(sound)
    
class Pig(Animal):
    def speak(self, sound = "Oink"):
        return super().speak(sound)
    
class Cat(Animal):
    def speak(self, sound = "Meow"):
        return super().speak(sound)
    
pip = Dog("Pip", 6)
fox = Dog("Fox", 10)
otho = Cat("Otho", 18)

menagerie = [pip, fox, otho, 12]

for creature in menagerie:
    if isinstance(creature, Animal):
        print(creature)
        print(creature.speak())
