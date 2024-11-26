class Animal:
    def __init__(self, name, species, age, adopted):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__adopted = adopted

    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name

    def get_species(self):
        return self.__species
    def set_species(self, new_species):
        self.__species = new_species

    def get_age(self):
        return self.__age
    def set_age(self, new_age):
        self.__age = new_age

    def get_adopted(self):
        return self.__adopted
    def set_adopted(self, new_adopted):
        self.__adopted = new_adopted
    
    def make_sound(self):
        return "This animal makes a sound"

class Dog(Animal):
    def __init__(self, name, species, age, breed, adopted):
        super().__init__(name, species, age, adopted)
        self.__breed = breed
    
    def get_breed(self):
        return self.__breed
    def set_breed(self, new_breed):
        self.__breed = new_breed
    
    def __str__(self):
        return f"Name: {self.get_name()}\nSpecies: {self.get_species()}\nAge: {self.get_age()}\nBreed: {self.get_breed()}\nAdopted status: {self.get_adopted()}"
    
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, species, age, indoor_only, adopted):
        super().__init__(name, species, age, adopted)
        self.__indoor_only = indoor_only
    
    def get_indoor_only(self):
        return self.__indoor_only
    def set_indoor_only(self, new_indoor_only):
        self.__indoor_only = new_indoor_only
    
    def __str__(self):
        return f"Name: {self.get_name()}\nSpecies: {self.get_species()}\nAge: {self.get_age()}\nIndoor only status: {self.get_indoor_only()}\nAdopted status: {self.get_adopted()}"
    
    def make_sound(self):
        return "Meow!"