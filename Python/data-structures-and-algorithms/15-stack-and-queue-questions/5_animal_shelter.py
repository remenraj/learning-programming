# An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis.
# People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can
# select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). 
# They cannot select which specific animal they would like.
# Create the data structures to maintain this system and implement operations such as enqueue, dequeue_any
# dequeue_dog, and dequeue_cat

from random import choice


class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []
        
    def enqueue(self, animal, type):
        """Add an animal"""
        if type == "cat":
            self.cats.append(animal)
        elif type == "dog":
            self.dogs.append(animal)
        else:
            raise TypeError("Invalid Type")
        
    def dequeue_cat(self):
        """Remove first cat and returns it"""
        if len(self.cats) == 0:
            return None
        
        else:
            cat = self.cats.pop(0)
            return cat
        
    def dequeue_dog(self):
        """"Remove first dog and returns it"""
        if len(self.dogs) == 0:
            return None
        
        else:
            dog = self.dogs.pop(0)
            return dog
        
    def dequeue_any(self):
        """Remove random animal and returns it"""
        if len(self.cats) == 0 and len(self.dogs) == 0:
            return None
        elif len(self.cats) == 0:
            result = self.dogs.pop(0)
        elif len(self.dogs) == 0:
            result = self.cats.pop(0)
        else:
            # choosing random    
            toss = choice([0, 1])
            if toss == 0:
                result = self.cats.pop(0)   
            else:
                result = self.dogs.pop(0)         
        return result
            

if __name__ == "__main__":
    custom_queue = AnimalShelter()
    custom_queue.enqueue(animal="cat1", type="cat")
    custom_queue.enqueue(animal="cat2", type="cat")
    custom_queue.enqueue(animal="dog1", type="dog")
    custom_queue.enqueue(animal="cat3", type="cat")
    custom_queue.enqueue(animal="dog2", type="dog")
    
    
    print(custom_queue.dequeue_cat())
    print(custom_queue.dequeue_dog())
    print(custom_queue.dequeue_any())
    