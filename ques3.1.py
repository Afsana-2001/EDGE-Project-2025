class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def speak(self):
        print(f"A {self.species} says {self.sound}.")

anima11 = Animal("Dog", "Woof")
anima11.speak()

anima12 = Animal("Cat", "Meow")
anima12.speak()