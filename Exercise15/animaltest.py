from package.animal import Animal

tiger = Animal("Tiger")
tiger.legs(4)
tiger.trickList("Roar", "Dance")
print(f"The {tiger.name()} has {tiger.numLeg} legs and can do {tiger.trickList()}")
snake = Animal("Snake")
snake.legs(0)
print(f"The {snake.name()} has {snake.numLeg} legs")
print(Animal.numAnimals)
