import pytest
from stackQueueAnimalShelter import Animal, AnimalShelter

@pytest.fixture
def animal_shelter():
    return AnimalShelter()

def test_enqueue_dequeue_dog(animal_shelter):
    dog1 = Animal("dog", "Buddy")
    dog2 = Animal("dog", "Max")
    animal_shelter.enqueue(dog1)
    animal_shelter.enqueue(dog2)
    assert animal_shelter.dequeue("dog") == dog1

def test_enqueue_dequeue_cat(animal_shelter):
    cat1 = Animal("cat", "Whiskers")
    cat2 = Animal("cat", "Mittens")
    animal_shelter.enqueue(cat1)
    animal_shelter.enqueue(cat2)
    assert animal_shelter.dequeue("cat") == cat1

def test_enqueue_dequeue_mix(animal_shelter):
    dog = Animal("dog", "Buddy")
    cat = Animal("cat", "Whiskers")
    animal_shelter.enqueue(dog)
    animal_shelter.enqueue(cat)
    assert animal_shelter.dequeue("dog") == dog
    assert animal_shelter.dequeue("cat") == cat

def test_enqueue_dequeue_invalid_preference(animal_shelter):
    dog = Animal("dog", "Buddy")
    cat = Animal("cat", "Whiskers")
    animal_shelter.enqueue(dog)
    animal_shelter.enqueue(cat)
    assert animal_shelter.dequeue("invalid") == dog

def test_enqueue_dequeue_empty(animal_shelter):
    assert animal_shelter.dequeue("dog") is None
    assert animal_shelter.dequeue("cat") is None

def test_enqueue_dequeue_oldest(animal_shelter):
    dog1 = Animal("dog", "Buddy")
    dog2 = Animal("dog", "Max")
    cat1 = Animal("cat", "Whiskers")
    cat2 = Animal("cat", "Mittens")
    animal_shelter.enqueue(dog1)
    animal_shelter.enqueue(cat1)
    animal_shelter.enqueue(dog2)
    animal_shelter.enqueue(cat2)
    assert animal_shelter.dequeue("dog") == dog1
    assert animal_shelter.dequeue("cat") == cat1

def test_enqueue_dequeue_no_preference(animal_shelter):
    dog = Animal("dog", "Buddy")
    cat = Animal("cat", "Whiskers")
    animal_shelter.enqueue(dog)
    animal_shelter.enqueue(cat)
    assert animal_shelter.dequeue("") == dog
    assert animal_shelter.dequeue("") == cat


