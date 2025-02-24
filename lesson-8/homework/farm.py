class Animal:
    def __init__(self, name, age, color, can_do, place):
        self.name = name
        self.age = age
        self.color = color
        self.can_do = can_do
        self.place = place

    def make_sound(self):
        return "Animal sound"
    
    def habitat(self):
        if self.place == 'forest':
            return f"{self.name} lives in a forest"
        elif self.place == 'ocean':
             return f"{self.name} lives in the ocean"
        elif self.place == 'desert':
            return f"{self.name} lives in a desert"
        elif self.place == 'land':
            return f"{self.name} lives in a land"
        
    def ability(self):
        if self.can_do == 'vision':
            return f"{self.name} can see nearly 360 degrees around them"
        elif self.can_do == 'fly':
            return f"{self.name} can fly"
        elif self.can_do == 'swim':
            return f"{self.name} can swim"
        elif self.can_do == 'jump':
            return f"{self.name} can jump"
        elif self.can_do == 'underwater breating':
            return f"{self.name} can breathe underwater"
        elif self.can_do == 'run':
            return f"{self.name} can run"
        
    def info(self):
        return f"{self.name} is {self.age} years old. \n{self.habitat()} \n{self.ability()}. It is {self.color}"
        
class Dog(Animal):
    def __init__(self, name, age, color, can_do, place, breed):
        super().__init__(name, age, color, can_do, place)
        self.breed = breed

    def info(self):
        return f"{self.name} is a {self.age} years old {self.breed}. \n{self.habitat()} \n{self.ability()}. It is {self.color}"

    def make_sound(self):
        return 'Woof!'
    
    def fetch(self, item):
        return f"{self.name} can fetch {item}"
    
class Cow(Animal):
    def __init__(self, name, age, color, can_do, place, milk):
        super().__init__(name, age, color, can_do, place)
        self.milk = milk

    def info(self):
        return f"{self.name} is {self.age} years old. \n{self.habitat()} \n{self.ability()}. It is {self.color}. It can give {self.milk} litres of milk"
    
    def make_sound(self):
        return 'Moo!'
    
    def sensibility(self, things):
        return f"{self.name} have an excellent sense of smell. It can smell {things} easily"
    
class Ostrich(Animal):
    def __init__(self, name, age, color, can_do, place, height):
        super().__init__(name, age, color, can_do, place)
        self.heigh = height

    def info(self):
         return f"{self.name} is a {self.age} year old {self.color} ostrich. \n{self.habitat()} \n{self.ability()}. {self.name} can be {self.heigh} meters high."

    def make_sound(self):
        return 'Hiss!'
        
    def diet(self, insects):
        return f"{self.name} eats {insects} in a desert to survive"

my_dog = Dog('Max', 10, 'golden', 'run', 'land', 'Labrador')
print(my_dog.make_sound())
print(my_dog.info())
print(my_dog.fetch('a ball'))
print('* '*15)

my_cow = Cow('Molly', 15, 'brown', 'vision', 'land', 10)
print(my_cow.make_sound())
print(my_cow.info())
print(my_cow.sensibility('food'))
print('* '*15)

my_ostrich = Ostrich('Ozzy', 20, 'white', 'jump', 'desert', 2)
print(my_ostrich.make_sound())
print(my_ostrich.info())
print(my_ostrich.diet('plants, insects and seeds'))
print('* '*15)