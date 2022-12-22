# Importing the Animal Class from the Animal Module
from Animal import Animal


# Indicating that the Bird Class will inherit (attributes and methods) from the Animal Class
class Bird(Animal):

    def __init__(self, sings, nocturnal, name, gender, color, mood):    #constructor
        self.sings = sings              # Instance Variable
        self.nocturnal = nocturnal      # Instance Variable
        self.name = name                # Instance Variable
        self.gender = gender            # Instance Variable
        self.color = color              # Instance Variable
        self.mood = mood                # Instance Variable

    def fly(self):
        print("This animal is flying...")

    def peck(self):
        print("This animal is pecking...")

    def tweet(self):
        print("This animal is tweeting...")