class Animal:
    numLeg = 0
    numAnimals = 0
    tricks = []

    def __init__(self, name):
        self._name = name
        Animal.numAnimals += 1

    def legs(self, amt):
        self.numLeg += amt
        return

    def name(self):
        return self._name

    def trickList(self, trick):
        self.tricks + trick
        return

