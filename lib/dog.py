#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Dog", breed=APPROVED_BREEDS[0]):
        self.set_name(name)
        self.set_breed(breed)
    
    def set_name(self, name):
        if isinstance(name, str) and (1 <= len(name) <= 25):
            self.name = name
        else:
            print("Name must be string between 1 and 25 characters.")
            
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self.breed = breed
        else:
            print("Breed must be in list of approved breeds.")
    

