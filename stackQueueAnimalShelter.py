# Import double-ended-queue from collection library
from collections import deque

class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

class AnimalShelter:
    def __init__(self):
        self.dogs = deque()
        self.cats = deque()
        self.timestamp = 0

    def enqueue(self, animal):
        animal.timestamp = self.timestamp
        self.timestamp += 1
        if animal.species == "dog":
            self.dogs.append(animal)
        elif animal.species == "cat":
            self.cats.append(animal)

    def dequeue(self, pref):
        if pref == "dog":
            if self.dogs:
                return self.dogs.popleft()
        elif pref == "cat":
            if self.cats:
                return self.cats.popleft()
        elif pref != "dog" and pref != "cat":
            if self.dogs and self.cats:
                if self.dogs[0].timestamp < self.cats[0].timestamp:
                    return self.dogs.popleft()
                else:
                    return self.cats.popleft()
            elif self.dogs:
                return self.dogs.popleft()
            elif self.cats:
                return self.cats.popleft()

        return None
